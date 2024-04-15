file = open("Downloads/bloques_funcionales_json-2/sample.py", "w")
file.write("def conditional_if_node(condition, TruePath, FalsePath):\n")
file = open("Downloads/bloques_funcionales_json-2/sample.py", "a")
file.write("   if condition:\n")
file.write("       return TruePath\n")
file.write("   else:\n")
file.write("       return FalsePath\n")
file.close()


def bloque_condicional_if(file, condition, TruePath, FalsePath):
    file = open(f"{file}", "a")
    file.write(f"\nconditional_if_node({condition}, {TruePath}, {FalsePath})\n")
    file.close()

