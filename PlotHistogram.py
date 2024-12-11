import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

values =  np.random.randn(1000)
plt.subplots(figsize=(14,8))
# plt.hist(values, bins=100, alpha=0.8, histtype='bar', color='steelblue', edgecolor='black')
plt.hist(values, bins=100, alpha=0.8, histtype='step', fill='steelblue', edgecolor='black')
plt.xlim(xmin=-4, xmax=4)
plt.show()

# KDE (kernel density estimation)
from scipy import stats
density=stats.kde.gaussian_kde(values)

plt.subplots(figsize=(12,6))
values = np.linspace(min(values)-10, max(values)+10, 100)

plt.plot(values, density(values), color='#FF7F00')
plt.fill_between(values, 0, density(values), alpha=0.5, color='#FF7F00')
plt.xlim(xmin=-5, xmax=5)

plt.show()
