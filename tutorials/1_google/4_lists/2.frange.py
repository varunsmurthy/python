# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 21:43:50 2015

@author: Varun
"""

def frange(start_val,stop_val,step):
    curr_val = start_val;
    retn_val = []
    
    retn_val.append(curr_val)
    
    while curr_val<stop_val:
       retn_val.append(curr_val)
       curr_val = curr_val + step 
       
       
    return retn_val
       

def main():
    start_val = 0.5;
    stop_val = 9.5;
    step = 2;
    
    for i in frange(start_val,stop_val,step):
        print(i)

if __name__ == '__main__':
    main()
