import matplotlib.pyplot as plt

class EulerEstimator:
	def __init__(self, derivative, start_point):
		self.derivative = derivative
		self.original_point = list(start_point)
		self.point = list(start_point)
    
	def calc_derivative(self):
		return self.derivative(self.point[0])
    
	def step(self, precision):
		self.point[1] += self.calc_derivative() * precision
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
		plt.plot(xs, ys)
		plt.legend(['Line'])
		plt.xlabel('X')
		plt.ylabel('Y')
		plt.title('Graph of Euler Estimator')
		plt.savefig(filename)
		plt.show()

	def get_positions_for_line(self, x_range, stepsize):
		xs_forward, ys_forward = self.get_xs_and_ys(x_range, stepsize, True)
		xs_backward, ys_backward = self.get_xs_and_ys(x_range, stepsize, False)
		xs_backward.pop(0)
		xs_backward.reverse()
		ys_backward.pop(0)
		ys_backward.reverse()
		return xs_backward + xs_forward, ys_backward + ys_forward

	def get_xs_and_ys(self, x_range, stepsize, forward):
		if forward:
			self.go_to_input(x_range[1], stepsize)
			self.point = [pos for pos in self.original_point]
			return [x for x in self.x_points], [y for y in self.y_points]
		else:
			self.go_to_input(x_range[0], -1 * stepsize)
			self.point = [pos for pos in self.original_point]
			return [x for x in self.x_points], [y for y in self.y_points]