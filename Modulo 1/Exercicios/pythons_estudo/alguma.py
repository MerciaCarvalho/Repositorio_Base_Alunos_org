#programa {
  #funcao inicio() {
    
    #real peso,altura,imc

    #escreva("Digite o peso em kg: ")
    #leia(peso)

    #escreva("Digite a altura em m: ")
    #leia(altura)

    #imc = peso / (altura * altura)

    #escreva("O imc é: ", imc)

peso = float( input("Digite o peso em kg: ") )

altura = float( input("Digite a altura em m: ") )

imc = peso / (altura * altura)

print(imc)



