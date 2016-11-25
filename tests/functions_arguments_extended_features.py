1)

def func():
    raise OSError

try:
    func()
except Exception:
    pass
finally:
    print('finally')
    
    
    
2)
def func(a):
    return None

for i in [1,2,3]:
    if not func(i):
        print('i')
        
        
3)
list = [1, 2, 3, 4, 5]


def process_list(list):
    result = []
    for i in list:
        result.append(i)
    return result

res = process_list(list)
print(res == list)

4)

def check_if_list_is_empty(list):
    return not list


print(check_if_list_is_empty([]))
print(check_if_list_is_empty([0]))


5)list = None

def func(list):
    list = [1,2,3]
    return list

print(list)
print(func)



6)
l = [0,1,2,3,4]
def iterate_list(l):
    for index, value in enumerate(list):
        print(index, value)

    for i in enumerate(list):
        print(i)


if not iterate_list(l):
    raise Exception('Nothing')
    
    
7)


def calculate_item(item):
    return item + 1 

generated_list = [calculate_item(x) for x in [0, 1, 2, 3]]
print(generated_list)

if 10 in generated_list:
    print('10 exists')
if generated_list:
    print('list exists')

if 10 not in generated_list:
    print('10 not in generated_list')

if len(generated_list) > 0:
    print(len(generated_list))
print(len)


8)

def calculate_args(*args):
    if not args:
        return
    else:
        return args[0]
    if len(args) > 0:
        return args


calculate_args()
calculate_args(1, 2, 3, 4)
calculate_args(1)



