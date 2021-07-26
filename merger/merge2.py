
filenames = ['C:/Users/hmdan/Downloads/WS (1)/WS/merger/base.html', 'C:/Users/hmdan/Downloads/WS (1)/WS/merger/ytindex.html']

# Open file3 in write mode
with open('C:/Users/hmdan/Downloads/WS (1)/WS/Youtube.html', 'w') as outfile:
    # Iterate through list
    for names in filenames:
        # Open each file in read mode
        with open(names) as infile:
            # read the data from file1 and
            # file2 and write it in file3
            outfile.write(infile.read())

        # Add '\n' to enter data of file2
        # from next line
        outfile.write("\n")
