### YOUR CODE FOR openLocks() FUNCTION GOES HERE ###
def openLocks(number_of_lockers, number_of_students):
    m=number_of_lockers
    n=number_of_students
    if m>=0 and n>=0:
        l=[False] * m
        i=0
        while i<n:
            i=i+1
            for j in range(1, m+1):
                if j%i==0:
                    if l[j-1]==True:
                        l[j-1]=False
                    elif l[j-1]==False:
                        l[j-1]=True
        counter=0
        k=0
        while k < m:
            k = k+1
            if l[k-1]==True:
                counter=counter+1
        return counter
    else:
        return None



#### End OF MARKER





### YOUR CODE FOR mostTouchableLocker() FUNCTION GOES HERE ###

    

#### End OF MARKER
