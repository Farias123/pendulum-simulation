# pendulum-simulation

Esse programa é o projeto final da minha aula de física computacional e ele consiste em uma simulação de três pêndulos diferentes.

A simulação foi feita utilizando de cálculo númerico com resolução de EDOs pelo método de Runge-Kutta (RK), sendo que as variáveis escolhidas para o sistema variam em cada pêndulo. Os pêndulo simples com e sem atrito utilizam das variáveis theta (ângulo) e omega (velocidade angular), enquanto que o pêndulo duplo (sem atrito) utiliza das variáveis theta1, theta2, omega1 e omega2 (ângulo e velocidade angular de cada partícula). A partir da derivação dos thetas e omegas a cada etapa é determinada a localização das partículas a cada momento (se baseando na altura e posição no eixo x em que elas estão).
