import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(-10,11)
fig, axes = plt.subplots(figsize=(12,6))
axes.plot(x, (x**2), color='red', linewidth=3, marker='o', markersize=8, label='x^2')
axes.plot(x, -1*(x**2), 'b--', label='-x^2')
axes.set_xlabel('x')
axes.set_ylabel('x squared')
axes.set_title('sample plot 3')
axes.legend()
fig

# with subplots
MyPlots = plt.subplots(nrows=2, ncols=2, figsize=(14,8))
fig, ((ax1,ax2), (ax3,ax4)) = MyPlots
MyPlots
ax1.plot(np.random.randn(50), c='red', linestyle='--')
ax1.plot([0,1,50],[1,1,1])
ax2.plot(np.random.randn(50), c='green', linestyle=':')
ax3.plot(np.random.randn(50), c='blue', marker='o', linewidth=3)
ax4.plot(np.random.randn(50), c='magenta')
fig

# more systematic subplots
plt.figure(figsize=(14,8))
# here with (3,3) we make a 3*3 grid
ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)     # 'colspan=3' expands the element in (0,0) to 3 columns
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)     # 'colspan=2' expands the element in the first column and second row
ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2)     # 'rowspan=2' expands the element in the third column and second row to 2 rows
ax4 = plt.subplot2grid((3,3), (2,0))
ax5 = plt.subplot2grid((3,3), (2,1))
