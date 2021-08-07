#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Vamos a arrancar cargando los parametros iniciales que estimamos
Vmax = 30
Ks1 = 200
Ks2 = 100
Alpha = 0.5
Beta = 0.3


# In[5]:


import scipy.optimize as optimization  # Scipy: Necesitamos esta libreria para hacer el Metodo de Minimos Cuadrados
import numpy as np                     # Numpy: complementa a la anterior y nos deja usar matrices onda Matlab 
import csv                             # Esta nos deja usar archivos CSV

# Ahora vamos a agarrar el archivo que yo compile con tus datos que se llama 'data.csv' donde CSV es Comma Separated Values
# y lo vamos a convertir en tres matrices de numpy

A = []
B = []
V = []

with open('data.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    
    # Evitamos la primer linea (A, B, V)
    next(csv_reader)
    
    for row in csv_reader:
        A.append(float(row[0]))
        B.append(float(row[1]))
        V.append(float(row[2]))

# Convertimos los arrays de Python a arrays de Numpy optimizados
A = np.array(A)
B = np.array(B)
V = np.array(V)


# In[9]:


# Vamos a definir nuestra funcion a fittear

def f(var_indep, Vmax, Ks1, Ks2, Alpha, Beta):
    A, B = var_indep
    num = Vmax * ( (A/Ks1) + ( (Beta*A*B) / (Alpha*Ks1*Ks2) ) )
    denom = 1 + (A/Ks1) + (B/Ks2) +( (A*B) / (Alpha*Ks1*Ks2))
    return num/denom

start = np.array([Vmax, Ks1, Ks2, Alpha, Beta])

popt, pcov = optimization.curve_fit(f, (A, B), V, start)

std_dev = np.sqrt(np.diag(pcov))

print(f'Vmax:  {popt[0]} ± {std_dev[0]}')
print(f'Ks1:   {popt[1]} ± {std_dev[1]}')
print(f'Ks2:   {popt[2]} ± {std_dev[2]}')
print(f'Alpha: {popt[3]} ± {std_dev[3]}')
print(f'Beta:  {popt[4]} ± {std_dev[4]}')

residuals =  V - f((A, B), *popt)
RSS = np.sum(residuals**2)

print(f'RSS:   {RSS}')


# In[ ]:




