# Dicionário para converter número do mês em nome
month_names = {
    1: "janeiro",
    2: "fevereiro",
    3: "março",
    4: "abril",
    5: "maio",
    6: "junho",
    7: "julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",data

        12: "dezembro"
}

# Inicializar variáveis
total_temperature = 0
hot_months = 0
hottest_month = [0, -90]
coldest_month = [0, 60]

# Loop para coletar dados para cada mês
for month in range(1, 13):
    while True:
        try:
            # Coletar dados do usuário
            temperature = input(f"Insira a temperatura máxima em graus Celsius para {month_names[month]}: ")

            # Substituir a vírgula por um ponto
            temperature = temperature.replace(',', '.')

            # Converta a temperatura para float
            temperature = float(temperature)

            # Validar dados de entrada
            if -90 <= temperature <= 60:
                total_temperature += temperature

                # Verificar se a temperatura é "escaldante"
                if temperature > 40:
                    hot_months += 1

                # Verificar se é o mês mais quente ou mais frio
                if temperature > hottest_month[1]:
                    hottest_month = [month, temperature]
                if temperature < coldest_month[1]:
                    coldest_month = [month, temperature]

                # Quebra o loop para avançar para o próximo mês
                break
            else:
                print("Erro: Insira uma temperatura válida entre -90 e 60 graus Celsius.")
        except ValueError:
            print("Erro: Insira um número válido.")

# Calcular a média da temperatura
average_temperature = total_temperature / 12

# Exibir resultados
print(f"A temperatura média máxima anual foi {average_temperature:.2f} graus Celsius.")
print(f"Houve {hot_months} meses escaldantes.")
print(f"O mês mais escaldante do ano foi {month_names[hottest_month[0]]} com {hottest_month[1]:.2f} graus Celsius.")
print(f"O mês menos quente do ano foi {month_names[coldest_month[0]]} com {coldest_month[1]:.2f} graus Celsius.")

