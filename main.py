def bloque_condicional_if(bloqueName, condition):
    print(f"Bloque [{bloqueName}] comienza ejecución ---> if {condition}:")
    if eval(condition):
        print(f"La condición es TRUE")
        return True
    else:
        print(f"La condición es FALSE")
        return False

bloque_condicional_if("conditional_if_node", "1 == 2")