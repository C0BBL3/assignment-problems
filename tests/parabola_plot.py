import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

euler = EulerEstimator((lambda x: x + 1), (1, 4))
euler.plot([-5,5])