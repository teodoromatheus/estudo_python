def perimeto_circulo()->float:
    '''
    Retorna o perímetro do circulo com o raio passado pelo usuário
    '''
    try:
        raio = float(input("Digite o valor do raio: "))
        perimetro = 2*3.14*raio
        perimetro_arredondado = round(perimetro,2)
        return perimetro_arredondado
    except ValueError:
        print("Tipo de dado não é número")
        exit()
    except Exception as e:
        print(e)
        exit()

if __name__ == "__main__":
    print(perimeto_circulo())