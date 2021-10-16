#Cole Hill
#CPSC 1301
#Dr. Carroll
#Project 5


#welcome function
def welcome():
    print("Welcome to the Words in a File Program!")



#get Filename function
def getFilename():
    f=True
    while f:
        filename=input("Please enter a filename:")
        mode='r'
        try:
            fileObject=open(filename, mode)
            f=False
        except FileNotFoundError:
            print("ALERT: Unable to open", filename)

    return filename
        
        

#get starting letter function
def getstartLetter():
    startLetter=input("Please enter in a starting letter:")
    while not(startLetter.isalpha()):
        startLetter=input("Please enter in a starting letter:")
    return startLetter.lower()
        
    
    
    
#get ending letter function
#same as start letter except variable is end letter
def getendLetter():
    endLetter=input("Please enter in a ending letter:")
    while not(endLetter.isalpha()):
        endLetter=input("Please enter in a ending letter:")
    return endLetter.lower()
    
        


#output function
def output(fileName, start,end):
    file = open(fileName,'r')
    start = ord(start)
    end = ord(end)
    words=file.read()
    words=words.lower()
    wordList=list(words.split())
    for i in range(start,end+1):
        letter = chr(i)
        print('All words starting with',letter)
        for x in wordList:
            if x[0]==letter:
                print(x)
    file.close()
    
        
            
    



#main function calling other functions
def main():
    welcome()
    file = getFilename()
    start = getstartLetter()
    end = getendLetter()
    output(file,start,end)
    


#call main function
main()
