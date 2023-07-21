import json

states = {
    'andhra pradesh': 'hyderabad',
    'gujarat': 'ganhinagar',
    'karnataka': 'bengalore',
    'maharashtra': 'mumbai',
    'rajasthan': 'jaipur',
    'tamil nadu': 'chennai',
    'uttra prades': 'lucknow' 
}    
#write the following dict to a jsno file
with open('E:/indian_states.json','w') as file:
    json.dump(states,file)
print('json file created successfully!')
