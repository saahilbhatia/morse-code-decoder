# Task 1: Building a class for Morse Code Decoder
class Decoder:
    def __init__(self):
        self.dict = dict()

        char_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                     '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '?']

        mc_list = ['01', '1000', '1010', '100', '0', '0010', '110', '0000', '00', '0111',
                   '101', '0100', '11', '10', '111', '0110', '1101', '010', '000', '1',
                   '001', '0001', '011', '1001', '1011', '1100', '11111', '01111', '00111',
                   '00011', '00001', '00000', '10000', '11000', '11100', '11110', '010101',
                   '110011', '001100']


        # Keys for the dictionary are Morse Code sequences and values are characters,
        # because the morse code sequences are the input and characters are the ouput
        for i in range(len(mc_list)):
            self.dict[mc_list[i]] = char_list[i]

    def __str__(self):
        output_str = ''
        output_str = '--- Start of Dictionary ---' + '\n'

        for mc, char in self.dict.items():
            output_str += mc + '  :  ' + char + '\n'

        output_str += '--- End of Dictionary ---'
        return output_str

    def decode(self,morse_code_sequence):
        decoded_str = ''
        error_str = ''

        # Removing leading and trailing spaces in the input sequence
        morse_code_sequence = morse_code_sequence.strip('*')

        # Checking for invalid characters in the input sequence, and
        # returning error message if an invalid character is found
        accepted_char = ['0', '1', '*']


        for each in morse_code_sequence:
            if each not in accepted_char:
                error_str += 'Error in translation as the character ' + each + \
                             ' in the input sequence is invalid.'
                return error_str

        # Checking for correct number of spaces (*) between sequences,
        # and returning error message for invalid number of spaces
        error_space_flag = 0
        if morse_code_sequence.count('*') > 1:
            i = 0
            while i < len(morse_code_sequence):
                i = morse_code_sequence.find('*', i, len(morse_code_sequence))

                if i == -1: # No more spaces in the morse_code_sequence
                    break
                # checking for 1 space or 3 consecutive spaces
                if morse_code_sequence[i + 1] != '*':
                    error_space_flag = 0
                elif morse_code_sequence[i + 2] == '*' and morse_code_sequence[i + 3] != '*':
                    error_space_flag = 0
                else:
                    error_space_flag = 1
                    break
                # incrementing 'i' by the number of spaces
                count = 1
                j = i
                while j < len(morse_code_sequence):
                    if morse_code_sequence[j] == morse_code_sequence[j + 1]:
                        count += 1
                        j += 1
                    else:
                        break
                i += count

        if error_space_flag == 1:
            error_str += 'Error in translation due to incorrect number of spaces between sequences. ' \
                         'Note that each character is separated by one space and each word by 3 spaces.'
            return error_str
        # Checking that the input morse code sequence terminates with a punctuation mark
        punc_char_list = ['.', ',', '?']
        punc_mc_list = ['010101','110011', '001100']

        mc_seq_end = morse_code_sequence[-6:]
        if mc_seq_end not in punc_mc_list:
            error_str += 'Error in translation as the Morse Code sequence is not terminating ' \
                         'with a punctuation character.'
            return error_str

        # Decoding the input sequences with valid characters & ending with a punctuation mark

        input_mc_list = morse_code_sequence.split('*')
        # Checking whether elements in the input list are present in the dictionary.
        i = 0
        j = 0
        output = []

        while i < len(input_mc_list):
            if input_mc_list[i] in self.dict.keys():
                output.append(self.dict[input_mc_list[i]])
            # When splitting on '*', of the 3 consecutive '***', 2 stars become null ('') & are added to the list
            elif input_mc_list[i] == '':
                output.append(' ')
            else:
                error_seq_flag = 1
                error_str += 'Error in translation as the sequence ' + str(input_mc_list[i]) + \
                             'has no Morse code translation.'
                return error_str
            i += 1

        decoded_str = decoded_str.join(output)
        # Replace 2 spaces with one space
        decoded_str = decoded_str.replace('  ', ' ')

        # Input sequence should have at least one minimum set of three consecutive '***'
        if ' ' not in decoded_str:
            error_str += 'Error in translation. The input sequence should have at least one set ' \
                         'of three consecutive "***"'
            return error_str

        # Decoded sequence cannot start with a punctuation mark
        if decoded_str[0] in punc_char_list:
            error_str += 'Error in translation as the sentence cannot begin with a punctuation mark'
            return error_str

        # Decoded sequence cannot have two consecutive punctuation marks
        if decoded_str[-2] in punc_char_list: # The last character will be a punctuation mark
            error_str += 'Error in translation as 2 consecutive punctuation marks are not permitted'
            return error_str
        i = 0
        while i < len(decoded_str) - 2: # Already checked last two characters
            if decoded_str[i] in punc_char_list:
                if decoded_str[i + 1] in punc_char_list:
                    error_str += 'Error in translation as 2 consecutive punctuation marks are not permitted'
                    return error_str
                elif decoded_str[i + 1] == ' ' and decoded_str[i + 2] in punc_char_list:
                    error_str += 'Error in translation as 2 consecutive punctuation marks are not permitted'
                    return error_str
            i += 1

        # Return the decoded message
        return decoded_str


def main():
    decoder_mc = Decoder()
    # print(decoder_mc)


if __name__ == "__main__":
    main()














