import json


class DiagramNode:
    """Clase base que representa un nodo en el diagrama"""
    def __init__(self, id, schemaId, inputs, outputs, nodeType, connectedTo):
        """Inicializa un objeto DiagramNode que contiene los datos de un nodo"""
        self.id = id
        self.schemaId = schemaId
        self.inputs = inputs
        self.outputs = outputs
        self.nodeType = nodeType
        self.connectedTo = connectedTo

    def generate_code(self, nodes_dict, tab_level=1):
        """Genera el código Python correspondiente al nodo"""
        return ""


# Clase para el nodo de inicio de ciclo
class StartCycleNode(DiagramNode):
    def generate_code(self, nodes_dict, tab_level=1):
        return "while True:\n"


# Clase para el nodo de fin de ciclo
class EndCycleNode(DiagramNode):
    def generate_code(self, nodes_dict, tab_level=1):
        return "\t\tbreak\n"


# Clase para el nodo de disparador
class TriggerNode(DiagramNode):
    def generate_code(self, nodes_dict, tab_level=1):
        indent = "\t" * tab_level
        code = f"{indent}while True:\n"
        code += f"{indent}\t# Esperar hasta que se reciba una señal verdadera del PLC\n"
        code += f"{indent}\tif {self.inputs[0]['value']}:\n"
        code += f"{indent}\t\tbreak\n"
        return code


# Clase para el nodo de cámara
class CameraNode(DiagramNode):
    def generate_code(self, nodes_dict, tab_level=1):
        camera_name = self.inputs[0]["value"]
        output_image_name = self.outputs[0]["value"]
        indent = "\t" * tab_level
        code = f"{indent}# Capturar imagen de la cámara {camera_name} y guardarla como {output_image_name}\n"
        return code


# Clase para el nodo de IA
class AINode(DiagramNode):
    def generate_code(self, nodes_dict, tab_level=1):
        model_name = self.inputs[0]["value"]
        model_image_name = self.inputs[1]["value"]
        indent = "\t" * tab_level
        code = f"{indent}# Ejecutar el modelo de IA con el nombre {model_name} y la imagen {model_image_name}\n"
        # Aquí iría el código real para ejecutar el modelo de IA, pero aún no está disponible
        return code


# Clase para el nodo de escritura de PLC
class PLCWriteNode(DiagramNode):
    def generate_code(self, nodes_dict, tab_level=1):
        plc_name = self.inputs[0]["value"]
        signal = self.inputs[1]["value"]
        indent = "\t" * tab_level
        return f"{indent}# Escribir en el PLC {plc_name} la señal {signal}\n"


# Clase para el nodo condicional
class ConditionalIfNode(DiagramNode):
    if_execution_count = 0  # Variable de clase para contar la ejecución del nodo 'if'
    executed_conditions = set()  # Conjunto para almacenar los IDs de los nodos condicionales ejecutados

    def has_nested_conditionals(self, nodes_dict):
        """Verifica si hay condicionales anidados en las salidas del nodo"""
        outputs = self.connectedTo["outputs"]
        for output_id in outputs:
            output_node = nodes_dict.get(output_id)
            if output_node and output_node.schemaId == "conditional-if-node":
                return True
        return False

    def generate_code(self, nodes_dict, tab_level=1):
        indent = "\t" * tab_level
        condition = self.inputs[0]["value"]
        true_path = self.connectedTo["outputs"][0]
        false_path = self.connectedTo["outputs"][1]
        true_node_code = ""
        false_node_code = ""

        # Verificar si hay datos disponibles en el nodo verdadero
        if true_path:
            true_node = nodes_dict.get(true_path)
            if true_node:
                true_node_code = true_node.generate_code(nodes_dict, tab_level + 1)

        # Verificar si hay datos disponibles en el nodo falso y no hay condicionales anidados
        if false_path:
            false_node = nodes_dict.get(false_path)
            if false_node and not self.has_nested_conditionals(nodes_dict):
                false_node_code = false_node.generate_code(nodes_dict, tab_level + 1)

        # Construir la estructura condicional
        code = f"{indent}if {condition}:\n{true_node_code}\t\t\tpass\n"
        if false_node_code:
            code += f"{indent}else:\n{false_node_code}"

        return code


# Diccionario que mapea el schemaId a la clase correspondiente
node_type_classes = {
    "start-cycle-node": StartCycleNode,
    "end-cycle-node": EndCycleNode,
    "trigger-node": TriggerNode,
    "camera-node": CameraNode,
    "ai-node": AINode,
    "plc-write-node": PLCWriteNode,
    "conditional-if-node": ConditionalIfNode,
}


def load_data(data):
    """Genera una lista que contiene las instancias de cada objeto (nodo)"""
    return [node_type_classes[item['schemaId']](**item) for item in data]


def execute_nodes_in_order(nodes, start_node_id):
    """Ejecuta los nodos en orden a partir del nodo inicial"""
    nodes_dict = {node.id: node for node in nodes}
    current_node = nodes_dict[start_node_id]
    visited_nodes = set()  # Conjunto para almacenar los IDs de los nodos visitados
    code = ""

    while current_node:
        print(f"Ejecutando nodo: {current_node.schemaId}")
        if current_node.id in visited_nodes:
            break  # Si el nodo ya ha sido visitado, salimos del ciclo para evitar bucles infinitos

        code += current_node.generate_code(nodes_dict)

        visited_nodes.add(current_node.id)

        if current_node.nodeType == "end-cycle-node":
            break

        # Si el nodo actual es condicional, se recorren todas las ramas
        if current_node.schemaId == "conditional-if-node":
            true_path = current_node.connectedTo["outputs"][0]
            false_path = current_node.connectedTo["outputs"][1]
            print(f"True path: {true_path}")
            print(f"False path: {false_path}")

        # Si el nodo actual tiene salidas, se avanza al siguiente nodo según la primera salida
        elif current_node.connectedTo["outputs"]:
            next_node_id = current_node.connectedTo["outputs"][0]
            current_node = nodes_dict.get(next_node_id, None)

        else:
            # Si no tiene salidas, finalizamos el ciclo
            break

    return code


def main():
    path = "example_backend.json"
    with open(path, "r") as file:
        data = json.load(file)

    nodes = load_data(data)
    start_node_id = next((node.id for node in nodes if node.schemaId == "start-cycle-node"), None)

    if start_node_id:
        code = execute_nodes_in_order(nodes, start_node_id)
        with open("output.py", "w") as file:
            file.write(code)
    else:
        print("No se encontró el nodo inicial del flujo.")


if __name__ == "__main__":
    main()
    print(f"El nodo 'if' se ejecutó {ConditionalIfNode.if_execution_count} veces.")
