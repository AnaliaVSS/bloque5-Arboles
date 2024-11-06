class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def construir_arbol():
    return Nodo(1, Nodo(2, Nodo(4), Nodo(5)), Nodo(3, Nodo(6), Nodo(7)))

def preorden(nodo):
    if nodo:
        print(nodo.valor, end=' ')
        preorden(nodo.izquierda)
        preorden(nodo.derecha)

# Ejemplo de uso
arbol = construir_arbol()
print("Recorrido en preorden:")
preorden(arbol)

