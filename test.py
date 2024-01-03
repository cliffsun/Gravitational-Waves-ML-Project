import scipy.integrate as spi
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


x = sp.symbols('x')

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

p_x = sp.sin(x)
g_x = sp.exp(2*x)
int_factor_values = integrating_factor(p_x, x_values)
tp_section_values = top_section(int_factor_values, g_x, x_values)

result = solution(tp_section_values, int_factor_values)

print(result)

plt.plot(x_values, result, label='Solution')
plt.title('Solution')
plt.xlabel('x')
plt.ylabel('Value')
plt.legend()
plt.show()