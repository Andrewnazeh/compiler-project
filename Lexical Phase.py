#!/usr/bin/env python
# coding: utf-8

# In[4]:


import re
import nltk

input_program = input("Enter Your Code: ");
input_program_tokens = nltk.wordpunct_tokenize(input_program);

print(input_program_tokens);



RE_Keywords ="print|while|False|None|True|and|as|assert|async|await|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|with|yield"
RE_Operators = "(\++)|(-)|(=)|(\*)|(/)|(%)|(--)|(<=)|(>=)"
RE_Numerals = "^(\d+)$"
RE_Special_Characters = "[\[@&~!#$\^\|{}\]:;<>?,\.']|\(\)|\(|\)|{}|\[\]|\""
RE_Identifiers = "^[a-zA-Z_]+[a-zA-Z0-9_]*"





for token in input_program_tokens:
    if(re.findall(RE_Keywords,token)):
        print(token , "-------> Keyword")
    elif(re.findall(RE_Operators,token)):
        print(token, "-------> Operator")
    elif(re.findall(RE_Numerals,token)):
        print(token, "-------> numeric constants")
    elif(re.findall(RE_Special_Characters,token)):
        print(token, "-------> Special Character/Symbol")
    elif(re.findall(RE_Identifiers,token)):
        print(token, "-------> Identifiers")
    else:
        print("Unknown Value")

