#Q.1 
# Create a list called 'names' with the names of a few friends
names = ["Uzair", "Bilal", "Mohsin", "Jamil", "Zeeshan"]
# Print each person's name by accessing each element in the list
print(names[0])  
print(names[1])  
print(names[2])  
print(names[3])  
print(names[4])  

#Q.2
names = ["Uzair", "Bilal", "Mohsin", "Jamil", "Zeeshan"]
# Print a personalized message for each friend
msg_0 = f"Hello, {names[0]}! How are you?"
msg_1 = f"Hello, {names[1]}! How are you?"
msg_2 = f"Hello, {names[2]}! How are you?"
msg_3 = f"Hello, {names[3]}! How are you?"
msg_4 = f"Hello, {names[4]}! How are you?"
print(msg_0)
print(msg_1)
print(msg_2)
print(msg_3)
print(msg_4)

#Q.3
vehicles = ["Honda Civic", "Honda City", "Corolla Altis"]
veh_0 = f"I would like to drive {vehicles[0]}."
veh_1 = f"I would like to drive {vehicles[1]}."
veh_2 = f"I would like to drive {vehicles[2]}."
print(veh_0)
print(veh_1)
print(veh_2)

#4
# Create a list called 'guests' with the names of people you'd like to invite to dinner

guests = ["Uzair", "Bilal", "Mohsin"]

# Print a personalized invitation message for each guest

print(f"Dear {guests[0]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests[1]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests[2]}, I would be honored to have you join me for dinner.")

#5
guests_1 = ["Uzair", "Bilal", "Mohsin"]

print(f"Dear {guests_1[0]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests_1[1]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests_1[2]}, I would be honored to have you join me for dinner.")

can_not_attend = guests_1[1]
print(f"\nUnfortunately, {can_not_attend} can't make it to the dinner.")

guests_1[1] = "Jamil"
print("\nUpdated invitations:")
print(f"Dear {guests_1[0]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests_1[1]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests_1[2]}, I would be honored to have you join me for dinner.")

#Q.6
guests_2 = ["Uzair", "Bilal", "Mohsin"]

print(f"Dear {guests_2[0]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests_2[1]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests_2[2]}, I would be honored to have you join me for dinner.")

# Inform that a bigger table has been found
print("\nGood news! We found a bigger table.")

# Add new guests to the list
guests_2.insert(0, "Ali")  # Add a guest to the beginning of the list
guests_2.insert(2, "Zeeshan")        # Add a guest to the middle of the list
guests_2.append("Jamil")        # Add a guest to the end of the list

print("\nUpdated invitations:")
print(f"Dear {guests_2[0]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests_2[1]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests_2[2]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests_2[3]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests_2[4]}, I would be honored to have you join me for dinner.")
print(f"Dear {guests_2[5]}, I would be honored to have you join me for dinner.")

#Q.7







