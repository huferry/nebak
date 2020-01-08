# import csv

# with open('example.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     for row in csv_reader:
#         print(row)

def normalize(quotes):
    '''
    Normalize quotes will turn the first element in the list
    into 1 and divides the rest of the elements by this first
    value.

    This function will return a list with the same size of the 
    given quotes.
    '''
    if len(quotes) == 0 or quotes[0]==0:
        return []

    return list(map(lambda x: x / quotes[0], quotes))

