import sys
from .classmodule import MyClass
def main():
    args = sys.argv[1:]
    my_object = MyClass(args)
    my_object.Regression()
if __name__ == '__main__':
    main()