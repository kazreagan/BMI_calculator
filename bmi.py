print("Welcome!")

weight = int(input("how much do you weigh in kg?:\n"))
height = float(input("please enter your height in metres:\n"))

BMI = round(weight / (height)**2, 2)

print(f"Your Body Mass Index is: {BMI}")

def result(BMI):
    if 18.5 <= BMI < 24.9:
        return "Your weight is healthy!"
        
    elif 25.00 <= BMI < 29.9:
        return "You're overweight!"
        
    elif 30.00 <= BMI < 34.9:
        return "You're first class obese"
    
    elif 35.00 <= BMI < 40.00:
        return "You're second class obese"
        
    elif BMI >= 40:
        return "You're morbidly obese"
        
       
    else:
       
        return "You're underweight, consider eating enough."
    
level = result(BMI)
print(f"BMI: {BMI}, Category: {level}")
        