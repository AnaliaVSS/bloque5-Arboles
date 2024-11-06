class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def construir_arbol():
    return Nodo(1, Nodo(2, Nodo(4), Nodo(5)), Nodo(3, Nodo(6), Nodo(7)))

def inorden_y_suma(nodo):
    if nodo is None:
        return 0
    return inorden_y_suma(nodo.izquierda) + nodo.valor + inorden_y_suma(nodo.derecha)

# Ejemplo de uso
arbol = construir_arbol()
resultado = inorden_y_suma(arbol)
print("Suma de los valores de los nodos:", resultado)