height = float(input("Type your height, example(1.70): "))
weight = float(input("Type your weight, example(60.5): "))
imc = weight / (height*height)

if imc < 18.5:
    print("Underweight")

elif imc >= 18.5 and imc <=24.9:
    print("Nomral Weight")

elif imc >= 25 and imc <=29.9:
    print("Overweight")

elif imc >= 30:
    print("Obesity")
