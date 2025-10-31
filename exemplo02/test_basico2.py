def eh_positivo(numero):
    return numero > 0 

def teste_eh_positivo():
    assert eh_positivo(5) == True
    assert eh_positivo(-6) == False
    