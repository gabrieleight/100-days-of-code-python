"""
Day 7 - 100 Days of Python
1. Write a program to convert temperature from Celsius to Fahrenheit. 
2. Write a program to convert temperature from Fahrenheit to Celsius
"""

def convert_temperature(value, scale):
    T_f = 0
    T_c = 0
    if scale.lower() == "celsius" or scale.lower() == "c":
        T_c = value
        T_f = (9*T_c/5) + 32
        print("Escala convertida: Celsius -> Fahrenheit")
        return T_f
    elif scale.lower() == "fahrenheit" or scale.lower() == "f":
        T_f = value
        T_c = (5*T_f - 160)/9
        print("Escala convertida: Fahrenheit -> Celsius")
        return T_c
    else:
        print("Dados invalidos! Repita novamente!")
        convert_temperature()

if __name__ == "__main__":
    escala = input("Qual a escala termométrica selecionada (Celsius [C] ou Fahrenheit [F]): ")
    valor = float(input("Digite o valor da temperatura da escala: "))
    valor_convertido = convert_temperature(valor, escala)
    print(f"O valor convertido é {valor_convertido:,.1f}")