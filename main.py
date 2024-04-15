import json

with open("example_backend.json", "r") as archivo_json:
    data = json.load(archivo_json)

def end_cycle(data):
    for node in data:
        if node["schemaId"] == "end-cycle-node":
            schema_id = node["schemaId"]
            inputs = node["inputs"]
            outputs = node["outputs"]
            print("Buscando el nodo...")
            print("El siguiente nodo es", schema_id)
            print("\tInputs:")
            for inp in inputs:
                input_id = inp["inputId"]
                # type = inp["type"]
                # value = inp["value"]
                print("\t\tInput Id:", input_id)
            print("\tOutputs:")
            if not outputs:
                print("\t\tNo hay más nodos, es el final del ciclo.")
            else:
                for out in outputs:
                    print("\tOutput Id:", out["outputId"])
    print("Saliendo del nodo..")
end_cycle(data)
