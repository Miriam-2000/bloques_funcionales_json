import json

with open("example_backend.json", "r") as archivo_json:
    data = json.load(archivo_json)



start_node = None
for node in data:
    if node["schemaId"] == "start-cycle-node":
        start_node = node
        break

# Función para realizar una búsqueda en profundidad (DFS)
def dfs(node, visited):
    visited.add(node["id"])
    print("Visitando nodo:", node["schemaId"])
    print("Inputs:")
    for inp in node["inputs"]:
        print("\tInput Id:", inp["inputId"])
    print("Outputs:")
    for output_id in node["connectedTo"]["outputs"]:
        next_node = next((n for n in data if n["id"] == output_id), None)
        if next_node:
            print("\tOutput Id:", output_id)
            dfs(next_node, visited)

# Realizar la búsqueda en profundidad desde el nodo de inicio (start_cycle)
if start_node:
    print("Comenzando ciclo:")
    visited_nodes = set()
    dfs(start_node, visited_nodes)
    print("Fin del ciclo.")
else:
     print("No se encontró el nodo de inicio (start_cycle).")
