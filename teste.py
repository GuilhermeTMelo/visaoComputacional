import math

#Comparar Vetores de Pontos

def comparador(vetorA, vetorB, raio_threshold=3):
    vetorAux = []

    #comparação A com B
    for A in vetorA:
        ponto_valido = False
        for B in vetorB:
            distancia = math.sqrt((A[0] - B[0])**2 + (A[1] - B[1])**2)
            if distancia < raio_threshold:
                ponto_valido = True
                break
        if ponto_valido:
            vetorAux.append(A)

    return vetorAux

# Teste 1: Vetores vazios
vetorA = [(1,2), (5,5), (12,7)]
vetorB = [(11,8), (7,7)]
resultado = comparador(vetorA, vetorB)
print("Teste 1:", resultado)  # Deve imprimir []