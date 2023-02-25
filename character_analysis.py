# Task 2: Building a class for analysing decoded characters
class CharacterAnalyser:
    def __init__(self):
        self.dict = dict()

    def __str__(self):
        output_str = ''
        output_str = 'Character  :  Count' + '\n'

        for char, count in self.dict.items():
            output_str += str(char) + '  :  ' + str(count) + '\n'

        return output_str

    def analyse_characters(self, decoded_sequence):
        # Removing spaces and punctuation marks
        unwanted_char = [' ', '.', ',', '?']
        for char in decoded_sequence:
            if char in unwanted_char:
                decoded_sequence = decoded_sequence.replace(char, '')

        # Creating a set of characters in the decoded sequence
        dec_seq_list = []
        for char in decoded_sequence:
            dec_seq_list.append(char)

        dec_seq_set = set(dec_seq_list)

        # Counting occurrences of each character in the decoded sequence
        dec_seq_deduped = list(dec_seq_set)
        dec_seq_deduped.sort()
        count_list = []
        for i in range (len(dec_seq_deduped)):
            count = dec_seq_list.count(dec_seq_deduped[i])
            count_list.append(count)

        # Combining the char and count list & returning it
        for i in range(len(dec_seq_deduped)):
            self.dict[dec_seq_deduped[i]] = count_list[i]

        return self


def main():
    char_analyser_mc = CharacterAnalyser()
    # print(char_analyser_mc)


if __name__ == "__main__":
    main()