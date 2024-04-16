import json
import time

class block():
    
    flag = False

    def __init__(self, ID, schemaId, inputs, outputs, connections):
        self.id = ID
        self.name = schemaId
        self.inputs = inputs
        self.outputs = outputs
        self.connectionsIn = connections["inputs"]
        self.connectionsOut = connections["outputs"]
        if self.name == "conditional-if-node":
            self.used_ways = 0

    def __str__(self):
        if self.name == "conditional-if-node":
            return (f" Ejecutando Nodo: {self.name} [{self.id}]")
        return (f"Ejecutando Nodo: {self.name} [{self.id}]")

    def ejecutar(self, funcion):
        funcion

def leer_json(ruta):
    with open(ruta, 'r') as archivo:
        datos = json.load(archivo)
    return datos

def node_jump(lista_nodos, nodo_actual):
    if nodo_actual.name == "end-cycle-node":
        nodos_destino = [nodo_actual]
    elif nodo_actual.name != "conditional-if-node":
        nodos_destino = [nodo for nodo in lista_nodos if nodo_actual.connectionsOut[0] == nodo.id]
    elif nodo_actual.name == "conditional-if-node":
        nodos_destino = [nodo for nodo in lista_nodos if nodo_actual.connectionsOut[0] == nodo.id]   
        nodo_actual.connectionsOut.reverse()
        nodo_actual.used_ways += 1
    return nodos_destino[0]

def flag_check(lista_nodos):
    for nodo in lista_nodos:
        if nodo.flag == False:
            return False
    return True

def flag_node(nodo):
    if nodo.name != "conditional-if-node":
        nodo.flag = True
    else:
        if nodo.used_ways >= 2:
            nodo.flag = True

def imprimir_nodo(nodo):
    print(f"\n{nodo}\n")
# --------------------------------------------------------------------------------------------------

file = leer_json("Downloads/bloques_funcionales_json-2/example_backend.json")
lista_nodos = []

for bloque in file:
    nodo = block(bloque["id"], bloque["schemaId"], bloque["inputs"], bloque["outputs"], bloque["connectedTo"])
    lista_nodos.append(nodo)

for nodo in lista_nodos:
    if nodo.name == "start-cycle-node":
        nodo_actual = nodo

nodo_actual.flag = True
print(f"\n{nodo_actual}\n")

while flag_check(lista_nodos) == False:
    if nodo_actual.name == "end-cycle-node":
        for nodo in lista_nodos:
            if nodo.name == "start-cycle-node":
                nodo_actual = nodo
    nodo_actual = node_jump(lista_nodos , nodo_actual)
    if nodo_actual.flag == False:
        flag_node(nodo_actual)
        nodo_actual.ejecutar(imprimir_nodo(nodo_actual))
print("----------------------------FIN-------------------------")