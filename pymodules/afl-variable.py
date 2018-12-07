#!/usr/bin/env python2

from shutil import rmtree
from sys import argv
from tempfile import NamedTemporaryFile
import errno
import re
import glob
import string
import argparse
import time
import signal
import sys, os

try:
    import subprocess32 as subprocess
except ImportError:
    import subprocess

def run_cmd(cmd, cargs):
    out = []
    if cargs.verbose:
        print "    CMD: %s" % cmd
    fh = None
    fh = NamedTemporaryFile(delete=False)
    es = subprocess.call(cmd, stdin=None,
            stdout=fh, stderr=subprocess.STDOUT, shell=True)
    fh.close()
    with open(fh.name, 'r') as f:
        for line in f:
            out.append(line.rstrip('\n'))
    os.unlink(fh.name)
    #if (es != 0) :
     #   print "    Non-zero exit status '%d' for CMD: %s" % (es, cmd)

    return es, out

def main():
    cov_paths = {}
    cargs = parse_cmdline()
    diff      = {}
    
#    coverage_diff(cov_paths, cargs, diff)
#    return 1

    import_fuzzing_dirs(cov_paths, cargs)
    
    for fuzz_dir in cov_paths['dirs']:
        new_files = []
        tmp_files = import_test_cases(fuzz_dir + '/queue/.state/variable_behavior/')

        for f in tmp_files:
            new_files.append(f)
        
        init_run(cov_paths, cargs)
        for f in new_files:
            cov_paths['diff'] = "%s/%s" % (cov_paths['diff_dir'], os.path.basename(f))
            log_lines = []
            init_counter(cov_paths, cargs)
            run_cmd(cargs.coverage_cmd.replace('AFL_FILE', f), cargs)
            ### generate the first time code coverage stats for this test case
            lcov_gen_coverage(cov_paths, cargs)

            for num in range(1,4):
                cov_paths['detail'] = "%s/%s__%d" % (cov_paths['diff_dir'], os.path.basename(f), num)
                init_counter(cov_paths, cargs)
                run_cmd(cargs.coverage_cmd.replace('AFL_FILE', f), cargs)
                ### generate the first time code coverage stats for this test case
                lcov_gen_coverage_again(cov_paths, cargs)
                coverage_diff(cov_paths, cargs, diff)

            if len(diff):
                for f in diff:
                    log_lines.append(f)
                    for ctype in diff[f]:
                        log_lines.append(ctype)
                        for val in diff[f][ctype]:
                            log_lines.append(val+": "+diff[f][ctype][val])

            if len(log_lines):
                for l in log_lines:
                    #print "%s" % l
                    append_file(l, cov_paths['diff'])
            #break
    return 1

def coverage_diff(cov_paths, cargs, diff):
    new_cov = extract_coverage(cov_paths['lcov_info_first'], cargs)
    old_cov = extract_coverage(cov_paths['lcov_info_next'], cargs)
    detail_lines = []
    for f in new_cov:
        print_file_name=True
        for ctype in new_cov[f]:
            for val in sorted(new_cov[f][ctype]):
                if old_cov[f][ctype][val] != new_cov[f][ctype][val]:
                    if print_file_name:
                        detail_lines.append(f)
                        print_file_name=False
                    cov_init(f,diff)
                    if old_cov[f][ctype][val] == '0' or new_cov[f][ctype][val] == '0':
                        diff[f][ctype][val]='0'
                    else:
                        diff[f][ctype][val]='1'
                    detail_lines.append(ctype + val+" :"+old_cov[f][ctype][val]+" vs. "+new_cov[f][ctype][val])

    if len(detail_lines):
        for l in detail_lines:
            #print "%s" % l
            append_file(l, cov_paths['detail'])
    return

def append_file(pstr, path):
    f = open(path, 'a')
    f.write("%s\n" % pstr)
    f.close()
    return

def extract_coverage(lcov_file, cargs):
    search_rv = False
    tmp_cov = {}
    ### populate old lcov output for functions/lines that were called
    ### zero times
    with open(lcov_file, 'r') as f:
        current_file = ''
        for line in f:
            line = line.strip()

            m = re.search('SF:(\S+)', line)
            if m and m.group(1):
                current_file = m.group(1)
                cov_init(current_file, tmp_cov)
                continue

            if current_file:
                m = re.search('^FNDA:(\d+),(\S+)', line)
                if m and m.group(2):
                    fcn = m.group(2) + '()'
                    tmp_cov[current_file]['function'][fcn] = m.group(1)
                    continue

                ### look for lines that were never called
                m = re.search('^DA:(\d+),(\d+)', line)
                if m and m.group(1):
                    lnum = m.group(1)
                    tmp_cov[current_file]['line'][lnum] = m.group(2)

    return tmp_cov

def cov_init(cfile, cov):
    if cfile not in cov:
        cov[cfile] = {}
        cov[cfile]['function'] = {}
        cov[cfile]['line'] = {}
    return

def lcov_gen_coverage(cov_paths, cargs):
    out_lines = []
    lcov_opts = ''
    if cargs.enable_branch_coverage:
        lcov_opts += ' --rc lcov_branch_coverage=1'
    if cargs.follow:
        lcov_opts += ' --follow'

    run_cmd(cargs.lcov_path + lcov_opts + " --no-checksum -c -d " + cargs.code_dir + " -o " \
                + cov_paths['lcov_info'], cargs)

    if (cargs.disable_lcov_exclude_pattern):
        out_lines = run_cmd(cargs.lcov_path \
                + lcov_opts
                + " --no-checksum -a " + cov_paths['lcov_base'] \
                + " -a " + cov_paths['lcov_info'] \
                + " -o " + cov_paths['lcov_info_first'], cargs)[1]
    else:
        tmp_file = NamedTemporaryFile(delete=False)
        run_cmd(cargs.lcov_path \
                + lcov_opts
                + " --no-checksum -a " + cov_paths['lcov_base'] \
                + " -a " + cov_paths['lcov_info'] \
                + " -o " + tmp_file.name, cargs)
        out_lines = run_cmd(cargs.lcov_path \
                + lcov_opts
                + " --no-checksum -r " + tmp_file.name \
                + " " + cargs.lcov_exclude_pattern + "  -o " \
                + cov_paths['lcov_info_first'], cargs)[1]
        if os.path.exists(tmp_file.name):
            os.unlink(tmp_file.name)

    return

def lcov_gen_coverage_again(cov_paths, cargs):
    out_lines = []
    lcov_opts = ''
    if cargs.enable_branch_coverage:
        lcov_opts += ' --rc lcov_branch_coverage=1'
    if cargs.follow:
        lcov_opts += ' --follow'
    run_cmd(cargs.lcov_path \
            + lcov_opts
            + " --no-checksum --capture --directory " \
            + cargs.code_dir + " --output-file " \
            + cov_paths['lcov_info'], cargs)

    if (cargs.disable_lcov_exclude_pattern):
        out_lines = run_cmd(cargs.lcov_path \
                + lcov_opts
                + " --no-checksum -a " + cov_paths['lcov_base'] \
                + " -a " + cov_paths['lcov_info'] \
                + " --output-file " + cov_paths['lcov_info_next'], \
                cargs)[1]
    else:
        tmp_file = NamedTemporaryFile(delete=False)
        run_cmd(cargs.lcov_path \
                + lcov_opts
                + " --no-checksum -a " + cov_paths['lcov_base'] \
                + " -a " + cov_paths['lcov_info'] \
                + " --output-file " + tmp_file.name, \
                cargs)
        out_lines = run_cmd(cargs.lcov_path \
                + lcov_opts
                + " --no-checksum -r " + tmp_file.name \
                + " " + cargs.lcov_exclude_pattern + "  --output-file " \
                + cov_paths['lcov_info_next'], cargs)[1]
        if os.path.exists(tmp_file.name):
            os.unlink(tmp_file.name)
    return

def is_dir(dpath):
    return os.path.exists(dpath) and os.path.isdir(dpath)

def mkdirs(cov_paths, cargs):
    if is_dir(cov_paths['top_dir']):
        if cargs.overwrite:
            rmtree(cov_paths['top_dir'])
            create_cov_dirs = True
    else:
        create_cov_dirs = True

    if create_cov_dirs:
        for k in ['top_dir', 'web_dir', 'lcov_dir', 'diff_dir']:
            if not is_dir(cov_paths[k]):
                os.mkdir(cov_paths[k])
    return

def import_test_cases(qdir):
    return sorted(glob.glob(qdir + "/id:*"))

def add_dir(fdir, cov_paths):
    cov_paths['dirs'][fdir] = {}
    return

def import_fuzzing_dirs(cov_paths, cargs):
    if not cargs.afl_fuzzing_dir:
        print "[*] Must specify AFL fuzzing dir with --afl-fuzzing-dir or -d"
        return False

    if 'top_dir' not in cov_paths:
        if not init_tracking(cov_paths, cargs):
            return False

    def_dir = cargs.afl_fuzzing_dir

    if is_dir("%s/queue" % def_dir):
        if def_dir not in cov_paths['dirs']:
            add_dir(def_dir, cov_paths)
    else:
        for p in os.listdir(def_dir):
            fuzz_dir = "%s/%s" % (def_dir, p)
            if is_dir(fuzz_dir):
                if is_dir("%s/queue" % fuzz_dir):
                    ### found an AFL fuzzing directory instance from
                    ### parallel AFL execution
                    if fuzz_dir not in cov_paths['dirs']:
                        add_dir(fuzz_dir, cov_paths)
    return True

def init_tracking(cov_paths, cargs):
    cov_paths['dirs'] = {}
    cov_paths['top_dir']  = "%s/cov"  % cargs.afl_fuzzing_dir
    cov_paths['web_dir']  = "%s/web"  % cov_paths['top_dir']
    cov_paths['lcov_dir'] = "%s/lcov" % cov_paths['top_dir']
    cov_paths['diff_dir'] = "%s/diff" % cov_paths['top_dir']
    ### raw lcov files
    cov_paths['lcov_base']       = "%s/trace.lcov_base" % cov_paths['lcov_dir']
    cov_paths['lcov_info']       = "%s/trace.lcov_info" % cov_paths['lcov_dir']
    cov_paths['lcov_info_first'] = "%s/trace.lcov_info_first" % cov_paths['lcov_dir']
    cov_paths['lcov_info_next'] = "%s/trace.lcov_info_next" % cov_paths['lcov_dir']

    if cargs.overwrite:
        mkdirs(cov_paths, cargs)
    else:
        if is_dir(cov_paths['top_dir']):
            if not cargs.func_search and not cargs.line_search:
                print "[*] Existing coverage dir %s found, use --overwrite to " \
                        "re-calculate coverage" % (cov_paths['top_dir'])
                return False
        else:
            mkdirs(cov_paths, cargs)
    return True

def init_run(cov_paths, cargs):
    ### reset code coverage counters
    run_cmd(cargs.lcov_path + " --no-checksum -z -d " + cargs.code_dir, cargs)
    run_cmd(cargs.lcov_path + " --no-checksum -c -i -d " + cargs.code_dir + " -o " + cov_paths['lcov_base'], cargs)

def init_counter(cov_paths, cargs):
    ### reset code coverage counters
    run_cmd(cargs.lcov_path + " --no-checksum -z -d " + cargs.code_dir, cargs)

def parse_cmdline():
    p = argparse.ArgumentParser()

    p.add_argument("-e", "--coverage-cmd", type=str,
            help="Set command to exec (including args, and assumes code coverage support)")
    p.add_argument("-d", "--afl-fuzzing-dir", type=str,
            help="top level AFL fuzzing directory")
    p.add_argument("-c", "--code-dir", type=str,
            help="Directory where the code lives (compiled with code coverage support)")
    p.add_argument("-O", "--overwrite", action='store_true',
            help="Overwrite existing coverage results", default=False)
    p.add_argument("--lcov-path", type=str,
            help="Path to lcov command", default="/usr/bin/lcov")
    p.add_argument("-v", "--verbose", action='store_true',
            help="Verbose mode", default=False)
    p.add_argument("--enable-branch-coverage", action='store_true',
            help="Include branch coverage in code coverage reports (may be slow)",
            default=False)
    p.add_argument("-f", "--follow", action='store_true',
            help="Follow links when searching .da files", default=False)
    p.add_argument("--disable-lcov-exclude-pattern", action='store_true',
            help="Allow default /usr/include/* pattern to be included in lcov results",
            default=False)
    p.add_argument("--lcov-exclude-pattern", type=str,
            help="Set exclude pattern for lcov results",
            default="/usr/include/\*")
    p.add_argument("--genhtml-path", type=str,
            help="Path to genhtml command", default="/usr/bin/genhtml")
    return p.parse_args()

if __name__ == "__main__":
    sys.exit(main())

