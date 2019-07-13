#!/usr/bin/env python
import os
import subprocess
import shutil
import logging
import urlllib

def run_command(args, wait=False):
    try:
        if (wait):
            p = subprocess.Popen(args, stdout = subprocess.PIPE)
            p.wait()
        else:
            p = subprocess.Popen(args, stdin = None, stdout = None, stderr = None, close_fds = True)
        (result, error) = p.communicate()
    except subprocess.CalledProcessError as e:
        sys.stderr.write("common::run_command() : [ERROR]: output = %s, error code = %s\n" % (e.output, e.returncode))
        
##Your code goes here ##
