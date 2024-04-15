def conditional_if_node(condition, TruePath, FalsePath):
    print('Ejecutando bloque conditional_if')
    if condition:
       print('Condición True')
       return TruePath
    else:
       print('Condición False')
       return FalsePath


try:
   conditional_if_node(rebaba.confidence<0.7, 1, 0)
except NameError:
    print('Una de las variables no existe')