import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

euler = EulerEstimator([(lambda t,x: -0.0003 * x[0] * x[1]), (lambda t,x: -0.02 * x[1] + 0.0003 * x[0] * x[1]), (lambda t,x: 0.02 * x[1])], (0, [1000, 1, 0]))
euler.plot([0,350], stepsize = 0.001, filename = 'assignment_50-2.png')