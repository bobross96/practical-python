import os 

os.getcwd()

with open('foo.txt','wt') as file:
    # both seems to do the same thing 
    file.write('asdasd\n') 
    print('Hellow world',file=file)

