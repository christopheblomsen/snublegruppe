"""
Author: Christophe Blomsen

Simple reader of file.txt
"""



with open('file.txt', 'r') as infile:   # how to open for reading
    infile.readline()                   # ´´Reads´´ a line
    for line in infile:                 # Runs throug all lines in file
        line = line.split()             # splits at whitespace and make
                                        # a new list
        ans = 0                         # for sum
        N = 0                           # amount of elements for mean
        for i in range(len(line)-1):    # runs through the list line
            #print(f'Current it is {i+1}')
            ans += float(line[i+1])     # float or eval to convert from string
            N += 1

avg = ans/N
print(f'The average from Lorems are {avg:.2f}')
