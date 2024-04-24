import math
def get_values():
    height = float(input("Enter your Height in centimeteres (cm) : "))
    weight = float(input("Enter your weight in kilograms (kg) : "))
    if height <= 0 or weight <= 0:
        print("invalid Height or Weight")
    elif height <=0 and weight <= 0:
        print("Invalid Height and Weight")
    return height, weight

def check_BMI(height, weight):
    height = height / 100
    height = (height)**2
    print(f"your height is {height} meters")
    print(f"your weight is {weight} kilograms")
    bmi = weight / height
    print(f"your body mass index is : {round(bmi, 4)} kg/m\u00b2 ")
    if bmi < 18.5 : 
        print("You are underweight!, we recommend you to take nutrition properly")
    elif bmi > 18.5 and bmi < 24.9:
        print("You are having a Healthy Nuitrion")
    elif bmi > 25.0 and bmi < 29.9:
        print("You are Overweight!, we recommend you to do some exercise")
    else:
        print("We recommend you to loose some more weight")

height, weight = get_values()
check_BMI(height, weight)

