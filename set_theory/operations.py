#!/usr/bin/env python

import itertools
import math
from math import ceil, pi, e


def divisor(a,b):
    ''' Returns true if there exists an integer c 
    such that a = bc .
    '''
    return a % b == 0
def prime(n):
    ''' Returns true/false based on n's primality. '''
    roof = ceil(pow(n, 0.5)) + 1
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in xrange(1, int(roof)):
        if x % n == 0:
            return False
    return True

def stirling(n, stdout=False):
    ''' approximates n! using James Stirling's equation:

    n! ~= sqrt(2*pi*n)*n^n*e^-n
    '''
    if stdout:
        print 'sqrt(2*%d*%d) * %d^%d * %d^%d' %(pi, n, n, n, e, (n*-1))
    return pow(2*pi*n, .5)*pow(n,n)*pow(e, (n*-1))
    

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
