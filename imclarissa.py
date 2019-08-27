
alturaFloat = 1.70
pesoFloat = 65

imc = pesoFloat/(alturaFloat**2)
print(imc)
print("A muito abaixo do peso quando?", imc < 17.0)
print("B abaixo do peso normal quando?", imc >= 17.0 and imc <= 18.5)
print("C peso dentro do normal quando?", imc  > 18.5 and imc <= 25.0)
print("D acima do peso normal quando?", imc > 25.0 and imc <= 30.0)
print("E muito acima do peso normal quando?", imc > 30.0)
print(imc)

