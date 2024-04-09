import numpy as np
import matplotlib.pyplot as plt
prey_population = float(input("Enter initial prey population: "))
predator_population = float(input("Enter initial predator population: "))
alpha = 0.1
beta = 0.02
gamma = 0.3
delta = 0.01
t_start = 0
t_end = 200
dt = 0.1
num_steps = int((t_end - t_start) / dt)
prey_population_values = np.zeros(num_steps)
predator_population_values = np.zeros(num_steps)
time_values = np.zeros(num_steps)
for i in range(num_steps):
prey_population_dot = alpha * prey_population - beta * prey_population *
predator_population
predator_population_dot = delta * prey_population * predator_population - gamma *
predator_population
prey_population += prey_population_dot * dt
predator_population += predator_population_dot * dt
prey_population_values[i] = prey_population
predator_population_values[i] = predator_population
time_values[i] = t_start + i * dt
t_start += dt
plt.figure(figsize=(10, 6))
plt.plot(time_values, prey_population_values, label='Prey')
plt.plot(time_values, predator_population_values, label='Predator')
plt.xlabel('Time')
plt.ylabel('Population')
plt.title('Predator-Prey Dynamics')
plt.legend()
plt.grid(True)
plt.show()