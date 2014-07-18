#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import os
import glob
from subprocess import Popen, call

try:
    os.makedirs("results")
except os.error:
    pass

# cases = ["case-01", "case-02"]

cmd = "math -noprompt -run \"<<cases/{0}.m; Exit[];\" > results/{0}.txt"
cases = map(lambda fn: os.path.splitext(os.path.split(fn)[1])[0],
            glob.glob("cases/*.m"))

try:
    jobs = [(c, Popen(cmd.format(c), shell=True)) for i, c in enumerate(cases)]
    while True:
        for i, (jobid, p) in enumerate(jobs):
            p.poll()
            code = p.returncode
            if code is not None:
                print("Case '{0}' finished with code {1}".format(jobid, code))
                del jobs[i]
                break
        if not len(jobs):
            break

except KeyboardInterrupt:
    # Horrifying hack to kill all the launched processes.
    call("killall -9 MathKernel", shell=True)
