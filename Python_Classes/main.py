from Dog import Dog
from Cat import Cat

first1 = Dog(67, 'dobberman', 'woop')
print(first1.get_animal_cry())
print(first1.get_breed())

sec2 = Cat(34, 'kitten-cute', 'meow')

print(sec2.get_animal_cry())
print(sec2.get_breed())

sec2.set_breed('Mama Cat')
sec2.set_animal_cry('meeeooowww')
sec2.set_height(67)

print(sec2.get_animal_cry())
print(sec2.get_breed())
print(sec2.get_height())
