import os
import sys
import subprocess
import shutil

if len(sys.argv) < 3:
	print 'Usage: %s num [1]' % sys.argv[0]
	sys.exit(-1)

fuzz_num = int(sys.argv[1])

for i in range(fuzz_num):
		i_str = str(i)
		fuzz_p = " -S fuzz"+i_str
		#if i == 0 :
		#	fuzz_p = " -M fuzz0"
		run_f = "./afl-fuzz" + fuzz_p+" "+ sys.argv[2]
		print run_f
		p = subprocess.Popen( run_f,shell=True) 
