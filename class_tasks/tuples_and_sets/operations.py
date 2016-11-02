from collections import namedtuple

sample_tuple = (1, 2, 3,)

print(sample_tuple)

print('Length={}'.format(len(sample_tuple)))

print('+ Operation={}'.format(sample_tuple + (3, 4, 5)))

print('Index={}'.format(sample_tuple.index(3)))


print('Converted_list={}'.format(list(sample_tuple)))


record_tuple = namedtuple('Rec', ['name', 'age', 'jobs'])
tuple_instance = record_tuple('Bob', age=40.5, jobs=['dev', 'mgr'])
print(tuple_instance)


sample_set = set([1, 2, 3, 4])
another_set = set([0])
print(sample_set)
print(another_set)
sample_set.add(6)
sample_set.add(1)

intersection = sample_set.intersection(another_set)
union = sample_set.union(another_set)
difference = sample_set.difference(another_set)

print('Intersection ={}'.format(intersection))
print('Union={}'.format(union))
print('Diff={}'.format(difference))

#remove
#discard
#clear
