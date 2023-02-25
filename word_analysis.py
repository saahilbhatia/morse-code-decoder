# Task 3: Building a class for analysing decoded words
class WordAnalyser:
    def __init__(self):
        self.dict = dict()

    def __str__(self):
        output_str = ''
        output_str = 'Word  :  Count' + '\n'

        for word, count in self.dict.items():
            output_str += str(word) + '  :  ' + str(count) + '\n'

        return output_str

    def analyse_words(self, decoded_sequence):

        # Removing punctuation marks
        unwanted_char = ['.', ',', '?']
        i = 0
        while i < len(decoded_sequence):
            if decoded_sequence[i] in unwanted_char:
                decoded_sequence = decoded_sequence.replace(decoded_sequence[i], '')
            i += 1

        dec_seq_list = decoded_sequence.split(' ')
        if '' in  dec_seq_list:
            for each in dec_seq_list:
                if each == '':
                    dec_seq_list.remove('')
        # Creating a set of words in the decoded sequence
        dec_seq_set = set(dec_seq_list)

        # Counting occurrences of each word in the decoded sequence
        dec_seq_deduped = list(dec_seq_set)
        dec_seq_deduped.sort()
        count_list = []
        for i in range (len(dec_seq_deduped)):
            count = dec_seq_list.count(dec_seq_deduped[i])
            count_list.append(count)

        # Combining the word and count list & returning it
        for i in range(len(dec_seq_deduped)):
            self.dict[dec_seq_deduped[i]] = count_list[i]

        return self

def main():
    word_analyser_mc = WordAnalyser()
    # print(word_analyser_mc)


if __name__ == "__main__":
    main()

