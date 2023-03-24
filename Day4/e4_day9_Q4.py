# Create a class Stack and implement the push() and pop() and size() methods.
# Example stack:
# stack = []
# push(1)
# [1]
# push(2)
# [1,2]
# push(4)
# [1,2,4]
# push(10)
# [1,2,4,10]
# pop()
# [1,2,4]
# pop()
# [1,2]
class Stack:
    def __init__(self):
        self.__stack_list = []

    def push_element(self, num):
        self.__stack_list.append(num)

    def pop_element(self):
        return self.__stack_list.pop()

    def display_elements(self):
        print(self.__stack_list)


def main():
    stack = Stack()
    stack.push_element(5)
    stack.push_element(3)
    stack.display_elements()
    stack.pop_element()
    stack.display_elements()


if __name__ == "__main__":
    main()
