if __name__ == "__main__":
    import sys
    #Goes through system to count all arguments and stacks them.
    amount = 0
    for i in range(len(sys.argv) - 1):
        amount += int(sys.argv[i + 1])
    print("{}".format(amount))