from textblob import TextBlob
import nltk
from textblob import Word
import sys


def parse(string):
    """
    Parse a paragraph. Devide it into sentences and try to generate quesstions from each sentences.
    """
    output = []
    try:
        txt = TextBlob(string)
        # Each sentence is taken from the string input and passed to genQuestion() to generate questions.
        for sentence in txt.sentences:
            output = genQuestion(sentence)

        return output
    except Exception as e:
        raise e


def genQuestion(line):
    """
    outputs question from the given text
    """

    if type(line) is str:  # If the passed variable is of type string.
        line = TextBlob(line)  # Create object of type textblob.blob.TextBlob

    bucket = {}  # Create an empty dictionary

    for i, j in enumerate(line.tags):  # line.tags are the parts-of-speach in English
        if j[1] not in bucket:
            bucket[j[1]] = i  # Add all tags to the dictionary or bucket variable

    if verbose:  # In verbose more print the key,values of dictionary
        print('\n', '-' * 20)
        print(line, '\n')
        print("TAGS:", line.tags, '\n')
        print(bucket)

    question = ''  # Create an empty string

    # These are the english part-of-speach tags used in this demo program.
    # .....................................................................
    # NNS     Noun, plural
    # JJ  Adjective
    # NNP     Proper noun, singular
    # VBG     Verb, gerund or present participle
    # VBN     Verb, past participle
    # VBZ     Verb, 3rd person singular present
    # VBD     Verb, past tense
    # IN      Preposition or subordinating conjunction
    # PRP     Personal pronoun
    # NN  Noun, singular or mass
    # .....................................................................

    # Create a list of tag-combination

    l1 = ['NNP', 'VBG', 'VBZ', 'IN']
    l2 = ['NNP', 'VBG', 'VBZ']

    l3 = ['PRP', 'VBG', 'VBZ', 'IN']
    l4 = ['PRP', 'VBG', 'VBZ']
    l5 = ['PRP', 'VBG', 'VBD']
    l6 = ['NNP', 'VBG', 'VBD']
    l7 = ['NN', 'VBG', 'VBZ']

    l8 = ['NNP', 'VBZ', 'JJ']
    l9 = ['NNP', 'VBZ', 'NN']

    l10 = ['NNP', 'VBZ']
    l11 = ['PRP', 'VBZ']
    l12 = ['NNP', 'NN', 'IN']
    l13 = ['NN', 'VBZ']


    #Applying
    l14 = ['NNP', 'NN']
    l15 = ['NNP']
    l16 = ['NNP', 'NN', 'CC']
    l17 = ['NNP', 'NN' ,'VBZ', 'JJ']
    l18 = ['NNS', 'CC', 'VBP', 'NNP', 'NN']

    output = []

    # With the use of conditional statements the dictionary is compared with the list created above
    #Applying: Solve, Show, Use, Illustrate, Construct, Complete, Examine, Classify

    #Applying
    if all(key in bucket for key in l14):  # 'NNP', 'NN' in sentence.
        question = 'How can you apply' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[bucket['NN']] + ' '\
                   + 'approach in project development' + '?'
        print('\n', 'Question: ' + question)
        output.append(question)

    if all(key in bucket for key in l15):  # 'NNP' in sentence.
        question = 'Do you know' + ' ' + line.words[bucket['NNP']] + ' ' + '?'
        print('\n', 'Question: ' + question)
        output.append(question)

    if all(key in bucket for key in l16):  # 'NNP', 'NN in sentence.
        question = 'Can you illustrate the' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[bucket['NN']] + ' ' + 'process' + '?'
        print('\n', 'Question: ' + question)
        output.append(question)

    if all(key in bucket for key in l17):  # 'NNP', 'NN', 'VBZ' in sentence.
        question = 'Show how' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[bucket['NN']] + ' ' +'development' +  ' ' + line.words[bucket['VBZ']] +\
                  ' ' + line.words[bucket['JJ']] +'.'
        print('\n', 'Question: ' + question)
        output.append(question)

    if all(key in bucket for key in l18):  # 'NNS', 'CC', 'VBP' in sentence.
        question = 'Solve how' + ' ' + line.words[bucket['NNS']] + ' ' + line.words[bucket['CC']] + ' ' +'solutions' +  ' ' + line.words[bucket['VBP']] +\
                  ' ' + 'in' + ' ' + line.words[bucket['NNP']] + ' ' + line.words[bucket['NN']] + ' ' + 'development' + '.'
        print('\n', 'Question: ' + question)
        output.append(question)

 
    return output

def main(textinput):
    """
    Accepts a text file as an argument and generates questions from it.
    """
    # verbose mode is activated when we give -v as argument.
    global verbose
    verbose = True

    print('\n-----------INPUT TEXT-------------\n')
    print(textinput, '\n')
    print('\n-----------INPUT END---------------\n')

    # Send the content of text file as string to function parse()
    return parse(textinput)


if __name__ == "__main__":
    main()