f = open("speech1.txt")
print(f)

txt = f.read()

print(type(txt))
print(txt)
print("total no of words in speech 1 file", len(txt))


with open("speech1.txt", 'r') as fp:
    x = len(fp.readlines())
    print('Total lines:', x)
