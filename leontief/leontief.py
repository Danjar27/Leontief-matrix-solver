import numpy as np
import pandas as pd
from IPython.core.display import display, HTML
pd.set_option("display.precision", 2)

def leontief(values,names,demand,new_demand):
    
    original = matriz(values,names,demand)
    coeficientes = pd.DataFrame(coef(matriz(values,names,demand)))
    final = matriz(adjust((coef(matriz(values,names,demand))),prod(coef(matriz(values,names,demand)), new_demand),new_demand),names,new_demand)
    
    def jupyter():
        try:
            shell = get_ipython().__class__.__name__
            if shell == 'ZMQInteractiveShell':
                return True 
            elif shell == 'TerminalInteractiveShell':
                return False
            else:
                return False
        except NameError:
            return False
    
    if(jupyter()):
        display(HTML('<h4>Matriz Original</h4>'))
        display(original)
        display(HTML('<h4>Matriz de coeficientes</h4>'))
        display(coeficientes)
        display(HTML('<h4>Matriz de resultado</h4>'))
        display(final)
    else:
        print("\nMatriz Original\n")
        display(original)
        print('\nMatriz de coeficientes\n')
        display(coeficientes)
        print('\nMatriz de resultado\n')
        display(final)
    
def matriz(values, names, dem): 
    
    df = pd.DataFrame(values, columns= names, index=names)
    df["Final"] = dem
    df["Bruta"] = df.sum(axis=1)
    return df

def coef(matriz):
    
    total = np.array(matriz['Bruta'])
    df = np.array(matriz.drop(columns=['Final', 'Bruta']))
    coef = []
    for i in range(len(df)):
        coef.append(np.transpose(df)[i]/total[i])
    return np.transpose(coef)

def prod(coef, v_dem):
    id =np.identity(len(coef))
    df = np.matmul(np.linalg.inv(id-coef),v_dem)
    return df

def adjust (coef, prod, dem):
    relative = 1-dem/prod
    weight = []
    df = []
    for i in range(len(dem)):
        weight.append(relative[i]*(coef[i]/np.transpose(coef).sum(axis=0)[i]))
    
    for i in  range(len(weight)):
        df.append(weight[i]*prod[i])
    
    return df



