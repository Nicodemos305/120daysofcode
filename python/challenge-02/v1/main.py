def subtrair(value1, value2):
    try:
        valor1 = check_number(value1)
        valor2 = check_number(value2)
        subtracao = valor1 - valor2
        print(f"O resultado da subtracao é {subtracao}")
    except:
        print("Ocorreu algum erro na subtração, algum dos valores pode não ser um número.")

def check_number(value_tmp):
    if type(value_tmp) is int:
        return value_tmp
    elif type(value_tmp) is float:
        return value_tmp
    elif value_tmp.find(".") != -1:
        return float(value_tmp)
    else:
        return int(value_tmp)

if __name__ == "__main__":
    valor1 = input("Digite o primeiro valor ")
    valor2 = input("Digite o segundo valor ")
    subtrair(valor1, valor2)