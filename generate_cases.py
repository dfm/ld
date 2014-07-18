#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function

import os

bd = "cases"
try:
    os.makedirs(bd)
except os.error:
    pass

template = open("template.m", "r").read()
assumptions0 = ["g1 + g2 < 1", "z >= 0", "p > 0"]
cases = map(lambda l: "(" + " && ".join(l) + ")", [
    ["z == 0", "p < 1"],
    ["z <= p - 1"],
    ["z < p", "z < 1-p"],
    ["z < p", "z == 1-p"],
    ["z < p"],
    ["z == p", "z < 1 - p"],
    ["z == 1/2", "p == 1/2"],
    ["z == p"],
    ["z < 1 - p"],
    ["z == 1 - p"],
    ["z < 1 + p"],
])

for i, case in enumerate(cases):
    assumptions = assumptions0 + map("!{0}".format, cases[:i]) + [cases[i]]
    with open(os.path.join(bd, "case-{0:02d}.m".format(i+1)), "w") as f:
        f.write(template.replace("{ASSUMPTIONS}", " && ".join(assumptions)))

assumptions = assumptions0 + map("!{0}".format, cases)
with open(os.path.join(bd, "case-{0:02d}.m".format(len(cases)+1)), "w") as f:
    f.write(template.replace("{ASSUMPTIONS}", " && ".join(assumptions)))
