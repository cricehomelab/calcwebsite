from cgitb import text
import math
from turtle import textinput

def evaluation_prep(text):
    #print("hello")
    text = text.split("√")
    #print(text)
    if len(text) == 2:
        #print('hello')        
        text.insert(1, "math.sqrt")
        text = ''.join(text)
        #print(text)
    else:    
        #print(f'len of list {len(text)}') 
        num_of_splits = len(text) -1
        #print(f"num of splits {num_of_splits}")
        while num_of_splits > 0:
            #print(num_of_splits)
            text.insert(num_of_splits, "math.sqrt")
            num_of_splits -= 1            
        text = ''.join(text)
        #print(text)
    
    return text

'''
text = evaluation_prep('√(9)+√(9)')
print(text)
print(str(eval(text)))
'''


