import json
import csv

def main():


    # # file syntax
    # # Reading from a file
    #
    # f = open("test_file.txt")
    # print(f)
    #
    # # txt = f.read()
    # # print(type(txt))
    # # print(txt)
    #
    # # read partially:
    # txt = f.read(7)
    # print(type(txt))
    # print(txt)
    #
    #
    # # read line by line
    # line = f.readline()
    # print(type(line))
    # print(line)
    # line2 = f.readline()
    # print(line2)
    #
    # lines = f.readlines()
    # print(type(lines))
    # print(lines)
    # print(lines[0])
    # f.close()
    #
    with open("test_file.txt", "r") as f:
        txt = f.read()
        print(txt.splitlines())

    # appending to a file
    import os
    if os.path.exists("./test_file_2.txt"):
        os.remove("./test_file_2.txt")
    else:
        print("please check if the file exists")


   # JSON files

    person = {}
    person['Name'] = "Shantanu"
    person['Address'] = "123, Janpath, East Andheri"
    person['age'] = 21
    person['height'] = "170cm"
    person['weight'] = "55 kgs"

    json_str = json.dumps(person)
    print(type(json_str), json_str)

    with open("person.json", "w") as f:
        json.dump(person, f)


    # Csv files
    with open("test_csv.csv", "r") as f:
        csv_file = csv.reader(f)
        print(type(csv_file))
        print(csv_file)
        for idx, row in enumerate(csv_file):
            if idx == 0:
                # this is the first row which contains the col names
                pass
            else:
                # do the processing that is required
                print(row)
                row_add = sum(map(int, row))
                print(row_add)



if __name__ == "__main__":
    main()