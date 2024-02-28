#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    #orderly prints all name as registered and defined by the above import.
    for name in sorted(dir(hidden_4)):
        # prints names that dont start with undercase.
        if name[:2] != '__':
            print("{}".format(name))