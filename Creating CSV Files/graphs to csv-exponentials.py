import sympy as sp
import pandas as pd
import numpy as np

# Define symbolic variables
x = sp.symbols('x')
a1, a2, a3, a4 = sp.symbols('a1 a2 a3 a4')

# Define the cubic function symbolically
exp_function = a1 * sp.exp(a2 * x)+ a3 * sp.exp(a4 * x)

# Generate a range of coefficients a1, a2, a3, a4
coefficients_range = range(-10, 11)

flat_data = []
for a1_val in coefficients_range:
    for a2_val in coefficients_range:
        for a3_val in coefficients_range:
            for a4_val in coefficients_range:
                result = exp_function.subs({a1: a1_val, a2: a2_val, a3: a3_val, a4: a4_val})
                flat_data.append([a1_val, a2_val, a3_val, a4_val, result])

# Create a DataFrame
columns = ['a1', 'a2', 'a3', 'a4', 'result']
df = pd.DataFrame(flat_data, columns=columns)

# Save DataFrame to CSV
file_path = 'C:/Users/cliff/Downloads/Projects/symbolic_exp_functions.csv'
df.to_csv(file_path, index=False)