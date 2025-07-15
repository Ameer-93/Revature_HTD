# Create a dictionary
person = {'name': 'John', 'age': 25}

# Access value
print("Name:", person['name'])

# Add new key
person['city'] = 'Delhi'
print("After adding city:", person)

# Update value
person['age'] = 26
print("After updating age:", person)

# Remove a key
person.pop('city')
print("After removing city:", person)

# Check keys and values
print("Keys:", person.keys())
print("Values:", person.values())
