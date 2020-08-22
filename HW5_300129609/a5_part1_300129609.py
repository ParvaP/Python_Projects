import string

def remove_pun (word):
    '''string->string
    Removes the punctuation from the string'''
    new_str = ''
    for c in word:
        if c not in string.punctuation:
            new_str=new_str+c
    return new_str

def make_dict (d,word,line):
    ''''(dict,str,int)->dict
    Adds each word to the dictionary along with it's line#'''
    if word in d.keys():
        d[word].add(line+1)
    else:
        d[word] = set([line+1])
    return d

def check_word (word):
    '''string->boolean
    Checks if the string is alphabetical and its longer than 1 character'''
    return word.isalpha() and len(word)>1

def open_file():
    '''None->file object
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    test = False
    try:
            name = input ("Enter the name of the file: ")
            fp  = open(name, "r")
            return fp
    except:
            test = True
    while test == True:
        print("There is no file with that name. Try again.")
        name = input ("Enter the name of the file: ")
        try:
            fp  = open(name, "r")
            return fp
            test = False
        except:
            test = True

    
def read_file(fp):
    '''(file object)->dict
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    d = {}
    text=fp.readlines()
    for line in range(len(text)):
        text2 = text[line].strip().lower().split()
        for word in range(len(text2)):
            text2[word] = remove_pun(text2[word])
            if check_word(text2[word]):
                d = make_dict(d,text2[word],line)
    return d
                
def find_coexistance(D, query):
    '''(dict,str)->list
    See the assignment text for what this function should do'''
    # YOUR CODE GOES HERE
    li = query.split()
    if len(li) > 0:
       shared = D.get(remove_pun(li[0]),-1)
    else:
        return ''
    if len(li) == 1:
        li[0] = remove_pun(li[0])
        return D.get(li[0],li[0])
    for i in range(len(li)-1):
        li[i] = remove_pun(li[i])
        li[i+1] = remove_pun(li[i+1])
        if li[i] not in D:
            return li[i]
        elif li[i+1] not in D:
            return li[i+1]
        shared = shared.intersection(D[li[i+1]])
    return shared
    

##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# YOUR CODE GOES HERE
count = 1
while query != 'q':
    if count == -1:
        query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    if query != 'q':
        li = find_coexistance(d,query)
        if type(li) != set:
            print ("Word \'"+str(li)+"\' not in the file.")
        else:
            li = sorted(li)
            print("The one or more words you entered coexisted in the following lines of the file:")
            for i in li:
                print (i,end=" ")
        print ()
        count = -1
