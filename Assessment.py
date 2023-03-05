import nltk
from nltk.tokenize import word_tokenize

test_responses = ['I shared your email',
'I just shared your address',
"I've sent your email address to my friend",
"I've shared your email",
'I already shared email',
"I've just shared your address",
'Okay I have shared the email',
'I have shared your email',
'I did share your email',
'I shared your contacts',
'I shared your digits',
'I shared your contact details',
'I shared your contact card',
'I shared the email with my friends',
'I have sent this email to my friends',
'The email has been shared with all my friends',
'Can I share your email address',
'May I share your email',
'Might I share your email',
'Could we share your email address with my friends',
'Can I share your email with my friend',
'Can I send your email to my friend',
'Can I give your contacts with my friend?']

stemmer =  nltk.stem.snowball.SnowballStemmer('english')       # instanciated stemmer

def shared_or_not(sentence):

    group = 'This sentence does not have both share and email'
    first_words = ['can', 'may','might', 'could'] # keywords to look for in a sentence
    second_words = ['i', 'we']                     # keywords to look for in a sentence

    sentence_tokens = word_tokenize(sentence.lower())# Turns sentence to a token and lowercase

    sentence_stems = []                              # created an empty list
    for token in sentence_tokens:                    # a loop to stem tokens
        tokens = stemmer.stem(token)
        sentence_stems.append(tokens)
    
    if 'share' in sentence_stems and 'email' in sentence_stems:
        for stem in sentence_stems:
            if stem[0] in first_words and stem[1] in second_words:
                group = 'Student has shared' 
            else:
                group = 'Student wants to know if can share'

    return group
                    
        
print(shared_or_not('I shared the email with my friends'))     #testing with a sentence

for sentence in test_responses:                              # testing with list of sentences
    print(sentence,'\t', shared_or_not(sentence),'\n')





