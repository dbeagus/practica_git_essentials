import sympy as sp #Usado para simbolos, derivadas y manejo de funciones
e = sp.Symbol("e")
x = sp.Symbol("x")
y = sp.Symbol("y")

# Definir la función que se desea aproximar
def funcion1(x, y):
    return e**(-x**2-y**2)

def funcion2(x,y):
    return x*e**y

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
    def aproximar(self, funcion, grado, x0, y0):
        aproximacion = funcion(x0,y0)
        
        #derivadas mediante el uso de sp.diff
        df_dx = sp.diff(self.funcion, self.x).subs(self.x, x)
        df_dy = sp.diff(self.funcion, self.y).subs(self.y, y)
        
        for i in range(1, grado+1):
            aproximacion +=  (df_dx * (self.x - x0) + df_dy * (self.y - y0)) / sp.factorial(i)
        
        return aproximacion

#Prueba del codigo
print("- Aproximacion de funciones multivariables -\n".center(75))

#Analisis para la primer funcion
print(f"*- Se aproximara la funcion ' {str(funcion1(x,y))} ' en el punto (0,0): ")
funcion_act1 = sp.sympify(funcion1(x,y)) #Se utiliza sympify para que la libreria trabaje respetando variables
aproximacion1 = AproximacionTaylor(funcion_act1)

#Evaluo las aproximaciones de grado 1, 2 y 3 en el punnto (0,0)
funcion1_eval1 = aproximacion1.aproximar(funcion1, 1, 0, 0)
funcion1_eval2 = aproximacion1.aproximar(funcion1, 2, 0, 0)
funcion1_eval3 = aproximacion1.aproximar(funcion1, 3, 0, 0)

#Muestro en pantalla
print(f"Aproximacion de grado 1: {funcion1_eval1}")
print(f"Aproximacion de grado 2: {funcion1_eval2}")
print(f"Aproximacion de grado 3: {funcion1_eval3}")

#Analisis para la segunda funcion
print(f"\n*- Se aproximara la funcion ' {str(funcion2(x,y))} ' en el punto (1,0): ")
funcion_act2 = sp.sympify(funcion2(x,y)) #Se utiliza sympify para que la libreria trabaje respetando variables
aproximacion2 = AproximacionTaylor(funcion_act2)

#Evaluo las aproximaciones de grado 1, 2 y 3 en el punnto (0,0)
funcion2_eval1 = aproximacion2.aproximar(funcion2, 1, 1, 0)
funcion2_eval2 = aproximacion2.aproximar(funcion2, 2, 1, 0)
funcion2_eval3 = aproximacion2.aproximar(funcion2, 3, 1, 0)

#Muestro en pantalla
print(f"Aproximacion de grado 1: {funcion2_eval1}")
print(f"Aproximacion de grado 2: {funcion2_eval2}")
print(f"Aproximacion de grado 3: {funcion2_eval3}")