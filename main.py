def print_number_of_types_of_beers_to_buy(types_of_beers):
    print(len(types_of_beers))
    f = open('output.txt', 'x')
    f.write(str(len(types_of_beers)))


if __name__ == '__main__':
    results = []

    # reading the file with input and giving data from it to variables

    file = open('input.txt')
    line = file.read()
    num_of_workers = line.split('\n')[0].split(' ')[0]
    max_num_of_types_of_beers = line.split('\n')[0].split(' ')[1]
    answers = line.split('\n')[1].split(' ')

    # calling the method that returns the list of beers that is the one that persons love ( they must be in our output)

    print_number_of_types_of_beers_to_buy(results)
