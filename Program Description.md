# n-grams

The program designs and implements a Python program called ngram.py that learns an N-gram language model from the text files in the text data directory. The program generates a sentences based on the N-gram model. The program works for any value of N, and outputs sentences. Before learning the N-gram model, I converted all text to lower case, and included punctuation in the n-gram models. I also separated punctuation from words before learning the N-gram model. The program learns a single n-gram model from any number of input files. As a benchmark for performance, this program is able to generate results for a trigram model(n=3) based on 1,000,000 words (tokens) of text in under 5 minutes. The program runs as follows:

#### *ngram.py n m input-file/s*

n and m are integer values, and input-files is a list of file names that contain the text you are building your ngram model from. For instance:

*ngram.pl 3 10 pg2554.txt pg2600.txt pg1399.txt*

This command results in 10 randomly generated sentences based on a tri-gram model learned from the text files text file in the text data directory.
