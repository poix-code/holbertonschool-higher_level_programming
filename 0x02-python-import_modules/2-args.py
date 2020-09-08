#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("{} argument:".format(argc))
        print("{}: {}".format(argc, argv[argc]))
    else:
        print("{} arguments:".format(argc))
        for count in range(1, argc + 1):
            print("{}: {}".format(count, argv[count]))
