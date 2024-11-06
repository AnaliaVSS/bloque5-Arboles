class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def insertar(nodo, valor):
    if nodo is None:
        return Nodo(valor)
    if valor < nodo.valor:
        nodo.izquierda = insertar(nodo.izquierda, valor)
    else:
        nodo.derecha = insertar(nodo.derecha, valor)
    return nodo

def buscar(nodo, valor):
    if nodo is None:
        return False
    if valor == nodo.valor:
        return True
    elif valor < nodo.valor:
        return buscar(nodo.izquierda, valor)
    else:
        return buscar(nodo.derecha, valor)

# Ejemplo de uso
valores = [20, 10, 30, 5, 15, 25, 35]
raiz = None

for valor in valores:
    raiz = insertar(raiz, valor)

# Buscar valores en el árbol
numero_a_buscar = 15
existe = buscar(raiz, numero_a_buscar)
print(f"El número {numero_a_buscar} {'existe' if existe else 'no existe'} en el árbol.")

numero_a_buscar = 40
existe = buscar(raiz, numero_a_buscar)
print(f"El número {numero_a_buscar} {'existe' if existe else 'no existe'} en el árbol.")
