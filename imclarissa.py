print("programa para calcular IMC")
alturaFloat = input("digite sua altura (em metros): ")
pesoFloat = input ("digite seu peso (em kg): ")

imc = float(pesoFloat)/(float(alturaFloat)**2)

print(imc)

if imc < 17.0:
    print("A muito baixo peso!")
elif imc >= 17.0 and imc <= 18.5:
    print ("B abaixo do peso normal")
elif imc  > 18.5 and imc <= 25.0:
    print("C peso dentro do normal")
elif imc > 25.0 and imc <= 30.0:
    print("D acima do peso normal")
else: imc > 30.0
