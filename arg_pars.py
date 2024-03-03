# import sys
#
# print(sys.argv)
#
# if sys.argv[-1] == '--help':
#     print("Help information!")
# else:
#     print("Read Usage")

import argparse

def arg_func():
    parser = argparse.ArgumentParser("Some name")
    parser.add_argument('massage', help='Type your message')
    parser.add_argument('count', help='How often do you go to shop', type=int)
    parser.add_argument('-u', help="Some help text", action='store_false')
    args = parser.parse_args()
    print(args)
    print(args.massage, args.count)
    print(args.u)

    for i in range(args.count):
        if args.u:
            print(args.massage.upper())
        else:
            print(args.massage)





if __name__ == "__main__":
    arg_func()