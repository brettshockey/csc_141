guest_list = ['Big Sean', 'Michael Vick', 'Troy Polamalu']

print("Good news! There is a larger table that has become available at The Best Restaurant Ever. More guests will be invited!")

guest_list.insert(0, "Antonio Brown",)
guest_list.insert(2, "Jalen Ramsey")
guest_list.append("Randy Moss")

print(f"\nA select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[0].title()}! It will be an evening to remember!")
print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[1].title()}! It will be an evening to remember!")
print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[2].title()}! It will be an evening to remember!")
print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[3].title()}! It will be an evening to remember!")
print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[4].title()}! It will be an evening to remember!")
print(f"A select group of distinguished individuals are invited to dinner! We would be delighted to have you, {guest_list[5].title()}! It will be an evening to remember!")

print(f"\nDue to unforseen circumstances regarding availability, I am forced to rescind the invitation. Please look forward to the next invitation {guest_list[5].title()}!")
guest_list.pop(5)
print(f"Due to unforseen circumstances regarding availability, I am forced to rescind the invitation. Please look forward to the next invitation {guest_list[4].title()}!")
guest_list.pop(4)
print(f"Due to unforseen circumstances regarding availability, I am forced to rescind the invitation. Please look forward to the next invitation {guest_list[3].title()}!")
guest_list.pop(3)
print(f"Due to unforseen circumstances regarding availability, I am forced to rescind the invitation. Please look forward to the next invitation {guest_list[2].title()}!")
guest_list.pop(2)

print(f"\nThis will hopefully be the last update to the invitations being sent out for this evening's event. Rest assured, you are still invited {guest_list[0]}!")
print(f"This will hopefully be the last update to the invitations being sent out for this evening's event. Rest assured, you are still invited {guest_list[1]}!")

del guest_list[0]
del guest_list[0]

print(guest_list)