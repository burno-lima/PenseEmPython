"""Escreva uma função chamada right_justify, que receba uma string chamada s como parâmetro e exiba a string com espaços suficientes à frente para que a última letra da string esteja na coluna 70 da tela"""

def right_justify(s):
    word = f"                                                                 {s}"
    print(word)
    print('Quantidade de espaços', len(word))
    
if __name__ == '__main__':
    right_justify('monty')
