concentracao = int(input("Digite a concentração do medicamento: "))
peso = int(input("Digite o peso: "))
dose = int(input("Digite a dose: "))
dose_total = peso * dose / concentracao * 20
print("De", dose_total, "gotas de remédio: ") 