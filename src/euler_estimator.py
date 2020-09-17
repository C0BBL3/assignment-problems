class EulerEstimator:
    def __init__(self, derivative, start_point):
        self.derivative = derivative
        self.point = list(start_point)
    
    def calc_derivative(self):
        return self.derivative(self.point[0])
    
    def step_forward(self, precision):
        self.point[1] += self.calc_derivative() * precision
        self.point[0] += precision

    def go_to_input(self, final_x, precision):
        while self.point[0] < final_x - precision:
            self.step_forward(precision)
        self.step_forward(final_x - self.point[0])