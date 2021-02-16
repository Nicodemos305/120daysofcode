def subtrair(value1, value2):
    try:
        return check_number(valor1) - check_number(valor2)
    except:
        print("Ocorreu algum erro na subtração, algum dos valores pode não ser um número.")

def check_number(value_tmp):
    if type(value_tmp) is int or type(value_tmp) is float:
        return value_tmp
    elif value_tmp.find(".") != -1:
        return float(value_tmp)
    return int(value_tmp)

if __name__ == "__main__":
    valor1 = input("Digite o primeiro valor ")
    valor2 = input("Digite o segundo valor ")
    print(subtrair(valor1, valor2))