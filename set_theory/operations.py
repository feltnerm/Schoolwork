#!/usr/bin/env python

import itertools

def cartesian_product(*args):
    ''' Returns a set of the Cartesian Product of some sets '''
    return set([e for e in itertools.product(*args)])

def positive_divisors(n):
    ''' returns a list of positive divisors of n.
    For example: 6 has four positive divisors [1,2,3,6]
    '''
    return [x for x in range(1, n+1) if n % x == 0]

def perfect(n):
    ''' returns True or False if a number is or is not perfect.
    An integer is called perfect provided it equals the sum of all
    its divisors that are both positive and less than n.
    '''

    return sum([x for x in positive_divisors(n) if x != n]) == n
