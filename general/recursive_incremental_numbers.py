def printIncrementalNumbers(start, digits, str_out=''):
    if digits == 0:
        print(str_out)
        return

    # number get incremented until 9 :)
    for i in range(start, 10):
        # add digit to the end
        myStr = str_out + str(i)

        printIncrementalNumbers(i + 1, digits - 1, myStr)


printIncrementalNumbers(1, 3)
