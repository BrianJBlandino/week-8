# importing necessary libaries
from collections import defaultdict
import streamlit as st
import numpy as np
import random

class MarkovText:
    ''' Creating a class MarkovText that will have functions
    that will return a dictionary of key: value paris of
    words as tokens and states of a corpus.'''
    
    def __init__(self, corpus):
        '''Creating a function assigning a corpus and
        ensuring each key automatically has a list as
        its value.'''
        
        self.corpus = corpus
        self.term_dict = defaultdict(list)

    def get_term_dict(self):
        '''Creating a function that will tokenize over the
        words and build the term dictionary'''
        
        # assigning the words variable to a list of corpus terms
        words = self.corpus.split()
        
        # iterate over the words and build the term dictionary
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            self.term_dict[current_word].append(next_word)
        
        # return the term dictionary
        return self.term_dict

    def generate(self, seed_term=None, term_count=15):
        '''Creating a function that will generate sentences
        using the Markov property.'''
        
        # ensuring the term_dict has been populated
        if not self.term_dict:
            self.get_term_dict()
        
        # validating seed term if it is provided
        if seed_term and seed_term not in self.term_dict:
            raise ValueError(f"The seed term '{seed_term}' is not in the term dictionary.")
        
        # starting with the seed_term or pick a random starting word
        current_word = seed_term or random.choice(list(self.term_dict.keys()))
        sentence = [current_word]
        
        # generating the sentence
        for _ in range(term_count - 1):
            followers = self.term_dict[current_word]
            if not followers:
                break
            current_word = random.choice(followers)
            sentence.append(current_word)
        
        # returning the generated sentence
        return ' '.join(sentence)
    
# setting the corpus to the example in the exercise
corpus = (
    "Healing comes from taking responsibility: to realize that it is you - and no one else - "
    "that creates your thoughts, your feelings, and your actions."
)

# creating a MarkovText object
text_gen = MarkovText(corpus)

# building the term dictionary
term_dict = text_gen.get_term_dict()

# returning the term dictionary
term_dict

# testing the function
text_gen.get_term_dict()

# testing the function
text_gen.generate(term_count=10)

st.write('Including duplicates would not add to the overall understanding \
         of the sentence or structure from the tokenizing of the corpus.')