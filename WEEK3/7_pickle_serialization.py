import json
import codecs
import pickle

person = {}
person['Name'] = "Shantanu"
person['Address'] = "123, Janpath, East Andheri"
person['age'] = 21
person['height'] = "170cm"
person['weight'] = "55 kgs"
person_lst = [person, person]
with open("dict.pkl", "wb") as f:
    pickle.dump(person, f)

with open("dict.pkl", "rb") as f:
    person_dict = pickle.load(f)

print(person_dict, type(person_dict))


class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type

    def print_attr(self):
        print("animal attributes are:", self.name, self.animal_type)


animal = Animal("Caesar", "Dog")
with open("animal.pkl", "wb") as f:
    pickle.dump(animal, f)

with open("animal.pkl", "rb") as f:
    animal_obj = pickle.load(f)
    animal_obj.print_attr()

list_mem_ser = pickle.dumps(person_lst)
print(type(list_mem_ser))
new_lst = pickle.loads(list_mem_ser)
print(new_lst)
print(new_lst == person_lst)



if __name__ == "__main__":
    pass
