def soma(value1, value2):
    try:     
        valor1 = check_numbers(value1)
        valor2 = check_numbers(value2)
        soma = valor1 + valor2
        print(f"A soma dos valores é  {soma}")
    except:
        print("Ocorreu um erro na soma, algum dos valores pode não ser um número.")

def check_numbers(value_tmp):
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
    soma(valor1, valor2)