from alphabet import morse_to_letter, letter_to_morse

# SOS message
morse_code = ['...', '---', '...', '"', '...', '---', '...']
print('morse code: {}'.format(morse_code))


# Morse decoder function
def morse_decoder(row):
    return ''.join([morse_to_letter[i] for i in row])


# Morse decoder class
class MorseDecoder:
    def __init__(self, row):
        self.decoded_row = self.decode(row)

    # decoder
    def decode(self, row):
        return ''.join([morse_to_letter[i] for i in row])

    # encoder
    def encode(self, row):
        return [letter_to_morse[i] for i in row]

    # operator overloading
    def __eq__(self, other):
        # comparison of string and morse code
        if type(other) == list:
            return self.decoded_row == self.decode(other)
        # two string comparison
        else:
            first_string = self.decoded_row.replace('_', '')
            second_string = other.replace('_', '')
            return first_string == second_string


# decode SOS message using function
print('decoded row: {}'.format(morse_decoder(morse_code)))

# decode SOS message using object
obj = MorseDecoder(morse_code)
decoded_row = obj.decoded_row
print('decoded row: {}'.format(decoded_row))

# encode SOS message using object
encoded_row = obj.encode(decoded_row)
print('encoded row: {}'.format(encoded_row))

new_morse_code = ['---', '...', '.--.']

print('SOS_SOS and morse code:', obj == morse_code)
print('SOS_SOS and new morse code:', obj == new_morse_code)
print('SOS_SOS and SOS_SOS:', obj == 'SOS_SOS')
print('SOS_SOS and ___SOS_____SOS____:', obj == '___SOS_____SOS____')
print('SOS_SOS and OK:', obj == 'OK')
