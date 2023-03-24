# Rewrite the below code to utilise a generator function instead of
# using map and lambda
# names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]


def strip_list():
    names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy"]
    for name in names:
        yield name.strip()


def is_title():
    names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy"]
    for name in names:
        yield name.title()

def main():
    sl = strip_list()
    t = is_title()
    a= []
    for i in sl:
        print(i)
    for i in t:
        a.append(i)
        print(i)
if __name__ == "__main__":
    main()
