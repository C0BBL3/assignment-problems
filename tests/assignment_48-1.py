import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

euler = EulerEstimator([(lambda t,x: 0.6 * x[0] - 0.02 * x[0] * x[1]), (lambda t,x: -0.9 * x[1] + 0.02 * x[0] * x[1])], (0, [10, 11]))
euler.plot([0,100], stepsize = 0.001, filename = 'assignment_48-1.png')