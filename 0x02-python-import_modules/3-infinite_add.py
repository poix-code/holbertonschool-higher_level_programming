#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv) - 1
    tmp = 0
    count = 1
    if argc == 0:
        print(tmp)
    else:
        while count < argc + 1:
            tmp += int(argv[count])
            count += 1
        print(tmp)
