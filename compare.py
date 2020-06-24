#!usr/bin/env python

import os

cmd = "diff -u pre_check_file.txt post_check_file.txt | colordiff"
os.system(cmd)

