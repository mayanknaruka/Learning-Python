# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = "dog"
age = 2

if pet == "dog":
    if age < 2:
        print("Puppy Food")
    else:
        print("Adult Dog Food")

elif pet == "cat":
    if age > 5:
        print("Senior Cat Food")
    else:
        print("Adult Cat Food")

else:
    print("Food recommendation not available.")
