import sympy as sp #Usado para simbolos, derivadas y manejo de funciones
e = sp.Symbol("e")
x = sp.Symbol("x")
y = sp.Symbol("y")

# Definir la función que se desea aproximar
def funcion(x, y):
    return e**(-x**2-y**2)

#Aproximacion por serie de Taylor
class AproximacionTaylor:
    def __init__(self, funcion):
        self.funcion = funcion
        self.x = x
        self.y = y

    #Metodo para ver la funcion que se esta evaluando
    def ver(self):
        return str(self.funcion)
    
    #Metodo para aproximar la funcion en un punto
    def aproximar(self, grado, x0, y0):
        aproximacion = funcion(x0,y0)
        
        #derivadas mediante el uso de sp.diff
        df_dx = sp.diff(self.funcion, self.x).subs(self.x, x)
        df_dy = sp.diff(self.funcion, self.y).subs(self.y, y)
        
        for i in range(1, grado+1):
            aproximacion +=  (df_dx * (self.x - x0) + df_dy * (self.y - y0)) / sp.factorial(i)
        
        return aproximacion