import json
import codecs
"""
person = {}
person['Name'] = "Shantanu"
person['Address'] = "123, Janpath, East Andheri"
person['age'] = 21
person['height'] = "170cm"
person['weight'] = "55 kgs"

# javascript object notation
# serialization
with open("person.json", "w") as f:
    json.dump(person, f)
with open("person.json", "r") as f:
    person_dict = json.load(f)

print(person_dict)
print(person_dict['Name'])

"""
# deserialization

person_list = [person_dict, person_dict]
with open("person_list.json", "w") as f:
    json.dump(person_list, f)

with open("person_list.json", "r") as f:
    person_list_from_file = json.load(f)

print(person_list_from_file)

class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

    def print_attr(self):
        print("Animal attributes are:", self.name, self.animal_type)

class Zoo:
    def __init__(self, animals):
        self.animals = animals

    def print_attr(self):
        print("zoo attributes:", self.animals)
        for _animal in self.animals:
            _animal.print_attr()

    @staticmethod
    def from_json(zoo_json):
        zoo_dict = json.loads(zoo_json)
        zoo_obj_new = Zoo(**zoo_dict)
        animal_lst = []
        for _animal in zoo_obj_new.animals:
            animal_lst.append(Animal(**_animal))
        zoo_obj_new.animals = animal_lst
        return zoo_obj_new

animal = Animal("Caesar", "Dog")
print(animal.__dict__)

# in memory serialization
animal_obj_ser = json.dumps(animal.__dict__)
print("json dumps", animal_obj_ser, type(animal_obj_ser))

# deserialization
animal_obj_deser = json.loads(animal_obj_ser)
print(animal_obj_deser, type(animal_obj_deser))
new_animal_obj = Animal(**animal_obj_deser)
new_animal_obj.print_attr()

animal_dog = Animal("Caesar", "Dog")
animal_cat = Animal("Mandu", "Cat")

animal_list = [animal_cat, animal_dog]
zoo = Zoo(animal_list)
zoo.print_attr()

zoo_json = json.dumps(zoo.__dict__, default=lambda o: o.__dict__)
print(zoo_json)
"""
zoo_dict = json.loads(zoo_json)
print(zoo_dict)
zoo_obj_new = Zoo(**zoo_dict)
zoo_obj_new.print_attr()
"""
zoo_obj_new = zoo.from_json(zoo_json)
zoo_obj_new.print_attr()

if __name__ == "__main__":
    pass