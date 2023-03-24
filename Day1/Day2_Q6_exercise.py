# Create a list of Animal objects(minimum 5) and then iterate through them and print their attributes
class Animal:
    def __init__(self, sound):
        self.sound = sound


animal1 = Animal("Bark")
animal2 = Animal("moo")
animal3 = Animal("shouting")
animal4 = Animal("screeming")
list1=[animal1 ,animal2, animal3, animal4]
for i in list1:
    print(i.sound)



