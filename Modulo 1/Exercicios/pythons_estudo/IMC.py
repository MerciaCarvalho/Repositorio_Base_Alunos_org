massa_muscular = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura: "))

imc = massa_muscular / (altura * altura )

if imc >= 30.0:
    print("Cuidado com a saúde.")
