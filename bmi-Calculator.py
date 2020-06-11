def bmi_calc():
    height = float(input("Please type in your height in (meters)"))
    weight =  float(input("Please enter your weight in (kg)"))

    while True:
        print(round(weight / height ** 2))
        break
        
bmi_calc()
