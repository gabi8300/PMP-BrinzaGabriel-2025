import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
lam_posibil = [1, 2, 5, 10]

poisson_random_1 = np.random.poisson(lam=1, size=1000)
print(poisson_random_1 + [1, 2])