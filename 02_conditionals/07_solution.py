# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = input("Enter coffee size: ")

extra_shot = input("Would you like an extra shot of espresso? (yes/no): ").strip().lower()

if extra_shot == "yes":
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print("Order:", coffee)

