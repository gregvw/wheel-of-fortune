#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
How many valid solutions are there to this Wheel of Fortune puzzle?
    
https://www.youtube.com/watch?v=BobNg1-CSH4

This code determines the number of valid solutions and displays 10 
example solutions

--------------------------------------------------------------------------

Copyright (c) 2014 Greg von Winckel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

import os
import urllib2
from operator import mul
import random

if __name__ == '__main__':
  
    # List of valid words (lower case). One word per line. Alphabetical order
    filename = "wordsEn.txt"

    # The four and five letter words contain none of these letters
    # and the three letter word can not have these as its last letter    
    invalid_letters = ['r','s','t','l','n','e','h','m','d','o']

    def valid_word(s):
        return not any([c for c in s if c in invalid_letters])

    # If word file does not exist in current working directory, download it    
    if not os.path.isfile(filename):
        url = "http://www-01.sil.org/linguistics/wordlists/english/wordlist/"
        response = urllib2.urlopen(''.join([url,filename]))
        text = response.read()
        f = open(filename,'wb')
        f.write(text)
        f.close()

    # Read file so that each line is a string element in a list and strip
    # line break characters off
    wordlist = [line.strip() for line in open(filename,'rb')]

    # Get all valid word lengths
    wlen = set(len(w) for w in wordlist)

    # Make a dictionary where words are grouped by length
    D = {k:[] for k in wlen}
    [D[len(w)].append(w) for w in wordlist] 

    # Get all three letter words that begin with 'ne' but do not 
    # contain an invalid third letter

    three = set(w for w in D[3] if w[:2]=='ne' and w[-1] not in invalid_letters)

    # Get all four letter words that contain no invalid letters
    four = set(w for w in D[4] if valid_word(w))

    # Get all four letter words that contain no invalid letters
    five = set(w for w in D[5] if valid_word(w))

    valid = [three,four,five]

    # Number of valid words of each type
    number = [len(v) for v in valid]
    
    combos = reduce(mul,number,1)

    print('There are %d valid combinations' % combos)

    print('Here are ten valid solutions:')

    # Display 10 random valid solutions
    for k in range(10):
        print(' '.join([random.choice(list(v)) for v in valid]))
   
    
