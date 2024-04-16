import json
from diagrams import Diagram, Cluster, Node


class DiagramNode:
    """Representa un nodo en el flujograma
    """
    def __init__(self, id, schemaId, connectedTo):
        """Inicializa un objetos DiagramNode que contiene los datos de un nodo

        Args:
            id (str): Identificación del nodo.
            schemaId (str): Nombre del nodo.
            connectedTo (_type_): Conexiones del nodo con otros.
        """
        self.id = id
        self.schemaId = schemaId
        self.connectedTo = connectedTo


def cargar_datos(data):
    """Genera una lista que contiene las instacias de cada objeto (nodo)

    Args:
        data (List): Lista de diccionarios que contiene los datos

    Returns:
        list: Lista con los nodos (objetos)
    """
    nodos = []
    for item in data:
        nodo = DiagramNode(item['id'],
                           item['schemaId'],
                           item.get('connectedTo', {'inputs': [],
                                                    'outputs': []}))
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


def plc_read(data):
    """Extracts and prints inputs and outputs from PLC nodes.

    Args:
        data (list): List of dictionaries containing node data.
    """
    print("PLC Nodes Inputs and Outputs:")
    for node in data:
        if node['schemaId'] == 'plc-write-node':
            inputs = node.get('inputs', [])
            outputs = node.get('outputs', [])
            print(f"Node ID: {node['id']}")
            print("Inputs:")
            for inp in inputs:
                print(f"  Input ID: {inp['inputId']}")
                print(f"  Type: {inp['type']}")
                print(f"  Value: {inp['value']}")
            if outputs:
                print("Outputs:")
                for out in outputs:
                    print(f"  Output ID: {out['outputId']}")
                    print(f"  Type: {out['type']}")
                    print(f"  Value: {out['value']}")
            else:
                print("Outputs: None")
            print()


def main():
    ruta = "example_backend.json"
    with open(ruta, "r") as file:
        data = json.load(file)

    plc_read(data)


if __name__ == "__main__":
    main()
