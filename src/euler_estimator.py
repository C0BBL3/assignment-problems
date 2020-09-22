import matplotlib.pyplot as plt
plt.style.use('bmh')

class EulerEstimator:
    def __init__(self, derivative, start_point):
        self.derivative = derivative
        self.point = list(start_point)
    
    def calc_derivative(self):
        return self.derivative(self.point[0])
    
    def step(self, precision, if_return_point = False):
        self.point[1] += self.calc_derivative() * precision
        self.point[0] += precision
        if if_return_point: return self.point

    def go_to_input(self, final_x, precision):
        while self.point[0] < final_x - precision:
            self.step(precision)
        self.step(final_x - self.point[0])
		
    def plot(self, x_range, stepsize=0.1, filename='plot.png'):
        original_point = self.point
        xs = [round(i*stepsize,1) for i in range(x_range[0], int(x_range[1]/stepsize)+1)]
		ys_1 = [self.step(stepsize, if_return_point=True) for x in xs[:original_point[0]]]
		self.point = original_point
        ys_2 = [self.step(stepsize, if_return_point=True) for x in xs[original_point[0]:]]
        self.point = original_point
        plt.plot(xs, ys_1 + ys_2)
        plt.legend(['Line'])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Graph of Euler Estimator')
        plt.savefig(filename)
        plt.show()