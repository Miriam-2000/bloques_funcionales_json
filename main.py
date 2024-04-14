import json

with open("example_backend.json", "r") as archivo_json:
    data = json.load(archivo_json)


conexiones = []
i = 0
target = ["paco"]
condition = 0
while target != "":
    for node in data:
        # while target != []:
        if node["connectedTo"]["inputs"] == []:
            conexiones.append(node)
            target = node["connectedTo"]["outputs"][0]
            data.remove(node)
            print("PRIMER NODO ENCONTRADO: ", node["schemaId"])
            i += 1

        if target == node["id"]:
            conexiones.append(node)

            if node["schemaId"] == "conditional-if-node":
                if condition == 1:  # True
                    target = node["connectedTo"]["outputs"][0]
                    print("ENLAZADO CON: ", node["schemaId"], "; RAMA: ", node["outputs"][0]["outputId"])
                else:   # False
                    target = node["connectedTo"]["outputs"][1]
                    print("ENLAZADO CON: ", node["schemaId"], "; RAMA: ", node["outputs"][1]["outputId"])

            elif node["connectedTo"]["outputs"] != []:
                target = node["connectedTo"]["outputs"][0]
                print("ENLAZADO CON: ", node["schemaId"])
                i += 1
            else:
                target = ""
                print("ÚLTIMO NODO ENCONTRADO: ", node["schemaId"])

            data.remove(node)
# print(conexiones)
