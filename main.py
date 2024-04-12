import json

with open("example_backend.json", "r") as archivo_json:
    data = json.load(archivo_json)


conexiones = []
i = 0
mensajes = ["Empiezo", "trigger", "cámara", "ia","conditional","conditional","plc_write","end_cycle"]
target = ["paco"]
while target != "":
    for node in data:
        # while target != []:
        if node["connectedTo"]["inputs"] == []:
            conexiones.append(node)
            target = node["connectedTo"]["outputs"][0]
            data.remove(node)
            print("PRIMER NODO ENCONTRADO: ",node["schemaId"]) 
            i +=1                

        if target == node["id"]:
            conexiones.append(node)
            if node["connectedTo"]["outputs"] != [] :
                target = node["connectedTo"]["outputs"][0]
                print("ENLAZADO CON: ", node["schemaId"])
                i +=1 
            else:
                target=""
                print("ÚLTIMO NODO ENCONTRADO: ",node["schemaId"])
            
            data.remove(node)
# print(conexiones)
