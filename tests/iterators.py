1)
l = [1, 2, 3, 4, 5]

list_iterator = iter(l)
print(list_iterator)

another_list_iterator = iter(l)
print(another_list_iterator)

last_list_iterator = iter(l)
print(last_list_iterator)


2)
l = [1, 2, 3, 4, 5]

list_iterator = iter(l)
print(next(list_iterator))

another_list_iterator = iter(l)

print(next(list_iterator))
print(next(another_list_iterator))

3)
l = [1, 2, 3, 4, 5]

list_iterator = iter(l)
try:
  print(next(list_iterator))
  print(next(list_iterator))
  print(next(list_iterator))
  print(next(list_iterator))
  print(next(list_iterator))
  print(next(list_iterator))
except StopIteration:
  print('stop_iter')


4)
iter('12345')
list_iterator = iter(None)

5)

