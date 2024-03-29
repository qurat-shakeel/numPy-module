# -*- coding: utf-8 -*-
"""matplotlib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SwuhGR5NuowtLxSsh-zAdclDvuD6Kf9u
"""

import matplotlib.pyplot as plt
plt.plot([2,4,6,4])
plt.ylabel("Numbers")
plt.xlabel("Indices")
plt.title("MyPlot")
plt.show( )



plt.plot([1,2,3,4],[1,4,9,16])
plt.ylabel("Squares")
plt.xlabel("Numbers")
plt.grid()
plt.show()



plt.plot([1,2,3,4],[1,4,9,16], 'ro')
plt.grid()
plt.show()

import numpy as np
t = np.arange(0,5,0.2)

# blue dashes, red squares and green triangles
plt.plot(t, t**2, 'b--', label='^2')
plt.plot(t,t**2.2, 'rs', label='^2.2')
plt.plot(t,t**2.5, 'g^', label='^2.5')
plt.grid()
plt.legend()  # add legend based on line labels
plt.show()

x=[1,2,3,4]
y=[1,4,9,16]
plt.plot(x,y,linewidth=7)
plt.show()

# using set up
x1=[1,2,3,4]
x2=[1,4,9,16]
y1=[1,2,3,4]
y2=[2,4,6,8]
lines = plt.plot(x1,x2,y1,y1)

# use keyword args
plt.setp(lines[0], color='r', linewidth = 2)


# or MATLAB style string value pairs
plt.setp(lines[1], 'color','grey','linewidth',2)
plt.grid()

# working with multiple figures and axes
def f(t):
  return np.exp(-t)* np.cos(2*np.pi*t)

t1 = np.arange(0,5,0.1)
t2 = np.arange(0,5,0.02)

plt.figure(1)
# the subplot() command specifies numrows, numcols
# fignum where fignum ranges from 1 to numrows*numcols
plt.subplot(211)
plt.grid()
plt.plot(t1,f(t1),'b-')

plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2), 'r--')
plt.show()

plt.figure(1)
plt.subplot(211)
plt.plot([1,2,3])
plt.subplot(212)
plt.plot([4,5,6])

plt.figure(2)
plt.plot([4,5,6])

plt.figure(1)
plt.subplot(211)
plt.title("easy as 1,2,3")
plt.show()