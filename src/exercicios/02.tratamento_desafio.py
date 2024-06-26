### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
# 4) Calcule o valor do bônus final
# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

def calculo_bonus()->str:
    '''
    Função que retorna o nome do usuário (input), salário (calculated) e bônus (input)
    '''
    NOME_GATE: bool = False
    SALARIO_GATE: bool = False
    BONUS_GATE: bool = False

    while NOME_GATE is not True:
        nome_usuario: str = str(input("Digite seu nome: "))
        if nome_usuario.isdigit():
            print("O nome é um número")
        elif nome_usuario.isspace():
            print("Nome está em branco")
        else:
            NOME_GATE = True

    while SALARIO_GATE is not True:
        try:
            salario: float = float(input("Digite o seu salário: "))
            if salario <= 0:
                print("Valor do salário negativo ou zerado")
            else:
                SALARIO_GATE = True
        except ValueError:
            print("Não é um número válido")
    
    while BONUS_GATE is not True:
        try:
            bonus: float = float(input("Digite o seu bônus (ex.: '10' para 10%): "))
            if bonus < 0:
                print("Valor do bônus menor que 0")
            else:
                BONUS_GATE = True
        except ValueError:
            print("Não é um número válido")
    
    bonus_calculado: float = round(salario*bonus/100,1)
    return print(f"{nome_usuario}, seu salário é de {salario} reais e seu bônus de {bonus_calculado} reais")

if __name__ == '__main__':
    calculo_bonus()