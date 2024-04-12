def bloque_condicional_if(blockName, condition, TruePath, FalsePath):
    print(f"Bloque [{blockName}] comienza ejecución ---> if {condition}:")
    if eval(condition):
        print(f"La condición es TRUE")
        return TruePath
    else:
        print(f"La condición es FALSE")
        return FalsePath
