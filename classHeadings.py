#This code creates headings for my classes this semester(Fall 2020).
import os
from datetime import date

def choice(var1,fname):
    if var1 in ['a','A']:
        heading('CIS345 - Operating Systems','Jehan Sanmugaraja',fname)
    elif var1 in ['b','B']:
        heading('CIS346 - Ecommerce','Priya Krishnakumar',fname)
    elif var1 in ['c','C']:
        heading('MAT348 - OP Management','Johnny Hellman',fname)
    elif var1 in ['d','D']:
        heading('LEH354 - The Holocoust','Stephen Garrin',fname)
    else:
        print(var1, "is not an option, bro!:(")

def heading(className,professor,fname):
    print('A ' + fname + ' file has been created with a heading in this format:\n')
    today = (date.today())
    bestDate = today.strftime('%m/%d/%y')
    f = open(fname,'w')
    f.write("Diego Marcelino" + "\n" + professor + "\n" + className + "\n" + bestDate)
    f.close()

    f = open(fname, 'r')
    print(f.read())
    
os.chdir('/Users/diegomarcelino/OneDrive') #Files will be deposited into my OneDrive
print('What class would you like to make the heading for?')
print('a. CIS345 - Operating Systems\nb. CIS346 - Ecommerce\nc. MAT348 - OP Management\nd. LEH354 - The Holocoust\n')
var1 = input('Please enter a letter choice: ')
fname = input('What would you like to name your file? ')

choice(var1,fname)
