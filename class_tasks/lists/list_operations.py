sample_list = ['1', 2, 4.5, 's']

print(sample_list)

print('Main operations')
print(sample_list.append(0))
print(sample_list)
print(sample_list.extend(['1', 2]))
print(sample_list)

print('Count = ' + str(len(sample_list)))

reversed_list = sample_list.reverse()

print('Reversed List {0}'.format(reversed_list))
print(reversed_list)


sample_list.insert(30, 100)
print(sample_list)

print('Index = {}'.format(sample_list.index(100)))

print('Last Element = {}'.format(sample_list.pop()))

print(sample_list)


another_list = sample_list
last_list = sample_list

last_list[0] = 100000
print(last_list)
print(another_list)

del last_list[0]

print(last_list)

print('Test' in last_list)