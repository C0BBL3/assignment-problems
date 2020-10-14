from euler_estimator import EulerEstimator
import math
import matplotlib.pyplot as plt

def a_n(t, x): return 0.01*(10-x[0])/(math.exp(0.1*(10-x[0]))-1)
def b_n(t, x): return 0.125*math.exp(-x[0]/80)
def a_m(t, x): return 0.1*(25-x[0])/(math.exp(0.1*(25-x[0]))-1)
def b_m(t, x): return 4*math.exp(-x[0]/18)
def a_h(t, x): return 0.07 * math.exp(-x[0]/20)
def b_h(t, x): return 1/(math.exp(0.1*(30-x[0]))+1)
def dn(t, x): return a_n(t, x)*(1 - x[1]) - b_n(t, x)*x[1]
def dm(t, x): return a_m(t, x)*(1 - x[2]) - b_m(t, x)*x[2]
def dh(t, x): return a_h(t, x)*(1 - x[3]) - b_h(t, x)*x[3]
C, V_Na, V_k, V_L, g_bar_Na, g_bar_k, g_bar_l = 1, 115, -12, 10.6, 120, 36,  0.3
def I_Na(t, x): return g_Na(t, x)*(x[0]-V_Na)
def g_Na(t, x): return g_bar_Na * x[2]**3 * x[3]
def I_k(t, x): return g_k(t, x)*(x[0]-V_k)
def g_k(t, x): return g_bar_k * x[1]**4
def I_L(t, x): return g_l(t, x)*(x[0]-V_L)
def g_l(t, x): return g_bar_l
def dV(t, x): return 1/C * (s(t) - I_Na(t, x) - I_k(t, x) - I_L(t, x))
def s(t):
    if 10 <= t <= 11 or 20 <= t <= 21 or 30 <= t <= 40 or 50 <= t <= 51 or 53 <= t <= 54 or 56 <= t <= 57 or 59 <= t <= 60 or 62 <= t <= 63 or 65 <= t <= 66: return 150
    else: return 0
x = 0.07 * (math.e**3 + 1)
intitial_h = x/(x+1)
intitial_n = 1/(1.25*(math.e-1)+1)
intitial_m = 2.5/(2.5+4*(math.e**2.5 - 1))
intitial_V = 0
euler = EulerEstimator([dV, dn, dm, dh], (0, (intitial_V, intitial_n, intitial_m, intitial_h)))
plt.plot([n/2 for n in range(160)], [s(n/2) for n in range(160)])
euler.plot([0, 80], stepsize =0.02)