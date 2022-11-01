from cgitb import text
import math
from turtle import textinput


def squareroot_account(text):    
    text = text.split("√")
    
    if len(text) == 2:               
        text.insert(1, "math.sqrt")
        text = ''.join(text)        
    else:
        num_of_splits = len(text) -1 
        while num_of_splits > 0:            
            text.insert(num_of_splits, "math.sqrt")
            num_of_splits -= 1            
        text = ''.join(text)
    return text

def pi_account(text):
    if text == "π":
        return math.pi
    
    text = text.split("π")
    if len(text) == 2:               
        text.insert(1, "math.pi")
        text = ''.join(text)  
    else:
        num_of_splits = len(text) -1 
        while num_of_splits > 0:            
            text.insert(num_of_splits, "math.pi")
            num_of_splits -= 1            
        text = ''.join(text)

    return text

def evaluation_prep(text):
    text = squareroot_account(text)  
    text = pi_account(text) 



    return text

def solution(solve):
    text = evaluation_prep(solve)           
    if text:            
        try:
            solution = str(eval(text))
            return solution                
        except:
            return "error"



