import json
from diagrams import Diagram, Cluster, Node


class DiagramNode:
    """Representa un nodo en el flujograma
    """
    def __init__(self, id, schemaId, connectedTo, inputs, outputs):
        """Inicializa un objetos DiagramNode que contiene los datos de un nodo

        Args:
            id (str): Identificación del nodo.
            schemaId (str): Nombre del nodo.
            connectedTo (_type_): Conexiones del nodo con otros.
        """
        self.id = id
        self.schemaId = schemaId
        self.connectedTo = connectedTo
        self.inputs = inputs
        self.outputs = outputs



def cargar_datos(data):
    """Genera una lista que contiene las instancias de cada objeto (nodo)

    Args:
        data (List): Lista de diccionarios que contiene los datos

    Returns:
        list: Lista con los nodos (objetos)
    """
    nodos = []
    for item in data:
        nodo = DiagramNode(item['id'],
                        item['schemaId'],
                        item.get('connectedTo', {'inputs': [], 'outputs': []}), 
                        item['inputs'],
                        item['outputs'])


        nodos.append(nodo)
    return nodos


def crear_diagrama(nodos):
    """Crea el flujograma a partir de los nodos y sus respectivas conexiones

    Args:
        nodos (List): Lista con los nodos (objetos)
    """
    # Inicializa un nuevo diagrama (Diagram)
    with Diagram("Flujograma", show=False):
        # Agrupa todos los nodos relacionados (Cluster), en este caso todos
        with Cluster("Nodos"):
            # Se crean los nodos (Node) --> (Node = ID + Nombre)
            nodes = {nodo.id: Node(nodo.schemaId) for nodo in nodos}
            # Crea las conexiones comparando las salidas con el ID del nodo
            for nodo in nodos:
                for conexion in nodo.connectedTo['outputs']:
                    if conexion in nodes:
                        nodes[nodo.id] >> nodes[conexion]

def ia(input_id, nodos):
    nodo_seleccionado = None
    for nodo in nodos:
        if nodo.id == input_id:
            nodo_seleccionado = nodo
            break

    nodo_ia = None
    for nodo in nodos:
        if nodo.schemaId == "ai-node":
            nodo_ia = nodo
            break
    if nodo_ia is not None:
        print("Nombre del nodo ", nodo_ia.schemaId)
        print("He accedido a la IA ", nodo_ia.id)
    else:
        print("No he podido acceder al nodo IA")

    if nodo_seleccionado is not None:
        print("Inputs del nodo", nodo_seleccionado.schemaId + ":")
        for input_item in nodo_seleccionado.inputs:
            print("inputId:", input_item['inputId'], " type:", input_item['type']," value:", input_item['value'])
        print("Outputs del nodo", nodo_seleccionado.schemaId + ":")
        for output_item in nodo_seleccionado.outputs:
            print("outputId:", output_item['outputId']," type:", output_item['type']," value:", output_item['value'])
    else:
        print("No se encontró ningún nodo con el ID proporcionado.")

def main():
    with open("example_backend.json", "r") as file:
        data = json.load(file)
        nodos = cargar_datos(data)
    return nodos

nodos = main()
input_id = input("Ingrese el ID del nodo: ")
ia(input_id, nodos)



