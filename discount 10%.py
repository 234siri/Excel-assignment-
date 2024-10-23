def calculate_total_cost():
    quantity = int(input("Enter the quantity: "))
    unit_cost = 100
    total_cost = quantity * unit_cost
    
    if total_cost > 1000:
        total_cost = total_cost * 0.9  
        print(f"Total cost after discount: ₹{total_cost}")
    else:
        print(f"Total cost: ₹{total_cost}")
calculate_total_cost()

