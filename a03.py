### YOUR CODE FOR chocolatePrice() FUNCTION GOES HERE ###
def chocolatePrice(ali_budget, bashir_budget):
    
    if ali_budget >=0 and bashir_budget >=0:
        for i in range(1,ali_budget+1 and bashir_budget+1):
            if ali_budget%i==bashir_budget%i==0:
                price = i
        return(price)
    else:
        return 'Not Possible'

#### End OF MARKER





### YOUR CODE FOR calculateProfit() FUNCTION GOES HERE ###
def calculateProfit(ali_budget, bashir_budget):
    
    if type(ali_budget)== str or type(bashir_budget)==str:
        return 'Not Possible'
    
    if ali_budget ==0 or bashir_budget==0 or ali_budget < 0 or bashir_budget < 0 :
        return "Not Possible"
   
    if ali_budget > bashir_budget:
        A=(bashir_budget*2) - bashir_budget
        B=(ali_budget*(1.5)) - ali_budget
    else:
        A=(ali_budget*2) - ali_budget
        B=(bashir_budget*(1.5)) - bashir_budget
        
    if A > B:
        test=A % 1.0
        if test>= 0.5:
            A=int(A)+1
        return A
    else:
        test=B % 1.0
        if test>= 0.5:
            B=int(B)+1
        return B

#### End OF MARKER
