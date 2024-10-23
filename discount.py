def calculate_bonus():
    salary = float(input("Enter your salary: "))
    years_of_service = int(input("Enter your years of service: "))
    
    if years_of_service > 5:
        bonus = salary * 0.05  
        print(f"Net bonus amount: ₹{bonus}")
    else:
        print("No bonus as years of service are 5 or less.")

calculate_bonus()
