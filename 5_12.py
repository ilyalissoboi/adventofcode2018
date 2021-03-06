import sys

input_file = '/Users/lissoboi/code/advent_of_code_2018/5_12_input.txt'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

with open(input_file, 'r') as f:
    input_string = f.read()

    def reaction(input):
        verifications = 0
        while True:
            original_input = input
            for letter in alphabet:
                pair = letter + letter.upper()
                reverse_pair = letter.upper() + letter
                input = ''.join(''.join(input.split(pair)).split(reverse_pair))
            if input == original_input:
                verifications += 1
                # go through the entire alphabet for the last time
                if verifications > len(alphabet):
                    return input
            else:
                verifications = 0
        return ''

    def reaction_mk2(input):
        min_length = sys.maxint
        min_product = ''
        for letter in alphabet:
            shortened_input = ''.join(''.join(input.split(letter)).split(letter.upper()))
            shortened_product = reaction(shortened_input)
            if len(shortened_product) < min_length:
                min_length = len(shortened_product)
                min_product = shortened_product
        return min_product

    product = reaction_mk2(input_string)
    print len(product) - 1
