import json


def main():

    with open("countries_data.json", "r") as f:
        countries_dict = json.load(f)
        print(countries_dict)


if __name__ == "__main__":
    main()
