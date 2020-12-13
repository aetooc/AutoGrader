## IMPORTS GO HERE
import os
## END OF IMPORTS


#### YOUR CODE FOR text_count FUNCTION GOES HERE ####
def text_count(directory, filename, third=0, fourth=0):
    filepath=os.path.join(directory, filename)
    count=0
    with open (filepath, 'r') as i:
        A=len(i.read().strip().split())
    if third!=True and fourth!=True:
        return A
    if third == True:
        with open(filepath,'r') as f:
                for line in f: 
                    line=line.split()
                    for word in line:
                        if word.islower() == True:
                            count+=1
    if third == True:
        return count
    if fourth ==True and third ==False:
        with open(filepath,'r') as f:
            if fourth == True:
                B=len(f.read())
    return B

#### End OF MARKER

#### YOUR CODE FOR copy_lines FUNCTION GOES HERE ####
def copy_lines(input1, output1, number):
    filepath=os.path.join('.', input1)
    filepath1=os.path.join('.', output1)
    counter = 0
    with open(filepath, 'r') as f:
        with open(filepath1, 'w')as k:
            for line in f:
                counter += 1
                if counter == number:
                    k.write(line.strip())
                else:
                    k.write(line)
                if counter == number:
                    break
    
    

#### End OF MARKER



