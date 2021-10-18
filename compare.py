#!usr/bin/env python

import os

cmd = "diff -u pre_check_scn01.txt post_check_scn01.txt | colordiff"
os.system(cmd)
