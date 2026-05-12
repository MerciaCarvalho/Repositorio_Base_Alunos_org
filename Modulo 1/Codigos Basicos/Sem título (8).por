programa {
  funcao inicio() {
   //Verificar se o número é positivo
   //Verificar se o número é negativo 
  //Verificar se o número é zero
    inteiro numero
    logico ehPositivo
    logico ehNegativo
    logico ehZero

    escreva("Digite um número: ")
    leia(numero)

    ehPositivo = numero > 0
    ehNegativo = numero < 0
    ehZero = numero == 0

    escreva("esse número é positivo? ", ehPositivo)
escreva("\nEsse número é negativo? ", ehNegativo)
escreva("\nEsse número é igual a zero? ", ehZero)
  }
}
