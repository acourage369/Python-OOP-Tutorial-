from lion import Lion
from tiger import Tiger
from elephant import Elephant

# Instance of a lion
lion = Lion("Simba", 6)

print(f"{lion.get_name()} is {lion.get_age()} years, it makes a {lion.make_sound()} sound.")

# Instance of a tiger
tiger = Tiger("Timm", 8)

print(f"{tiger.get_name()} is {tiger.get_age()} years, it makes a {tiger.make_sound()} sound.")


# Instance of an elephant
elephant = Elephant("Tom", 12)

print(f"{elephant.get_name()} is {elephant.get_age()} years, it makes a {elephant.make_sound()} sound.")

