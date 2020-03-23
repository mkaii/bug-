import nltk
from nltk.tokenize import word_tokenize

tokens = word_tokenize( input() )
tagged = nltk.pos_tag(tokens)

print (tagged)


#import re
#string = input()
#transformed = re.sub(r'\b(?:not|never|no)\b[\w\s]+[^\w\s]', 
#       lambda match: re.sub(r'(\s+)(\w+)', r'\1NEG_\2', match.group(0)), 
#       string,
#       flags=re.IGN
# ORECASE)
#print (transformed)
#
#tokens = word_tokenize( string )
#print(nltk.pos_tag(tokens))