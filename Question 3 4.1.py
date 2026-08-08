import numpy as np

scores_80 = np.array([30,66,75,44,63,65,48,55,23,57,61,80,49,58,61,21])
scaled=scores_80*(100/80)
print(scaled)
#NumPy is used for this formula because NumPy has built in math formulas that
#can be applied to entire arrays and work much faster than Python loops
#this makes it more efficient.
