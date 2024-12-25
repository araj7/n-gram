# N-Gram Sentence Generator

## Overview
This project implements an N-gram language model that generates sentences based on the text data provided. Using a Python script, the program processes input files to build an N-gram model, which it then uses to create randomized, grammatically consistent sentences. The tool supports any N-gram size, making it highly versatile for various language modeling tasks.

## Key Features
- **Dynamic N-Gram Support:** Works for any value of N.
- **Input Flexibility:** Processes one or multiple text files to create a unified language model.
- **Random Sentence Generation:** Produces coherent sentences using probabilistic methods.
- **Optimized Performance:** Generates results for a trigram model (N=3) on 1,000,000 words in under 5 minutes.
- **Preprocessing:** Cleans and tokenizes text, handling punctuation and casing.

## How It Works
1. **Input:** Provide text files and specify N (size of the N-gram) and the number of sentences to generate.
2. **Preprocessing:** Converts text to lowercase, tokenizes sentences and words, and separates punctuation.
3. **Model Building:** Constructs N-grams and calculates frequency distributions.
4. **Sentence Generation:** Uses probabilities (e.g., Simple Good-Turing smoothing) to create sentences based on the learned model.

## Usage
Run the program from the command line:

```bash
python ngram.py <n> <m> <input-file1> <input-file2> ...
```

- `<n>`: Size of the N-gram.
- `<m>`: Number of sentences to generate.
- `<input-file(s)>`: Text files to train the N-gram model.

### Example
To generate 10 sentences using a trigram model from three text files:

```bash
python ngram.py 3 10 pg2554.txt pg2600.txt pg1399.txt
```

## Dependencies
Ensure the following Python libraries are installed:
- `nltk`
- `re`
- `collections`
- `sys`

Install dependencies using pip:

```bash
pip install nltk
```

## Repository Structure
- `n_grams.py`: Main script for building the N-gram model and generating sentences.
- `data/`: Directory for storing input text files.
- `output/`: Stores generated sentences (if configured to save).

## Technical Details
### Preprocessing Steps
- Converts text to lowercase.
- Tokenizes sentences and words.
- Appends `<start>` and `<end>` tags for modeling.
- Ensures sufficient corpus size (>100,000 words).

### Modeling and Generation
- **N-Gram Construction:** Builds N-grams from tokenized text.
- **Frequency Analysis:** Uses `collections.Counter` for frequency distribution.
- **Smoothing:** Applies Simple Good-Turing smoothing for probability estimation.
- **Random Sentence Generation:** Iteratively selects words based on N-gram probabilities.

## Performance
Efficiently processes large datasets and generates sentences within minutes. The script ensures scalability for extensive corpora.

## References
- [Markov Chains for NLP](http://www.samansari.info/2016/01/generating-sentences-with-markov-chains.html)
- [N-Grams in Python](https://stackabuse.com/python-for-nlp-developing-an-automatic-text-filler-using-n-grams/)
- [IBM AI Patterns](https://developer.ibm.com/technologies/artificial-intelligence/articles/cc-patterns-artificial-intelligence-part3/)
- [N-Gram Generator GitHub](https://github.com/aduroy/n-gram-generator)

## Acknowledgments
Special thanks to open-source contributors and resources that supported this project.

