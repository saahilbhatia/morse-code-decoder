
# Task 4: Building a class for analysing decoded sentences
class SentenceAnalyser:
    def __init__(self):
        self.dict = dict()

    def __str__(self):
        output_str = ''
        output_str = 'Sentence  :  Count' + '\n'

        for sentence, count in self.dict.items():
            output_str += str(sentence) + '  :  ' + str(count) + '\n'

        return output_str

    def analyse_sentences(self, decoded_sequence):

        # Counting number of punctuations and adding them to the dictionary

        count_periods = decoded_sequence.count('.')
        count_questions = decoded_sequence.count('?')

        self.dict['Complete Sentences'] = count_periods
        self.dict['Questions'] = count_questions

        # Counting clauses
        # Creating a list of punctuations present in the decoded sequence
        punc_char_list = [',', '.', '?']
        decoded_seq_punct = []

        for each in decoded_sequence:
            if each in punc_char_list:
                decoded_seq_punct.append(each)

        # Counting the number of clauses, taking into account the number of consecutive commas.
        # For Ex: The weather is great, but I am working on the assignment. Result should be 2 clauses.
        # For Ex: A, B, C, D and E are good friends. Result should be 5 clauses.
        count_clauses = 0
        # Checking for consecutive commas and counting number of clauses
        if ',' in decoded_seq_punct:
            i = 0
            while i < len(decoded_seq_punct) - 1:
                inc_counter = 1
                if decoded_seq_punct[i] == ',':
                    count_clauses += 2
                    for j in range(i, len(decoded_seq_punct) - 1):
                        if decoded_seq_punct[j] == decoded_seq_punct[j + 1]:
                            inc_counter += 1
                            count_clauses += 1
                        else:
                            break
                i += inc_counter

            if decoded_seq_punct[len(decoded_seq_punct) - 2] != ',' and \
               decoded_seq_punct[len(decoded_seq_punct) - 1] == ',':
                count_clauses += 1

            # If there are only comma punctuation marks, the count needs to decreased by 1
            if '?' not in decoded_seq_punct or '.' not in decoded_seq_punct:
                count_clauses -= 1

            # Special case if there is only sentence ending with a comma
            if len(decoded_seq_punct) == 1:
                count_clauses = 1

        self.dict['Clauses'] = count_clauses
        return self


def main():
    sent_analyser_mc = SentenceAnalyser()
    # print(sent_analyser_mc)


if __name__ == "__main__":
    main()
