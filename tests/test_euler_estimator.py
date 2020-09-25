import sys
sys.path.append('src')
from euler_estimator import EulerEstimator

print('\nTesting... \n')

euler = EulerEstimator([(lambda x,y: x + 1)], (1, [4]))

print("    Testing EulerEstimator's calc_derivative()")
assert euler.calc_derivative() == [2], "EulerEstimator's calc_derivative() was not right, it should be [2], but was {}".format(euler.calc_derivative())
print("    EulerEstimator's calc_derivative() Passed!!!\n")

print("    Testing EulerEstimator's step_forward()")
euler.step(0.1)
assert tuple(euler.point) == (1.1, [4.2]), "EulerEstimator's step_forward() was not right, it should be (1.1, [4.2]), but was {}".format(tuple(euler.point))
print("    EulerEstimator's step_forward() Passed!!!\n")

print("    Testing EulerEstimator's calc_derivative()")
assert euler.calc_derivative() == [2.1], "EulerEstimator's calc_derivative() was not right, it should be [2.1], but was {}".format(euler.calc_derivative())
print("    EulerEstimator's calc_derivative() Passed!!!\n")

print("    Testing EulerEstimator's step_forward()")
euler.step(-0.5)
assert (round(euler.point[0],5), [round(x,5) for x in euler.point[1]]) == (0.6, [3.15]), "EulerEstimator's step_forward() was not right, it should be (0.6, 3.15), but was {}".format(tuple(euler.point))
print("    EulerEstimator's step_forward() Passed!!!\n")

print("    Testing EulerEstimator's go_to_input()")
euler.go_to_input(3, 0.5)
assert (round(euler.point[0],5), [round(x,5) for x in euler.point[1]]) == (3, [9.29]), "EulerEstimator's go_to_input() was not right, it should be (3, [9.29]), but was {}".format(tuple(euler.point))
print("    EulerEstimator's go_to_input() Passed!!!\n")

print('--------------------------------------------')

euler_2 = EulerEstimator([(lambda t,x: x[0] + 1), (lambda t,x: x[0] + x[1]), (lambda t,x: 2 * x[1])], (0,(0,0,0)))
print("    Testing EulerEstimator 2's calc_derivative()")
assert euler_2.calc_derivative() == [1,0,0], "EulerEstimator 2's calc_derivative() was not right, it should be [1,0,0], but was {}".format(euler_2.calc_derivative())
print("    EulerEstimator 2's calc_derivative() Passed!!!\n") 

print("    Testing EulerEstimator 2's step_forward()")
euler_2.step(0.1)
assert (round(euler_2.point[0],5), [round(x,5) for x in euler_2.point[1]]) == (0.1, [0.1, 0, 0]), "EulerEstimator 2's step_forward() was not right, it should be (0.1, (0.1, 0, 0)), but was {}".format((round(euler_2.point[0],5), [round(x,5) for x in euler_2.point[1]]))
print("    EulerEstimator 2's step_forward() Passed!!!\n")

print("    Testing EulerEstimator 2's calc_derivative()")
assert euler_2.calc_derivative() == [1.1, 0.1, 0], "EulerEstimator 2's calc_derivative() was not right, it should be [1.1, 0.1, 0], but was {}".format(euler_2.calc_derivative())
print("    EulerEstimator 2's calc_derivative() Passed!!!\n") 

print("    Testing EulerEstimator 2's step_forward()")
euler_2.step(-0.5)
assert (round(euler_2.point[0],5), [round(x,3) for x in euler_2.point[1]]) == (-0.4, [-0.45, -0.05, 0]), "EulerEstimator 2's step_forward() was not right, it should be (-0.4, [-0.45, -0.05, 0.0]), but was {}".format((round(euler_2.point[0],5), [round(x,5) for x in euler_2.point[1]]))
print("    EulerEstimator 2's step_forward() Passed!!!\n")

print("    Testing EulerEstimator 2's go_to_input()")
euler_2.go_to_input(5, 2)
assert (round(euler_2.point[0],5), [round(x,5) for x in euler_2.point[1]]) ==  (5, [10.88, 1.09, -9.58]), "EulerEstimator's go_to_input() was not right, it should be (5, [10.88, 1.09, -9.58]), but was {}".format((round(euler_2.point[0],5), [round(x,5) for x in euler_2.point[1]]))
print("    EulerEstimator 2's go_to_input() Passed!!!\n")

print('All Tests Passed!!!')

euler_3 = EulerEstimator([(lambda t,x: x[0] + 1), (lambda t,x: x[0] + x[1]), (lambda t,x: 2 * x[1])], (5, [10.88, 1.09, -9.58]))
euler_3.plot([-5,5], stepsize = 0.1, filename = 'plot.png')
