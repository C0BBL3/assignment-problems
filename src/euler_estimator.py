import matplotlib.pyplot as plt

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
		if self.original_point[0] == x_range[1]: xs, ys = self.get_positions_for_line(x_range, -stepsize)
		else: xs, ys = self.get_positions_for_line(x_range, stepsize)
		for y in [[ys[i][j] for i in range(0, len(ys))] for j in range(0, len(self.point[1]))]: plt.plot(xs, y)
		plt.savefig(filename)
		plt.show()
		
	def get_positions_for_line(self, x_range, stepsize):
		xs_forward, ys_forward = self.get_xs_and_ys(x_range[1],  stepsize)
		xs_backward, ys_backward = self.get_xs_and_ys(x_range[0], -1 * stepsize)
		return xs_backward[1:][::-1] + xs_forward, ys_backward[1:][::-1] + ys_forward

	def get_xs_and_ys(self, x, stepsize):
		self.go_to_input(x, stepsize)
		self.point = [pos for pos in self.original_point]
		return [x for x in self.x_points], [y for y in self.y_points]