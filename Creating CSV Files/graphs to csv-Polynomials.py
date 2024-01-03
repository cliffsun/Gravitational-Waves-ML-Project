import sympy as sp
import pandas as pd
import numpy as np

# Define symbolic variables
x = sp.symbols('x')
a1, a2, a3, a4 = sp.symbols('a1 a2 a3 a4')

# Define the cubic function symbolically
cubic_function = a1 * x**3 + a2 * x**2 + a3 * x + a4

# Generate a range of coefficients a1, a2, a3, a4
coefficients_range = range(-10, 11)

flat_data = []
for a1_val in coefficients_range:
    for a2_val in coefficients_range:
        for a3_val in coefficients_range:
            for a4_val in coefficients_range:
                result = cubic_function.subs({a1: a1_val, a2: a2_val, a3: a3_val, a4: a4_val})
                flat_data.append([a1_val, a2_val, a3_val, a4_val, result])

# Create a DataFrame
columns = ['a1', 'a2', 'a3', 'a4', 'result']
df = pd.DataFrame(flat_data, columns=columns)

# Save DataFrame to CSV
file_path = 'C:/Users/cliff/Downloads/Projects/symbolic_cubic_functions.csv'
df.to_csv(file_path, index=False)
