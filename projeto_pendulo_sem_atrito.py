import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

dt = 1/60
L = 1
ymax = 2
theta0 = np.pi/2
w0 = 0
g = 9.81

r = (theta0, w0)
# r = [theta, w]


def f_r(ri):
    thetai, wi = ri
    f_thetai = wi
    f_wi = -g/L*np.sin(thetai)
    
    return np.array([f_thetai, f_wi])


x0 = L*np.sin(r[0])
y0 = ymax - L*np.cos(r[0])

fig, ax = plt.subplots()
ax.set_aspect('equal')
plt.ylim([-0.25,3.05])
plt.xlim([-1.65,1.65])
plt.grid()

xx_chao = [-1.65, 1.65, 1.65,-1.65]
yy_chao = [0, 0, -0.25, -0.25]

xx_mastro = [0, 0]
yy_mastro = [0, ymax]

xx_corda = [0, x0]
yy_corda = [ymax, y0]

h = ax.plot(xx_mastro, yy_mastro, color="gray")
floor = ax.fill(xx_chao, yy_chao, color="black")

ball, = ax.plot([x0], [y0], color="red", marker="o")
l, = ax.plot(xx_corda, yy_corda)


def animate(i):
    global r
    k1 = dt*f_r(r)
    k2 = dt*f_r(r + k1/2)
    k3 = dt*f_r(r + k2/2)
    k4 = dt*f_r(r + k3)
    
    r = r + 1/6*(k1 + 2*k2 + 2*k3 + k4)
    
    theta, w = r
    x = L*np.sin(theta)
    y = ymax - L*np.cos(theta)
    
    xx_corda[1] = x
    yy_corda[1] = y
    
    l.set_data(xx_corda, yy_corda)
    ball.set_data([x], [y])


ani = FuncAnimation(fig, animate, frames=None, interval=dt*1000)
plt.show()