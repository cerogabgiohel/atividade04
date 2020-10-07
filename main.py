import pandas as pd
df = pd.read_csv("cotacao_MGLU3.csv", sep=';')
print("A quantidade de cotações no arquivo = " + str(df['close'].size))
str(df['close'].size).to_csv("atividade04.csv")

print("O maior valor é: " + str(df['close'].max()))

print("O menor valor é: " + str(df['close'].min()))

print("A média entre o maior valor e o menor valor é: " + str((df['close'].max()+df['close'].min())/2))

print("Os 10 maiores valores são: " + str(df['close'].nlargest(10).array))

print("Os 10 menores valores são: " + str(df['close'].nsmallest(10).array))

print("Os 10 maiores valores em ordem decrescente são: " + str(df['close'].nlargest(10).array))

print("Os 10 menores valores em ordem decrescente são: " + str(df['close'].nsmallest(10).sort_values(ascending=False).array))


vetor1 = df['close'].nlargest(10).sort_values().array
vetor2 = df['close'].nsmallest(10).array
vetor3 = []
i = 0

while i < 10:
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
    i = i +1
print("Assim são os 10 maiores valores e os 10 menores intercalados em ordem crescente " + str(vetor3))


vetor3.append(999)

print("Vetor após a inserção do elemento 999 " + str(vetor3))
vetor3.append(777)

print("Vetor após a inserção do elemento 777 " +str(vetor3))
vetor3.remove(vetor3[len(vetor3)-1])

print("Vetor após a remoção utilizando a estrutura de pilha " + str(vetor3))
vetor3.remove(vetor3[0])

print("Vetor após a remoção utilizando a estrutura de fila " +str(vetor3))




