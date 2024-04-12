import graphviz
import json

with open("example_backend.json", "r") as archivo_json:
    data = json.load(archivo_json)

dot = graphviz.Digraph()

# Añadir nodos
""" for node in data:
    dot.node(node["id"], label=node["schemaId"]) """

# Añadir conexiones
conexiones = []
target = ["paco"]

for node in data:
    # while target != []:
    if node["connectedTo"]["inputs"] == []:
        conexiones.append(node)
        target = node["connectedTo"]["outputs"]
        data.remove(node)
        print("EMPIEZO. Siguiente: ", target)
        node.clear()
        continue

    if target[0] == node["id"]:
        conexiones.append(node)
        target = node["connectedTo"]["outputs"]
        print("TRIGGER LANZADO:", target)
        node.clear()
        continue
            
    
                
    
        
                    # conexiones.append(target)

# Renderizar el gráfico
# dot.render('diagrama_de_bloques', format='png', cleanup=True)

#print(conexiones)
