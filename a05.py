# Your code for get_companies_names goes here
def get_companies_names(companyList):
    Elist1=[]
    for k in companyList:
        v=k["Company Name"]
        Elist1.append(v)
    return Elist1
# Your code for get_countries goes here
def get_countries(companyList):
    Elist2=[]
    Edict={}
    for i in companyList:
        v=i['Country']
        Elist2.append(v)
    for i in Elist2:
        Edict[i]=Elist2.count(i)
    return Edict
# Your code for get_companies goes here
def get_companies(companyList, location):
    a=[]
    for i in companyList:
        if i['City']==location['city']:
            if i['Country']==location['country']:
                b=i['Company Name']
                a.append(b)
            else:
                return None
    if a==[]:
        a=None
        return a
    else:
        return a    

