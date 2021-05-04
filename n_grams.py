# Amit Raj, Rakesh Subramani Kaleeshwaran, Abinash Vasudevan**

# **Description**

# The problem that we are looking to solve with this program is to generate random sentences from
# tokenized words retrieved from multiple text files.
 
# **Workflow**

#    Step 1  : Read the text data, read the other arguments that are needed.
#    Step 2  : Preprocess the data and calculate the words in the corpus, if less number of words then exit telling  more words are needed.
#    Step 3  : Generate the n-gram word corpus and then calcuate the frequency's using Counter.
#    Step 4  : If the ngram is 1 go to one_Gram_sentence_generator and if ngram is greater than 1 go to ngram_Sentence_generator
#    Step 5  : For loop to iterate in the range of number of sentences needed, form the n-1grams corpus needed accordingly.
#    Step 6  : Calculate the frequency distribution, Simple-turing smoothened probability distribution for the n and n-1 grams.
#    Step 7  : Generate the sentences using generate which chooses random word as the first word.
#    Step 8  : Repeat till the number of sentence is achieved.


## References:
## http://www.samansari.info/2016/01/generating-sentences-with-markov-chains.html 
## https://stackabuse.com/python-for-nlp-developing-an-automatic-text-filler-using-n-grams/
## https://developer.ibm.com/technologies/artificial-intelligence/articles/cc-patterns-artificial-intelligence-part3/
## https://stackoverflow.com/questions/1150144/generating-random-sentences-from-custom-text-in-pythons-nltk
## https://github.com/aduroy/n-gram-generator/blob/master/src/n_gram_model.py


import sys
import time
import re
import nltk
import pip
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter
from nltk.probability import FreqDist, SimpleGoodTuringProbDist


### Preprocess steps which removes the ?., from the right side of the text alone and keeping
### leaving the other ones without any replace, replacing multiple spaces with just a single space
### removing new lines and keeping the whole data in a single line. Sentence tokenizing 
### word tokenizing.

def preprocess_text(total_text, ngrams):
    total_text = total_text.lower()

    ### 
    pattern_1 = '\r\n'
    pattern_2 = '\r +'
    pattern_3 = 'r[^a-z0-9]\n,]'

    ###
    total_text = re.sub(pattern_1, " ", total_text.rstrip())
    total_text = re.sub(pattern_2, " ", total_text)
    total_text = re.sub(pattern_3, "", total_text)

    ## Sentence tokenizing the collected and merged data 

    sentences = sent_tokenize(total_text)

    #### Appending start and end tag and then checking for if there is sufficient number of words
    ### in the corpus created

    word_tokens,total_token_list = [],[]

    #word_tokens = [word_tokenize(sent) for sent in sentences]

    for sent in sentences:
        word_tokens = word_tokenize(sent)
        if (len(word_tokens) >= int(ngrams)):
            for i in range(int(ngrams)-1):
                word_tokens.insert(0, "<start>")
            word_tokens.append("<end>")
            total_token_list.append(word_tokens)
    
    return total_token_list


### checking the word token length of the preprocessed data whether it has a corpus less than
### that of 100000 words if so please exit the program and ask for more data.

def check_word_length(data):
    corpus_words = 0
    for word in data:
        corpus_words += len(word)
    if (corpus_words < 100000):
        print("Add more text files, since its enough")
        sys.exit(1)


### Generate list of n_grams for the word list created

def generate_n_grams(word_ngrams,ngrams):
    ngrams_list = list()
    for word_indx in range(len(word_ngrams)-ngrams+1):
        if ngrams == 1:
            ngrams_list.append(word_ngrams[word_indx:word_indx+ngrams][0])
        else:
            ngrams_list.append(tuple(word_ngrams[word_indx:word_indx+ngrams]))
    return ngrams_list


### sentence generator function for the n_grams greater than 1, where iterate through
## the length of the number of sentences needed and creating n-1 grams from the corpus 
### and then calculating the frequency distributions and from that check the simple turing
## probabilities distributions. Then based on that randomly select a start word using generate()


def ngram_sent_generate(n_gram_freq, num_sent, ngrams):
    for num in range(0, num_sent):
        sent_gen = True
        sent_list,answer = (), ""
        j =0
        while(j<int(ngrams)-1):
            sent_list += ('<start>',)
            j+=1
        while sent_gen == True:
            word_dict = {}
            for word_gram,cnt in n_gram_freq.items():
                ix = tuple([word_gram[w] for w in range(len(word_gram)-1)])
                if ix == sent_list:
                    word_dict.update({word_gram[-1]: cnt})
            
            freq_dist = FreqDist(word_dict)

            one_dist = SimpleGoodTuringProbDist(freq_dist)
            
            word_in_sent = one_dist.generate()
            
            if word_in_sent in ['.', '?', "!","<end>"]:
                sent_gen = False
                answer += word_in_sent
                continue
            
            elif word_in_sent in ["," , "''"]:
                answer += word_in_sent
            
            else:
                text = "{word} "
                answer += text.format(word= word_in_sent)
            
            if (len(sent_list) > 0):
                temp = list(sent_list)
                del temp[0]
                temp.append(word_in_sent)
                sent_list = tuple(temp)
            
        print("Sentence {0} : {1}".format(num, answer.capitalize()))



### Function is to generate the sentence if the n_gram is 1, take the unigrams
### from the already created word corpus. Calculate the frequency distribution, 
### probabilities and then generate sentence based on them.


def one_gram_sent_generate(n_gram_freq, num_sent):
    for num in range(0, num_sent):
        sent_gen = True
        sent_list,answer = (), ""
        while sent_gen == True:
            word_dict = n_gram_freq
            
            freq_dist = FreqDist(word_dict)
            
            one_dist = SimpleGoodTuringProbDist(freq_dist)
            
            word = one_dist.generate()
            
            if word in ['.','?','!','<end>']:
                sent_gen = False
                answer += word
                continue
            elif word in [',' , "''"]:
                answer += word
            else:
                text = "{n_word} "
                answer += text.format(n_word= word)
            
            if (len(sent_list) > 0):
                temp = list(sent_list)
                del temp[0]
                temp.append(word)
                sent_list = tuple(temp)
            
        print("Sentence {0} : {1}".format(num, answer.capitalize()))
    

### main function to take the arguments and then have the sequqntial executions of
## all the functions created above one after the other, calculate the time taken and
### then output it.


def main():
    
    starttime = time.time()
    
    if(len(sys.argv[1:])<4):
        print("Insufficient parameters passed")
        sys.exit(0)
        
    ngrams = int(sys.argv[1])
    num_sent = int(sys.argv[2])
    num_of_files = len(sys.argv) - 3
    
    total_text = ''
    cont = ''
    
    for text_files in range(num_of_files, len(sys.argv)):
        with open(sys.argv[text_files], "r",encoding = 'utf-8') as text:
            cont += text.read()
            total_text += cont
        
    total_token_list = preprocess_text(total_text,ngrams)
        
    check_word_length(total_token_list)
    
    word_ngrams = []
    for single in total_token_list:
        for single_word in single:
            word_ngrams.append(single_word)
    
    with_freq_grams= generate_n_grams(word_ngrams, int(ngrams))
    
    n_grams_freq = Counter(with_freq_grams)
    
    if ((ngrams)==1):
        one_gram_sent_generate(n_grams_freq, num_sent)   
    else:
        ngram_sent_generate(n_grams_freq, num_sent, ngrams)
        
    end_time = time.time()
    
    time_Taken = abs(starttime - end_time)
    
    print("Time taken is: {0}".format(time_Taken))


if __name__ == "__main__":
    main()
