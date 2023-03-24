# Create a Python Program that serialises and deserialises a dictionary of dictionaries using JSON and pickle
import codecs
import json
import pickle



student = {}
student['Name'] = "Shantanu"
student['Address'] = "123, Janpath, East Andheri"
student['age'] = 21
student['height'] = "170cm"
student['weight'] = "55 kgs"

# json
# serialization
with open("student.json", "w") as f:
    json.dump(student, f)


# deserialization
with open("student.json", "r") as f:
    student_dict = json.load(f)

print(student_dict)
print(student_dict['Name'])

student_list = [student_dict, student_dict]
with open("student_list.json", "w") as f:
    json.dump(student_list, f)

with open("student_list.json", "r") as f:
    person_list_from_file = json.load(f)

print(person_list_from_file)

# pickle

with open("dict1.pkl", "wb") as f:
    pickle.dump(student, f)

with open("dict1.pkl", "rb") as f:
    student_dict = pickle.load(f)

print(student_dict, type(student_dict))