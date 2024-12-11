import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
x = np.arange(-10,11)
plt.figure(figsize=(12,6))
plt.title('sample plot 1')
plt.plot(x, x**2)
plt.plot(x, -1*(x**2))

# plotting in subplots
plt.figure(figsize=(12,6))
plt.title('sample plot 2')
plt.subplot(1,2,1)
plt.plot(x, x**2)
plt.plot([0,0,0],[-10,0,100])
plt.legend([' x^2','a vertical line'])
plt.xlabel('x')
plt.ylabel('x squared')

plt.subplot(1,2,2)
plt.plot(x,-1*(x**2))
plt.plot([-10,0,10],[-50,-50,-50])
plt.legend(['-x^2','a horizontal line'])
plt.xlabel('x')
plt.ylabel('x squared')
