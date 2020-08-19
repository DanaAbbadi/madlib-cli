import re

def read_template():
    """
    Returns the template.txt file 
    """
    file = open('assets/template.txt','r')
    content = file.read()
    return content

def parse(constant):
    """
    Returns a list of words inside {} in a given text

    Arguments:
        constant {string} -- text contains words inside {}
    Output:
        lst {list of string} -- the words inside {} 

    """
    lst=[]
    res = re.findall(r'\{.*?\}', constant)
    # res = re.findall(r'\{.*?\}', constant)
    for i in res:
        lst.append(i.strip("{ }"))    
    return lst

def merge(constant, words):  

    """
    Returns a string with user input strings

    Arguments:
        constant {string} -- text contains empty {}
    Output:
         {string} -- replacing {} to words from the user 

    """
    lst = parse(constant)  
    return (re.sub(r' {[^}]*}',' {}',constant)).format(*words)


def copyFile(text):
    print(text)
    file = open('assets/ready.txt','w')
    file.write(text)

if __name__ == "__main__":
    print("Welcome to Madlib Game")
    content = read_template()
    lst = parse(content)
    words=[]
    for i in range(len(lst)):
        words.append(input("enter a {} ".format(lst[i])))
    toCopy = merge(content, words)
    copyFile(toCopy)


# copyFile()


# all =[]
# # print(re.sub(r"{.*}", "{ }", content))
# for x in range(21):
#     all.append("yes")

# print((re.sub(r' {[^}]*}',' {} ',content)).format(*all))

