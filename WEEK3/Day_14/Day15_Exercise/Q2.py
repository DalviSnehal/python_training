# Create a Python Program that serialises and deserialises a class VideoGameCharacter using JSON and pickle.
# Create 4 parameters for VideoGameCharacter

import json
import  pickle

class VideoGameCharacter:
    def __init__(self, name, level, rating):
        self.name = name
        self.level = level
        self.rating = rating

    def print_attributes(self):
        print("attributes are:", self.name, self.level, self.rating)


def main():
    vgc = VideoGameCharacter("ludo", 4, 5)
    print(vgc.__dict__)

    # in memory serialization
    vgc = json.dumps(vgc.__dict__)
    print("json dumps", vgc, type(vgc))

    list_mem_ser = pickle.dumps(person_lst)
    print(type(list_mem_ser))
    new_lst = pickle.loads(list_mem_ser)
    print(new_lst)
    print(new_lst == person_lst)

if __name__ == "__main__":
    main()