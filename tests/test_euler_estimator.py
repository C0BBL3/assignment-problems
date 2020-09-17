import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

print('\nTesting... \n')

euler = EulerEstimator((lambda x: x + 1), (1, 4))

print("    Testing EulerEstimator's calc_derivative()")
assert euler.calc_derivative() == 2, "EulerEstimator's calc_derivative() was not right, it should be 2, but was {}".format(euler.calc_derivative())
print("    EulerEstimator's calc_derivative() Passed!!!\n")

print("    Testing EulerEstimator's step_forward()")
euler.step_forward(0.1)
assert tuple(euler.point) == (1.1, 4.2), "EulerEstimator's step_forward() was not right, it should be (1.1, 4.2), but was {}".format(tuple(euler.point))
print("    EulerEstimator's step_forward() Passed!!!\n")

print("    Testing EulerEstimator's calc_derivative()")
assert euler.calc_derivative() == 2.1, "EulerEstimator's calc_derivative() was not right, it should be 2.1, but was {}".format(euler.calc_derivative())
print("    EulerEstimator's calc_derivative() Passed!!!\n")

print("    Testing EulerEstimator's step_forward()")
euler.step_forward(-0.5)
assert (round(euler.point[0],5), round(euler.point[1],5)) == (0.6, 3.15), "EulerEstimator's step_forward() was not right, it should be (0.6, 3.15), but was {}".format(tuple(euler.point))
print("    EulerEstimator's step_forward() Passed!!!\n")

print("    Testing EulerEstimator's go_to_input()")
euler.go_to_input(3, 0.5)
assert (round(euler.point[0],5), round(euler.point[1],5)) == (3, 9.29), "EulerEstimator's go_to_input() was not right, it should be (3, 9.29), but was {}".format(tuple(euler.point))
print("    EulerEstimator's go_to_input() Passed!!!\n")

print('All Tests Passed!!!')