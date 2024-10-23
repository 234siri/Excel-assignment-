def calculate_electricity_bill(installed_load, energy_consumed):
	 fixed_charge = installed_load * 75
	 variable_charge = 0
	 if energy_consumed <= 50:
		  variable_charge = energy_consumed * 4.75
	 elif energy_consumed <= 100:
		 variable_charge = (50 * 4.75) + (energy_consumed - 50) * 5.75
	 elif energy_consumed <= 200:
		  variable_charge = (50 * 4.75) + (50 * 5.75) + (energy_consumed - 100) * 7
	 else:
		 variable_charge = (50 * 4.75) + (50 * 5.75) + (100 * 7) + (energy_consumed - 200) * 8
	 total_bill = fixed_charge + variable_charge
	 return total_bill
installed_load = float(input("Enter the installed load in kW: "))
energy_consumed = float(input("Enter the energy consumed in units (kWh): "))
total_bill = calculate_electricity_bill(installed_load, energy_consumed)
print(f"Your total electricity bill is: ₹{total_bill:.2f}")
