first_variant = dict()
first_variant['key'] = 10

another_variant = {'key': 10}

third_variant = dict(key=10)

print('Keys={}'.format(first_variant.keys()))
print('Values={}'.format(first_variant.values))
print('Items={}'.format(first_variant.items()))

print('Before clear {}'.format(another_variant))
print('After clean {}'.format(another_variant.clear()))


print('IN operator {}'.format(7 in first_variant))

print('Add another key')
first_variant['another_key'] = 20

print(first_variant)

print('Merge')
print(first_variant.update({'key': 30}))

print(first_variant)


print('Get not existed key')

print(first_variant.get('unknown_key', 10))


print('delete key')

del first_variant['key']

print(first_variant)

print('length')

print(len(first_variant))