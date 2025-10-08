#project named bill buddy
import random
names=input("Enter everyone's name separated by commas:")
names_list = names.split(",")
random_choice = random.choice(names_list)
print(f"The {random_choice}  is going to pay the bill today.")
