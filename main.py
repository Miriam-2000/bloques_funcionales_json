def bloque_condicional_if(bloqueID, condition):
    print(f"Bloque {bloqueID} comienza ejecución")
    if eval(condition):
        print(f"La condición es TRUE")
        return True
    else:
        print(f"La condición es FALSE")
        return False
