def bloque_condicional_if(blockName, condition):
    print(f"Bloque [{blockName}] comienza ejecución ---> if {condition}:")
    if eval(condition):
        print(f"La condición es TRUE")
        return True
    else:
        print(f"La condición es FALSE")
        return False
