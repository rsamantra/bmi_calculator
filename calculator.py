import json

# Calculate the BMI

def bmi_calculator():
    # Function To calculate the BMI
    bmi_cal = lambda data: round(data["WeightKg"]/(data["HeightCm"]/100)**2, 2)    

    # sample Data
    peoples = '[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96}, {"Gender": "Male", "HeightCm": 161, "WeightKg":85}, {"Gender": "Male", "HeightCm": 180, "WeightKg": 77}, {"Gender": "Female", "HeightCm": 166, "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]'

    peoples = json.loads(peoples)

    for people in peoples:

        # Validation - if Height is present in the data or not, If yes, then the value is of type int or float
        if "HeightCm" not in people:
            continue
        elif not isinstance(people["HeightCm"],(int,float)):
            continue

        # Validation - if Weight is present in the data or not, If yes, then the value is of type int or float
        if "WeightKg" not in people:
            continue
        elif not isinstance(people["WeightKg"],(int,float)):
            continue

        bmi = bmi_cal(people)
        people["bmi"] = bmi
        if bmi <= 18.4:
            
            people["bmi_category"] = "Underweight"
            people["health_risk"] = "Malnutrition Risk"

        if 18.5 <= bmi <= 24.9:
            people["bmi_category"] = "Normal Weight"
            people["health_risk"] = "Low Risk"

        if 25 <= bmi <= 29.9:
            people["bmi_category"] = "Overweight"
            people["health_risk"] = "Enhanced Risk"

        if 30 <= bmi <= 34.9:
            people["bmi_category"] = "Moderately Obese"
            people["health_risk"] = "Medium Risk"

        if 35 <= bmi <= 39.9:
            people["bmi_category"] = "Severely Obese"
            people["health_risk"] = "High Risk"

        if bmi >= 40:
            people["bmi_category"] = "Very Severely Obese"
            people["health_risk"] = "Very High Risk"

    return json.dumps(peoples)

def main():
    return bmi_calculator()
    
    

if __name__ == "__main__":
    values = main()
    print(values)