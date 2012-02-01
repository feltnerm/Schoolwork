#!/usr/bin/env python

import itertools

def cartesian_product(*args):
    return set([e for e in itertools.product(*args)])


