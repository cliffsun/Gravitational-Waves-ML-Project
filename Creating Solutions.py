import numpy as np
import sympy as sp
import pandas as pd
import scipy as spi

#Solutions are in the form of y = int(u(x) * g(x)) / (u(x)) where u(x) = exp(int(p(x)))

file_path_poly = r'CSV Files\symbolic_cubic_functions.csv'

df_poly = pd.read_csv(file_path_poly)

file_path_exp = r'CSV Files\symbolic_exp_functions.csv'

df_exp = pd.read_csv(file_path_exp)

file_path_sine = r'CSV Files\symbolic_sine_functions.csv'

df_sine = pd.read_csv(file_path_sine)

x = sp.symbols('x')

df_poly['result']= df_poly['result'].apply(sp.sympify)

df_sine['result']= df_sine['result'].apply(sp.sympify)

df_exp['result']= df_exp['result'].apply(sp.sympify)

x_values = np.linspace(-10, 10, 100)

def integrating_factor(function, xvalues):
    f_x = sp.lambdify(x, function, 'numpy')
    result = spi.cumtrapz(f_x(xvalues), xvalues, initial=xvalues[0])
    return np.exp(result)

def top_section(int_factor, g_of_x, xvalues):
    g_x = sp.lambdify(x, g_of_x, 'numpy')
    product_values = int_factor * g_x(xvalues)
    return spi.cumtrapz(product_values, xvalues, initial=xvalues[0])

def solution(tp_section, int_factor):
    result = []
    for tp, factor in zip(tp_section, int_factor):
        if factor == 0 or np.isinf(factor) or not np.isfinite(factor):
            result.append(None)
        else:
            result.append(tp / factor)
    
    return np.array(result)