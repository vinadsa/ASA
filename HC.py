import numpy as np
import matplotlib.pyplot as plt
# Hill Climbing Algorithm untuk fungsi kompleks

# Fungsi baru yang lebih kompleks: Sinusoidal dengan banyak lokal optima
def complex_objective_function(x):
    return np.sin(5 * x) * (1 - np.tanh(x ** 2)) + np.cos(3 * x)

def hill_climbing_complex(start_x, step_size=0.7, max_iterations=10000):
    x = start_x
    history = [x]
    
    for _ in range(max_iterations):
        new_x = x + np.random.uniform(-step_size, step_size)
        if complex_objective_function(new_x) > complex_objective_function(x):  # Hanya menerima solusi yang lebih baik
            x = new_x
        
        history.append(x)
    
    return x, history

# Simulasi dengan fungsi kompleks
np.random.seed(42)
start_x = np.random.uniform(-3,3 )  # Memilih titik awal secara acak

# Jalankan Hill Climbing dengan fungsi baru
hc_solution_complex, hc_history_complex = hill_climbing_complex(-2.5)

# Visualisasi
x_range = np.linspace(-3, 3, 200)
y_range = complex_objective_function(x_range)

plt.figure(figsize=(8, 5))
plt.plot(x_range, y_range, label="Objective Function", color="gray")
plt.scatter(hc_history_complex, [complex_objective_function(x) for x in hc_history_complex], 
            c='blue', label="Search Path", alpha=0.6)
plt.scatter(hc_solution_complex, complex_objective_function(hc_solution_complex), 
            c='red', marker='X', s=100, label="Final Solution")
plt.title("Hill Climbing on Complex Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
