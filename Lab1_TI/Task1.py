import scipy.stats
from numpy import log
p = [0.11, 0.10, 0.09, 0.10, 0.12, 0.10, 0.08, 0.07, 0.14, 0.10]
print("ентропія за вбудованою функцією: ", scipy.stats.entropy(p))
h_x = - sum(p * log(p))
print("ентропія за формулою: ", h_x)