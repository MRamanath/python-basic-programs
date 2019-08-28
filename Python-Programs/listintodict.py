# A program to convert the elements of two lists into key value pairs of a dictionary.

countries = ['USA', 'India', 'Germany', 'France']
capitals = ['Washington', 'New Delhi', 'Berlin', 'Paris']

z = zip(countries, capitals)
d = dict(z)

for k,v in d.items():
    print('Country = {} and Capital = {}'.format(k, v))

# Country = USA and Capital = Washington
# Country = India and Capital = New Delhi
# Country = Germany and Capital = Berlin
# Country = France and Capital = Paris