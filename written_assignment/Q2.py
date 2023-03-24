# 2. What are the 2 ways to access private variables. Write 2 programs as examples to showcase it
# creating a class
# class Sample:
#    def __init__(self, nv, pv):
#       # normal variable
#       self.nv = nv
#       # private variable(not really)
#       self.__pv = pv
# # creating an instance of the class Sample
# def main():
#     sample = Sample('Normal variable', 'Private variable')
#     # accessing *nv*
#     print(sample.nv)
#     # accessing *__pv**
#     print(sample.__pv)
# creating a class
class Sample:
   def __init__(self, nv, pv):
      # normal variable
      self.nv = nv
      # private variable(not really)
      self.__pv = pv
# creating an instance of the class Sample
def main():
    sample = Sample('Normal variable', 'Private variable')
# accessing *nv*
    print(sample.nv)
# accessing *__pv** using _Sample__pv name
    print(sample._Sample__pv)
if __name__ =="__main__":
    main()

