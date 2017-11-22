# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 22:08:45 2015

@author: Varun
"""

def main():
    squares = [i*i for i in range(0,5)]
    print('squares =',squares)
    new_squares = squares
    print('new_squares =',new_squares)
    squares_len = len(squares)
    for i in range(0,squares_len):
        new_squares[i] = i*i*i
    print('new_squares =',new_squares)
    print('squares =',squares)

if __name__ == '__main__':
    main()