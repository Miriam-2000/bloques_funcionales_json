import json
with open("example_backend.json", "r") as archivo_json:
    data = json.load(archivo_json)


def mostrar_nodos_plc_write(data):
    nodos_plc_write = []
    for nodo in data:
        if nodo.get("schemaId") == "plc-write-node":
            nodo_plc_write = {
                "schemaId": nodo.get("schemaId"),
                "inputs": nodo.get("inputs"),
                "outputs": nodo.get("outputs")
            }
            nodos_plc_write.append(nodo_plc_write)
    return nodos_plc_write
nodos_plc_write = mostrar_nodos_plc_write(data)

# Mostrar los resultados
for nodo in nodos_plc_write:
    print("schemaId:", nodo["schemaId"])
    print("inputs:")
    for input_data in nodo["inputs"]:
        print("  inputId:", input_data["inputId"])
        print("  type:", input_data["type"])
        print("  value:", input_data["value"])
    print("outputs:")
    for output_data in nodo["outputs"]:
        print("  outputId:", output_data["outputId"])
        print("  type:", output_data["type"])
        print("  value:", output_data["value"])
    print()