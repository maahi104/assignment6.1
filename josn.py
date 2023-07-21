import json

# Create a dictionary of Indian states and their capitals
states = {
    'Andhra Pradesh': 'Amaravati',
    'Gujarat': 'Gandhinagar',
    'Karnataka': 'Bengaluru',
    'Maharashtra': 'Mumbai',
    'Odisha': 'Bhubaneswar',
    'Rajasthan': 'Jaipur',
    'Tamil Nadu': 'Chennai'
}

# Write the dictionary to a JSON file
with open('indian_states.json', 'w') as f:
    json.dump(states, f)

