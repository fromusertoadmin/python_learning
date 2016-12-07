print('first_module')

from second_module import X
from second_module import X as X_from_module_2

print(X)
print(X_from_module_2)
import third_module

if __name__ == '__main__':
    print('main block')


print('Continue import')


SOME_VARIABLE = 'some_var'


X = 78

import second_module


second_module.X = 78

print(second_module.X)


from second_module import X

print(X)


from third_module import X as X_from_module_3

print(X_from_module_3)

from imp import reload

reload(third_module)

