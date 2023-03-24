
class ShoppingBag:
    def __init__(self, shoes, clothes, socks):
        self.shoes = shoes
        self.clothes = clothes
        self.socks = socks

    def __len__(self):
        return self.shoes * 2 + self.clothes + self.socks * 2

    def __add__(self, other):
        return self.shoes * 2 + self.clothes + self.socks * 2 + other.shoes * 2 + other.clothes + other.socks * 2

    def __mul__(self, other):
        return (self.shoes * 2 + self.clothes + self.socks * 2) * (other.shoes * 2 + other.clothes + other.socks * 2)

def main():
    bag1 = ShoppingBag(4, 4, 4)
    bag2 = ShoppingBag(5, 5, 5)
    print(len(bag1))
    print(bag1 + bag2)
    print(bag1 * bag2)


if __name__ =="__main__":
    main()