# Implement a Queue class in Python which you add elements at the end and remove from the front.

class Queue:
    def __init__(self):
        self.__queue_list = []

    def add_element(self, num):
        self.__queue_list.append(num)

    def reomve_element(self):
        return self.__queue_list.pop(0)

    def print_elements(self):
        print(self.__queue_list)

def main():
    queue = Queue()
    queue.add_element(5)
    queue.add_element(3)
    queue.print_elements()
    print(queue.reomve_element())
    queue.print_elements()



if __name__ == "__main__":
    main()
