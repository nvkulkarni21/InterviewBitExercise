import pandas as pd
import re


def main():
    # Incase you have to take input, please take it from file named 'input' (without quotes) [e.g. cat input]
    # Print your final output to console. Do not redirect to another file.
    # E.g. Suppose the question is to print the content of a file.
    #    Your solution should be 'os.system("cat input")'(without single quotes) instead of 'os.system("cat input > output")'. That's it!
    # Your code starts from here...
    data = pd.read_csv("input", header=None)
    # print(data)
    # (xxx) xxx-xxxx

    with open('input') as f:
        for line in f:
            matchobj1 = re.match("[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$", line)
            matchobj2 = re.match("[(][0-9][0-9][0-9][)] [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$", line)
            if matchobj1:
                #print("OK")
                print(line.replace("\n",""))
            elif matchobj2:
                #print("OK")
                print(line.replace("\n", ""))
            #else:
                #print("NOT OK")
                #print(line)
    return 0


if __name__ == '__main__':
    main()