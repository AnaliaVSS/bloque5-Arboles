class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def construir_arbol():
    return Nodo(1, Nodo(2, Nodo(4), Nodo(5)), Nodo(3, Nodo(6), Nodo(7)))

def postorden_y_maximo(nodo):
    if nodo is None:
        return float('-inf')
    
    max_izquierda = postorden_y_maximo(nodo.izquierda)
    max_derecha = postorden_y_maximo(nodo.derecha)
    return max(nodo.valor, max_izquierda, max_derecha)

# Ejemplo de uso
arbol = construir_arbol()
resultado = postorden_y_maximo(arbol)
print("Valor máximo encontrado en el árbol:", resultado)
