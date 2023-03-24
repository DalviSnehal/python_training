# Investigate what happens when there is a return statement in both
# the try clause and finally clause of a try statement.

def example_2():
    try:
        val = 1
        # print("Print: Try Block")
        return "Return: Try Block"
    finally:
        val = val + 1
        # print("Print: Finally Block")
        return "Return: finally Block"


def main():
    example_2()


if __name__ == "__main__":
    main()
