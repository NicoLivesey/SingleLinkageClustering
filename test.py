import libclust as lc, numpy as np
import time

start_time = time.time()

np.random.seed(13)
X = np.random.randn(300, 4)
print(X)
X = np.r_[X, X+20, X -10, X+50]
hc = lc.SingleLinkage(X, 4)
print(hc.clusters)

print("--- %s seconds ---" % (time.time() - start_time))