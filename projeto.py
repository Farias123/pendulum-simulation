import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
  
theta0_1 = np.pi*3/4
theta0_2 = np.pi/2
    
dt = 1/60
L1 = 1
L2 = 1
ymax = 2.125
w0_1 = 0
w0_2 = 0
g = 9.81
raio_esf = 0.05
m1 = 0.05
m2 = 0.05
D = 0

r = (theta0_1, w0_1, theta0_2, w0_2)
# r = [theta_1, w_1, theta_2, w_2]


def f_r(ri):
    thetai_1, wi_1, thetai_2, wi_2 = ri
    
    f_thetai_1 = wi_1
    
    comp_w1 = -g*(2*m1+m2)*np.sin(thetai_1) - m2*g*np.sin(thetai_1 - 2*thetai_2)
    comp_w1 += - 2*np.sin(thetai_1 - thetai_2)*m2*(wi_2**2*L2 + wi_1**2*L1*np.cos(thetai_1 - thetai_2))
    f_wi_1 = comp_w1/(L1*(2*m1 + m2 - m2*np.cos(2*thetai_1 - 2*thetai_2)))

    f_thetai_2 = wi_2

    comp_w2 = wi_2**2*L2*m2*np.cos(thetai_1 - thetai_2)
    comp_w2 = 2*np.sin(thetai_1 - thetai_2)*(wi_1**2*L1*(m1+m2) + g*(m1+m2)*np.cos(thetai_1) + comp_w2)
    f_wi_2 = comp_w2/(L2*(2*m1 + m2 - m2*np.cos(2*thetai_1 - 2*thetai_2)))
    
    return np.array([f_thetai_1, f_wi_1, f_thetai_2, f_wi_2])


x0_1 = L1*np.sin(r[0])
y0_1 = ymax - L1*np.cos(r[0])

x0_2 = x0_1 + L2*np.sin(r[2])
y0_2 = y0_1 - L2*np.cos(r[2])

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_ylim([-0.125,(ymax+L1+L2)])
ax.set_xlim([-(L1+L2+ymax)/2,(L1+L2+ymax)/2])
ax.set_title('Pêndulo duplo')

xx_chao = [-2, 2, 2,-2]
yy_chao = [0, 0, -0.125, -0.125]

xx_mastro = [0, 0]
yy_mastro = [0, ymax]

xx_corda_1 = [0, x0_1]
yy_corda_1 = [ymax, y0_1]

xx_corda_2 = [x0_1, x0_2]
yy_corda_2 = [y0_1, y0_2]

xx_history_1 = [x0_1]
yy_history_1 = [y0_1]

xx_history_2 = [x0_2]
yy_history_2 = [y0_2]

h = ax.plot(xx_mastro, yy_mastro, color="gray")
floor = ax.fill(xx_chao, yy_chao, color="black")

ball_1, = ax.plot([x0_1], [y0_1], color="red", marker="o")
ball_2, = ax.plot([x0_2], [y0_2], color="blue", marker="o")

hist1, = ax.plot(xx_history_1, yy_history_1, color="red", alpha=0.15, ls="-")
hist2, = ax.plot(xx_history_2, yy_history_2, color="blue", alpha=0.15, ls="-")

l1, = ax.plot(xx_corda_1, yy_corda_1)
l2, = ax.plot(xx_corda_2, yy_corda_2)

ax.grid()


def animate(i):
    global r
    k1 = dt*f_r(r)
    k2 = dt*f_r(r + k1/2)
    k3 = dt*f_r(r + k2/2)
    k4 = dt*f_r(r + k3)
    
    r = r + 1/6*(k1 + 2*k2 + 2*k3 + k4)

    theta_1, w_1, theta_2, w_2 = r
    
    x1 = L1*np.sin(theta_1)
    y1 = ymax - L1*np.cos(theta_1)
    
    x2 = x1 + L2*np.sin(theta_2)
    y2 = y1 - L2*np.cos(theta_2)
    
    xx_history_1.append(x1)
    yy_history_1.append(y1)
    
    xx_history_2.append(x2)
    yy_history_2.append(y2)
    
    if len(xx_history_1) > 600:
        xx_history_1.pop(0)
        yy_history_1.pop(0)
        xx_history_2.pop(0)
        yy_history_2.pop(0)
    
    xx_corda_1[1] = x1
    yy_corda_1[1] = y1
    
    xx_corda_2 = x1, x2
    yy_corda_2 = y1, y2
    
    ball_1.set_data([x1], [y1])
    ball_2.set_data([x2], [y2])
    l1.set_data(xx_corda_1, yy_corda_1)
    l2.set_data(xx_corda_2, yy_corda_2)    
    hist1.set_data(xx_history_1, yy_history_1)
    hist2.set_data(xx_history_2, yy_history_2)


ani = FuncAnimation(fig, animate, frames=None, interval=dt*1000)
plt.show()
