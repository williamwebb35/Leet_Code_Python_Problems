# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 06:47:03 2022

@author: sinua
"""
# Given a roman numeral, convert it to an integer.

rom_dict = {'I':1, 'V':5,'X':10, 'L':50,'C':100,'D':500,'M':'1000'}

#break string into components
# LEFT OFF: conditionals for subtraction

def rom(rn):
    
    #make dict of subraction numbers
    sub_dict = {'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
      
    sub_list = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    
    #handle the subtraction numbers if present in the argument
    sub_nums = []
    for i in sub_list:
        if i in rn:
            #print('yes')
            rn = rn.replace(i,'')#remove subtraction numbers from rn
            #print('new:',rn)
            sub_nums.append(i)
    
    sub_nums_value = 0
    for num in sub_nums:
        sub_nums_value += sub_dict[num]
    
    rom_dict = {'I':1, 'V':5,'X':10, 'L':50,'C':100,'D':500,'M':1000}
    
    rom_nums = []
    for i in rn:
        rom_nums.append(i)
    
    rom_nums_value = 0
    for num in rom_nums:
        rom_nums_value += rom_dict[num]
    
    total = rom_nums_value + sub_nums_value
    
    return (total)
        







