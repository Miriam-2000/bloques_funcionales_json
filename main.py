file = open(f"sample.py", "a")
file.write("def conditional_if_node(file, condition, TruePath, FalsePath):\n")
file.write("   if condition:\n")
file.write("       return TruePath\n")
file.write("   else:\n")
file.write("       return FalsePath\n")
file.close()


def bloque_condicional_if(file, condition, TruePath, FalsePath):
    file = open(f"{file}", "a")
    file.write(f"conditional_if_node({file}, {condition}, {TruePath}, {FalsePath})\n")
    file.close()

file = open("sample.py", "w")
file.write("")
file.close()

bloque_condicional_if("sample.py", "1 == 2", "73137917", "839080139")