file = open("Downloads/bloques_funcionales_json-2/sample.py", "w")
file.write("def conditional_if_node(condition, TruePath, FalsePath):\n")
file = open("Downloads/bloques_funcionales_json-2/sample.py", "a")
file.write(f"    print('Ejecutando bloque conditional_if')\n")
file.write("    if condition:\n")
file.write(f"       print('Condición True')\n")
file.write("       return TruePath\n")
file.write("    else:\n")
file.write(f"       print('Condición False')\n")
file.write("       return FalsePath\n\n")
file.close()


def bloque_condicional_if(file, condition, TruePath, FalsePath):
    file = open(f"{file}", "a")
    file.write("\ntry:\n")
    file.write(f"   conditional_if_node({condition}, {TruePath}, {FalsePath})\n")
    file.write("except NameError:\n")
    file.write("    print('Una de las variables no existe')")
    file.close()

bloque_condicional_if("Downloads/bloques_funcionales_json-2/sample.py", "1 == 1", 1, 0)