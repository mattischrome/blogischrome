#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 4 11:49:00 2022

@author: matt
"""

# import spacy and the downloaded en_core_web_sm pre-trained model
import spacy
import en_core_web_lg
from collections import Counter
import frontmatter

""" # import yaml for ease of handling the blog posts
import yaml """

'''
For each file in the `\_posts` folder read in everything after the second instance of `---` (or use a yaml parsing package) and pass it through SpaCy large language model to get the named entities. Put all the entities of each type into a frequency dictionary corresponding to that type. Ideally the dictionary for each type is added to as we pass through each file. Failing that we can have a list of dictionaries for each type and smoosh it all together later. 
'''

nlp = spacy.load("en_core_web_lg")

# Try reading in one markdown file for now
with open("./_posts/2021-08-02-jab-two.markdown") as f:
    post = frontmatter.loads(f.read())

#print(post)

# Apply the pre-trained model to the raw text string to extract named entities
article = nlp(post.content.strip())

# Build a frequency dictionary of the article
# First a list of strings
ent_list = []
for ent in article.ents:
    ent_list.append(str(ent))
    print(ent.label_)

fd = {ent: ent_list.count(ent) for ent in ent_list}

print(fd)

ten_most_common = Counter(ent_list).most_common(10)
print(ten_most_common)
