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
    

    if type(line) is str:     # If the passed variable is of type string.
        line = TextBlob(line) # Create object of type textblob.blob.TextBlob

    bucket = {}               # Create an empty dictionary


    for i,j in enumerate(line.tags):  # line.tags are the parts-of-speach in English
        if j[1] not in bucket:
            bucket[j[1]] = i  # Add all tags to the dictionary or bucket variable
    
    if verbose:               # In verbose more print the key,values of dictionary
        print('\n','-'*20)
        print(line ,'\n')        
        print("TAGS:",line.tags, '\n')  
        print(bucket)

    # These are the english part-of-speach tags used in this demo program.
    #.....................................................................
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
    #.....................................................................

    # Create a list of tag-combination

    l1 = ['NNP']
    l2 = ['NNP', 'VBG', 'VBZ']
    l3 = ['PRP', 'VBG', 'VBZ', 'IN']
    l4 = ['PRP', 'VBG', 'VBZ']
    l8 = ['NNP', 'VBZ', 'JJ']

    output = []

    # With the use of conditional statements the dictionary is compared with the list created above

    if all(key in  bucket for key in l2): #'NNP', 'VBG', 'VBZ' in sentence.
        question = 'Describe' + ' ' + line.words[bucket['VBG']] +' '+ 'in' +' '+ line.words[bucket['NNP']] + '.'
        output.append(question)
        print('\n', 'Question: ' + question)
    
    if all(key in  bucket for key in l3): #'PRP', 'VBG', 'VBZ', 'IN' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] +' '+ line.words[bucket['PRP']]+ ' '+ line.words[bucket['VBG']] + '?'
        output.append(question)
        print('\n', 'Question: ' + question)
    
    if all(key in  bucket for key in l4): #'PRP', 'VBG', 'VBZ' in sentence.
        question = 'What ' + line.words[bucket['PRP']] +' '+  ' does ' + line.words[bucket['VBG']]+ ' '+  line.words[bucket['VBG']] + '?'
        output.append(question)
        print('\n', 'Question: ' + question)

    if all(key in bucket for key in l8): #'NNP', 'VBZ', 'JJ' in sentence.
        question = 'What' + ' ' + line.words[bucket['VBZ']] + ' ' + line.words[bucket['NNP']] + '?'
        output.append(question)
        print('\n', 'Question: ' + question)

    if all(key in bucket for key in l1): #'NNP'' in sentence.
        question = 'Describe the characteristics of' + ' ' + line.words[bucket['NNP']] + '.'
        output.append(question)
        print('\n', 'Question: ' + question)

    # When the tags are generated 's is split to ' and s. To overcome this issue.
    if 'VBZ' in bucket and line.words[bucket['VBZ']] == "’":
        question = question.replace(" ’ ","'s ")
    
    return output

def main(textinput):  
    """
    Accepts a text file as an argument and generates questions from it.
    """
    #verbose mode is activated when we give -v as argument.
    global verbose 
    verbose = True

    print('\n-----------INPUT TEXT-------------\n')
    print(textinput,'\n')
    print('\n-----------INPUT END---------------\n')

    # Send the content of text file as string to function parse()
    return parse(textinput)


if __name__ == "__main__":
    main()

