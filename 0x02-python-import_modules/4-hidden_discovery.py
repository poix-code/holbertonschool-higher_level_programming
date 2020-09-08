#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for count in dir(hidden_4):
        if count[:2] != '__':
            print(count)
