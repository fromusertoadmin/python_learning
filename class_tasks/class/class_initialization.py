class Book:
  is_closed = False
  current_page = None

  #def __new__(cls, height, weight):
  #  pass

  def __init__(self, height, weight):
    self.height = height
    self.weight = weight


  def close_book(self):
    self.is_closed = True

  def open_book(self):
    self.is_closed = False
    self.current_page = 0

  def move_to_page(self, page):
    self.current_page = page

  def __str__(self):
    return 'Book'

  def dummy_function(arg):
    print('dummy_function')

  def __call__(self):
    print('call')



book_instance = Book(10, 10)
print(book_instance)

print(book_instance())

book_instance.another_attr = 56
print(book_instance.another_attr)

setattr(book_instance, 'dummy_attr', 'dummy')

print(book_instance.dummy_attr)

print('GetAttr = {}'.format(getattr(book_instance, "non_existing_attr", 10)))

print('Everything under object={}'.format(book_instance.__dict__))

book_instance.__dict__['dir_attr'] = 10


print(book_instance.__dict__)
print(dir(book_instance))

print(isinstance(book_instance, Book))
print(issubclass(book_instance, object))


