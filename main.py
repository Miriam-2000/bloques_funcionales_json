import json

with open("example_backend.json", "r") as archivo_json:
    data = json.load(archivo_json)


for node in data:
    if node["schemaId"] == "end-cycle-node":
        schema_id = node["schemaId"]
        inputs = node["inputs"]
        outputs = node["outputs"]
        print("Nodo:", schema_id)
        print("Inputs:")
        for inp in inputs:
            print("\tInput Id:", inp["inputId"], "| Pertenece a:", node["schemaId"])
        print("Outputs:")
        if not outputs:
            print("\tNo hay más nodos, es el final del ciclo.")
        else:
            for out in outputs:
                print("\tOutput Id:", out["outputId"], "| Pertenece a schemaId:", node["id"])
        break 