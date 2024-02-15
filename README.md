# pendulum-simulation

-- PT-BR --

Esse programa é o projeto final da minha aula de física computacional e ele consiste em uma simulação de três pêndulos diferentes.

A simulação foi feita utilizando de cálculo númerico com resolução de EDOs pelo método de Runge-Kutta (RK), sendo que as variáveis escolhidas para o sistema variam em cada pêndulo. Os pêndulo simples com e sem atrito utilizam das variáveis theta (ângulo) e omega (velocidade angular), enquanto que o pêndulo duplo (sem atrito) utiliza das variáveis theta1, theta2, omega1 e omega2 (ângulo e velocidade angular de cada partícula). A partir da derivação dos thetas e omegas a cada etapa é determinada a localização das partículas a cada momento (se baseando na altura e posição no eixo x em que elas estão).

Plotagem da animação feita com matplotlib.

-- EN --

This program is the final project for my computational physics class and consists of a simulation of three different pendulums.

The simulation was done using numerical calculus and solving ODEs using the Runge-Kutta (RK4) method, with the variables chosen for the system varying for each pendulum. The simple pendulum with and without friction uses the variables theta (angle) and omega (angular velocity), while the double pendulum (without friction) uses the variables theta1, theta2, omega1 and omega2 (angle and angular velocity of each particle). From the derivation of the thetas and omegas at each step, the location of the particles at each moment is determined (based on their height and position on the x-axis).

Animation plotted with matplotlib.
