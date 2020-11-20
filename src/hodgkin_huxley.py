from euler_estimator import EulerEstimator
import math
import matplotlib.pyplot as plt

class Neuron:
    def __init__(self, stimulus):
        self.stimulus = stimulus
        self.derivatives = [self.dV, self.dn, self.dm, self.dh]
        self.x = 0.07 * (math.e ** 3 + 1)
        self.initial_v = 0
        self.initial_n = 1/(1.25 * (math.e - 1) + 1)
        self.initial_m = 2.5 / (2.5 + 4 * (math.e ** 2.5 - 1))
        self.initial_h = self.x/(self.x + 1)
        self.initial_positions = (0, (self.initial_v, self.initial_n, self.initial_m, self.initial_h))
        self.C = 1
        self.V_Na = 115
        self.V_k = -12
        self.V_L = 10.6
        self.g_bar_Na = 120 
        self.g_bar_k = 36
        self.g_bar_l = 0.3

    def plot_activity(self):
        euler = EulerEstimator(self.derivatives, self.initial_positions)
        plt.plot([n/2 for n in range(160)], [self.stimulus(n/2) for n in range(160)])
        euler.plot([0, 80], stepsize =0.02)

    def dV(self, t, x): return 1/self.C * (self.stimulus(t) - self.I_Na(t, x) - self.I_k(t, x) - self.I_L(t, x))
    def dn(self, t, x): return self.a_n(t, x) * (1 - x[1]) - self.b_n(t, x) * x[1]
    def dm(self, t, x): return self.a_m(t, x) * (1 - x[2]) - self.b_m(t, x) * x[2]
    def dh(self, t, x): return self.a_h(t, x) * (1 - x[3]) - self.b_h(t, x) * x[3]
    def a_n(self, t, x): return 0.01 * (10 - x[0]) / (math.exp(0.1 * (10 - x[0])) - 1)
    def b_n(self, t, x): return 0.125 * math.exp(-x[0] / 80)
    def a_m(self, t, x): return 0.1 * (25 - x[0]) / (math.exp(0.1 * (25 - x[0])) - 1)
    def b_m(self, t, x): return 4 * math.exp(-x[0] / 18)
    def a_h(self, t, x): return 0.07 * math.exp(-x[0] / 20)
    def b_h(self, t, x): return 1 / (math.exp(0.1 * (30 - x[0])) + 1)
    def I_Na(self, t, x): return self.g_Na(t, x) * (x[0] - self.V_Na)
    def g_Na(self, t, x): return self.g_bar_Na * x[2] ** 3 * x[3]
    def I_k(self, t, x): return self.g_k(t, x) * (x[0] - self.V_k)
    def g_k(self, t, x): return self.g_bar_k * x[1] ** 4
    def I_L(self, t, x): return self.g_l(t, x) * (x[0] - self.V_L)
    def g_l(self, t, x): return self.g_bar_l


def stimulus(t):
    if 10 <= t <= 11 or 20 <= t <= 21 or \
            30 <= t <= 40 or 50 <= t <= 51 or \
            53 <= t <= 54 or 56 <= t <= 57 or \
            59 <= t <= 60 or 62 <= t <= 63 or \
            65 <= t <= 66: return 150
    else: return 0

neuron = Neuron(stimulus)
neuron.plot_activity()