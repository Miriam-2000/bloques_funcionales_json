def bloque_condicional_if(file, condition, TruePath, FalsePath):
    file = open(f"{file}", "a")
    file.write(f"if {condition}:\n")
    file.write(f"   return {TruePath}\n")
    file.write(f"else:\n")
    file.write(f"   return {FalsePath}\n")
    file.close()

file = open("sample.py", "w")
file.write("")
file.close()

bloque_condicional_if("sample.py", "1 == 2", "73137917", "839080139")