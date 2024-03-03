import sys

result_sys = sys.argv
result_list = result_sys[1:]

a = int(result_list[0])
b = int(result_list[1])
# a = int(input("Enter number: "))
# b = int(input("Enter number: "))

if "+" in result_list:

    def average_num(a, b):
        """
        average_num func()
        :param a: int
        :param b: int
        :return: average_num a, b
        """
        result = (a + b)/2
        return result

    print("Result average: ", average_num(a, b))
elif "-" in result_list:

    def subtraction(a, b):
        """
        subtraction func()
        :param a: int
        :param b: int
        :return: subtraction a, b
        """
        result = a - b
        return result


    # new = subtraction.__doc__
    # global new
    print("Result subtraction: ", subtraction(a, b))

elif '-h' or '--help' in result_list:
    def subtraction(a, b):
        """
        subtraction func()
        :param a: int
        :param b: int
        :return: subtraction a, b
        """
        pass

    print(subtraction.__doc__)

