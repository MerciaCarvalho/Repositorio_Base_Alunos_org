temperatura = float(input("Digite s temperatura em celcius: "))

if temperatura >= 30:
    print("Está quente!")
elif temperatura >= 20:
    print("Está agradavel")
elif temperatura >= 10:
    print("Está frio!")
else:
    print("Está muito frio!")