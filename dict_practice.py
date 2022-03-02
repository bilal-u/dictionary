countries = {"CA": "Canada",
"US": "United States",
"MX": "Mexico"}

numbers = {1: "One", 2: "Two", 3: "Three",
4: "Four", 5: "Five"}

d1 = {1: "One", 2: "Two", 3: "Three",
4: "Four", 5: "Five"}

# access element: d1[key]
print(f'key: {d1.keys()} \n values: {d1.values()}')

print('print keys and values in to separate lists ')
keys = []
values = []

for key in d1.keys():
    keys.append(key)
print(f'Keys: {keys}')

for val in d1.values():
    values.append(val)
print(f'Values: {values}')

# set values
print(f'Set values to dict:')
d1[6] = "Six"

d1[1] = 'One'

print(d1)

# Code that uses the get() method
print(d1.get(1))

print(d1.get(7))

# The syntax for deleting an item

del d1[6]
print(d1)



print(countries.values())
print(countries.keys())
print(countries.items())

# make two list one for keys and another for values

for key in countries:
    print(key,countries[key])

