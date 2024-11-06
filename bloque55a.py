class Nodo:
    def __init__(self, valor, izquierda=None, derecha=None):
        self.valor = valor
        self.izquierda = izquierda
        self.derecha = derecha

def construir_arbol_expresion(expresion):
    def es_operador(c):
        return c in "+-*/"

    def precedencia(c):
        if c in "*/":
            return 2
        elif c in "+-":
            return 1
        return 0

    def a_postfijo(expresion):
        salida = []
        operadores = []
        for c in expresion:
            if c.isdigit():
                salida.append(c)
            elif es_operador(c):
                while operadores and precedencia(operadores[-1]) >= precedencia(c):
                    salida.append(operadores.pop())
                operadores.append(c)
        while operadores:
            salida.append(operadores.pop())
        return salida

    def construir_desde_postfijo(postfijo):
        pila = []
        for token in postfijo:
            if token.isdigit():
                pila.append(Nodo(int(token)))
            else:
                nodo_derecho = pila.pop()
                nodo_izquierdo = pila.pop()
                nuevo_nodo = Nodo(token, nodo_izquierdo, nodo_derecho)
                pila.append(nuevo_nodo)
        return pila[0]

    expresion = expresion.replace(" ", "")
    postfijo = a_postfijo(expresion)
    return construir_desde_postfijo(postfijo)

def evaluar_arbol(nodo):
    if isinstance(nodo.valor, int):
        return nodo.valor
    izquierda = evaluar_arbol(nodo.izquierda)
    derecha = evaluar_arbol(nodo.derecha)
    if nodo.valor == '+':
        return izquierda + derecha
    elif nodo.valor == '-':
        return izquierda - derecha
    elif nodo.valor == '*':
        return izquierda * derecha
    elif nodo.valor == '/':
        return izquierda / derecha

# Ejemplo de uso
expresion = "5 + 3 * 4"
arbol_expresion = construir_arbol_expresion(expresion)
resultado = evaluar_arbol(arbol_expresion)
print("Resultado de la expresión:", resultado)

