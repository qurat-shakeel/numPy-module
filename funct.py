# -*- coding: utf-8 -*-
"""funct.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nufB0mVYu4Z145f9U9v4F6TO-wKJoF-6
"""

double = lambda x: x*2
print(double(5))

def double(x):
  return x*2

print(double(5))

# example use with filter()
lst = [1,2,3,4,5]
even_lst= list(filter(lambda x: (x%2 == 0), lst))
print(even_lst)

# example use with map()
llst = [1,2,3,4,5]
new_lst = list(map(lambda x: x**2, lst))
print(new_lst)

# example use with reduce()
from functools import reduce
lst = [1,2,3,4,5]
product_lst = reduce(lambda x, y: x*y, lst)
print(product_lst)
