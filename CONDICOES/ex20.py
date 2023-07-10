sal = float(input("Digite seu salario: "))
if sal >= 1250:
    acres = (sal*0.10)+sal
else:
    acres = (sal*0.15)+sal
print("O salario novo é: {:.2f}".format(acres))