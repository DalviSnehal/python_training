# Modify the queue class you created last time and make
# the functionality such that you can delete
# and add elements from both ends of the list. The methods should
# be addFirst, addLast, deleteFirst, deleteLast

class Queue:
    def __init__(self):
        self.__queue_list = []

    def add_element_at_end(self, num):
        self.__queue_list.append(num)

    def add_element_at_start(self, num):
        self.__queue_list.insert(0, num)

    def reomve_element_at_first(self):
        return self.__queue_list.pop(0)

    def remove_element_at_last(self):
        return self.__queue_list.pop(-1)

    def print_elements(self):
        print(self.__queue_list)

def main():
    queue = Queue()
    queue.add_element_at_end(5)
    queue.add_element_at_end(3)
    queue.add_element_at_start(7)
    queue.print_elements()
    print(queue.reomve_element_at_first())
    print(queue.remove_element_at_last())
    queue.print_elements()



if __name__ == "__main__":
    main()
