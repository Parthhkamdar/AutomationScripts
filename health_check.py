#!/usr/bin/python

import os
import subprocess
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("hostfile",help="This is the file with your hostnames in it to check the connectivity")
args=parser.parse_args()


with open(args.hostfile,"r") as file:
	IPS=file.readlines()

for IP in IPS:
	IP=IP.rstrip()
	command = ['ping'] + \
                  ['-n'] + \
                  ['-c 1'] + \
                  [IP]
	proc = subprocess.Popen(command,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
        returncode = proc.wait()
	print "==========================================================================="
	if returncode==0:
		print "",IP," IS REACHABLE"
	else:
		print "",IP," IS NOT REACHABLE"
