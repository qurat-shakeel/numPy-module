# -*- coding: utf-8 -*-
"""reviseloops.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AxNACELAz5vk-wJ_SAl4kkwQf-gF6kUd
"""

# find product of all numbers in a list
lst = [10,20,30,40,50]
product = 1
# iterating over a list
for ele in lst:
  product *= ele

print("product is : {}". format(product))

# range function
for i in range(10):
  print(i)

for i in range(1,20,2):
  print(i)

lst = ["satish","arinu","murali","naveen"]
for index in range(len(lst)):
  print(lst[index])

lst = ["satish","arinu","murali","naveen"]
for ele in lst:
  print(ele)

numbers = [1,2,3]

for item in numbers:
  print(item)

else:
  print("no item left")

# print prime numbers
index1 = 20
index2 = 50
print("Prime numbers between {0} and {1} are :".format(index1,index2))

for num in range(index1, index2+1):
  if num>1:
      isDivisible = False
      for index in range(2,num):
          if num % index == 0:
              isDivisible = True
      if not isDivisible:
          print(num)