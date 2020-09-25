#import matplotlib.pyplot as plt

class EulerEstimator:
	def __init__(self, derivatives, start_point):
		self.derivatives = derivatives
		self.original_point = list(start_point)
		self.point = list(start_point)
    
	def calc_derivative(self):
		return [derivative(self.point[0], self.point[1]) for derivative in self.derivatives]
    
	def step(self, precision):
		self.point[1] = [self.point[1][i] + precision * derivative for i, derivative in enumerate(self.calc_derivative())]
		self.point[0] += precision

	def go_to_input(self, final_x, precision):
		self.x_points = [self.point[0]]
		self.y_points = [self.point[1]]
		while abs(self.point[0]) < abs(final_x - precision):
			self.step(precision)
			self.x_points.append(self.point[0])
			self.y_points.append(self.point[1])
		self.step(final_x - self.point[0])
		
	def plot(self, x_range, stepsize=0.1, filename='plot.png'):
		plt.style.use('bmh')
		xs, ys = self.get_positions_for_line(x_range, stepsize)
		for i in range(0, len(ys)): plt.plot(xs, ys[i])
		plt.legend(['Line'])
		plt.xlabel('X')
		plt.ylabel('Y')
		plt.title('Graph of Euler Estimator')
		plt.savefig(filename)
		plt.show()

	def get_positions_for_line(self, x_range, stepsize):
		xs_forward, ys_forward = self.get_xs_and_ys(x_range[1], stepsize, True)
		xs_backward, ys_backward = self.get_xs_and_ys(x_range[0], -1 * stepsize, False)
		xs_backward.pop(0)
		ys_backward.pop(0)
		return xs_backward[::-1] + xs_forward, ys_backward[::-1] + ys_forward

	def get_xs_and_ys(self, x_range, stepsize, forward):
		self.go_to_input(x_range, stepsize)
		self.point = [pos for pos in self.original_point]
		return [x for x in self.x_points], [y for y in self.y_points]