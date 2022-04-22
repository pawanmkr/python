def find_in_tup(veggies, element):
    result = any(element in tu for tu in veggies)
    return result


veggies = (
    ('cucumber', 'potato', 'brinjal'),
    ('aaloo', 'bhindi', 'kaddoo'),
    ('tomato', 'pyaaz', 'mirch'),
)

print(veggies)
elem = 'aaloo'
print(find_in_tup(veggies, elem))
