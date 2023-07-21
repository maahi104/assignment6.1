import json


# Create a dictionary of Indian states and their capitals
states = {}
for i in range(7):
    state = input("Enter state name: ")
    capital = input("Enter capital name: ")
    states[state] = capital

# Write the dictionary to a JSON file
with open('indian_states.json', 'w') as f:
    json.dump(states, f)