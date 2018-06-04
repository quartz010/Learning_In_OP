#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 'test'
b = '测试'
c = 'test'
print(a, b)
print(len(a))
print(a.encode('ascii'))
print(b.encode('utf-8'))
print('id_a: %d id_b: %d'% (id(a), id(c))) 
if id(a) == id(c):
    print('you see they have same id')

a = input('input some thing :')
print(a)