''' 
Description of the Program:
The program is used to decode Morse code sequences that represent words and sentences in English.
The dots, dashes and spaces are represented by 0, 1 and '*' respectively. Each character represented
by the Morse Code system is separated by a single space, and each word is separated by three spaces.
The program decodes the sequences and displays the decoded message. If there is an error in any sequence,
the program displays an error. Note that the input sequence also has other requirements: it should
have at least one set of three '***' and should terminate with a punctuation mark. If there was no error in
the input sequence, after displaying the decoded message, the program shows a menu asking the user for the
level of analysis of the decoded message. The different levels for analyses are characters, words and sentences.
Based on the level selected by the user, the program displays the occurrences of each character / word /
type of sentence. Please read the user documentation for more details on the calculation of the types of
sentences, and in general complete details with instructions for running the program.
'''

# Task 5: Putting all the classes together
from decoder import Decoder
from character_analysis import CharacterAnalyser
from word_analysis import WordAnalyser
from sentence_analysis import SentenceAnalyser

# Defining functions to receive input sequence, decode the input sequence, and analyse the different counts

def decoding_sequence(morse_code_sequence):
    mc_dict = Decoder()
    decoded_sequence = mc_dict.decode(morse_code_sequence)
    return decoded_sequence

def char_analyse(decoded_sequence):
    char_dict = CharacterAnalyser()
    char_count_output = char_dict.analyse_characters(decoded_sequence)
    return char_count_output

def word_analyse(decoded_sequence):
    word_dict = WordAnalyser()
    word_count_output = word_dict.analyse_words(decoded_sequence)
    return word_count_output

def sent_analyse(decoded_sequence):
    sent_dict = SentenceAnalyser()
    sent_count_output = sent_dict.analyse_sentences(decoded_sequence)
    return sent_count_output

def receive_input_seq():
    # Taking multiple lines with Morse Code sequences from the user
    morse_code_sequence = ''
    while True:
        temp = input('Please enter the Morse Code sequences with a minimum of one set of '
                     '3 consecutive "*" to be decoded:   ')
        if temp:
            morse_code_sequence += temp + '***'
        else:
            break
    return morse_code_sequence

def main():
    morse_code_sequence = receive_input_seq()
    # Decoding the sequencing and printing to the console
    decoded_sequence = decoding_sequence(morse_code_sequence)

    if 'Error' in decoded_sequence or 'Error' in decoded_sequence:
        error_flag = 1
    else:
        error_flag = 0

    if error_flag == 0:
        print('The decoded sequence is : ', decoded_sequence)
    else:
        print(decoded_sequence)

    if error_flag == 0:
        # Menu for selecting words, characters and sentences analyses
        menu_option = input('Please enter one of the following options for analysis:  ' + '\n' +
                            '1 for Characters' + '\n' + '2 for Words' + '\n' + '3 for Sentences'
                            + '\n' + '0 to exit' + '\n')

        while menu_option != '0':
            if menu_option == '1':
                char_output = char_analyse(decoded_sequence)
                print(char_output)
            elif menu_option == '2':
                word_output = word_analyse(decoded_sequence)
                print(word_output)
            elif menu_option == '3':
                sent_output = sent_analyse(decoded_sequence)
                print(sent_output)
            else:
                print('Invalid menu option')

            menu_option = input('Please enter one of the following options for analysis:  ' + '\n' +
                                '1 for Characters' + '\n' + '2 for Words' + '\n' + '3 for Sentences'
                                 + '\n' + '0 to exit' + '\n')

    if error_flag == 0:
        print('Thank You!')

if __name__ == "__main__":
    main()
