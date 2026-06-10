# Write a program to fill in a letter template given below with name and date. 
from datetime import date

name = input("Enter your name: ")
today = str(date.today())
  
letter = '''  
       Dear <|Name|>, 
       You are selected! 
       <|Date|> 
        ''' 
        
print(letter.replace("<|Name|>", name). replace("<|Date|>",today))        

        
        