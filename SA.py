# Import ulang pustaka yang diperlukan setelah reset
import numpy as np
import matplotlib.pyplot as plt

# Fungsi baru yang lebih kompleks: Sinusoidal dengan banyak lokal optima
def complex_objective_function(x):
    return np.sin(5 * x) * (1 - np.tanh(x ** 2)) + np.cos(3 * x)

# Simulated Annealing Algorithm untuk fungsi baru
def simulated_annealing_complex(start_x, step_size=0.9, max_iterations=100, initial_temp=5, cooling_rate=0.78):
    x = start_x
    temp = initial_temp
    history = [x]
    
    for y in range(max_iterations):
        new_x = x + np.random.uniform(-step_size, step_size)
        # print(y,new_x,x)
        delta_E = complex_objective_function(new_x) - complex_objective_function(x)
        
        print(complex_objective_function(new_x),complex_objective_function(x),np.exp(delta_E / temp))
        if delta_E > 0 or np.random.rand() < np.exp(delta_E / temp):  # Bisa menerima solusi lebih buruk
            x = new_x
        
        history.append(x)
        temp *= cooling_rate  # Menurunkan temperatur
    
    return x, history

# Simulasi dengan fungsi baru
np.random.seed(42)
start_x = np.random.uniform(-3, 3)  # Memilih titik awal secara acak

# Jalankan Simulated Annealing dengan fungsi baru
sa_solution_complex, sa_history_complex = simulated_annealing_complex(-2.5)

# Visualisasi
x_range = np.linspace(-3, 3, 200)
y_range = complex_objective_function(x_range)

plt.figure(figsize=(8, 5))
plt.plot(x_range, y_range, label="Objective Function", color="gray")
plt.scatter(sa_history_complex, [complex_objective_function(x) for x in sa_history_complex], 
            c='green', label="Search Path", alpha=0.6)
plt.scatter(sa_solution_complex, complex_objective_function(sa_solution_complex), 
            c='red', marker='X', s=100, label="Final Solution")
plt.title("Simulated Annealing on Complex Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
