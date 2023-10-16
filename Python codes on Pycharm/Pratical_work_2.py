def exercise1():
##########################################exercise1################
    print("[Exercise 1]")
    path = "k:\\Documents\\Web_Mining\\"
    str1 = input('Please enter a file name (without the txt extension): ')
    path_file = path+str1+".txt"
    with open(path_file, "r") as f:
        for l in f:
            print(l.replace("\n",""))



def exercise2a():
############################ Exercice 2a ############################################"""
    print("[Exercise 2a]")
    str1 = str(input('Please enter a file name:'))
    count = 1
    with open(str1, "r") as inputFile:
        for l in inputFile:
            print("Line "+str(count)+": "+l.replace("\n",""))
            count += 1


def exercise2b():
############################ Exercice 2b ############################################"""

    print("[Exercice 2b]")
    str1 = str(input('Please enter a file name:'))
    count = 1
    with open(str1, "r") as inputFile:
        for l in inputFile:
            if l != "\n":
                print("Line "+str(count)+": "+l.replace("\n",""))
                count += 1

def exercise3():
############################ Exercice 3 ############################################"""

    print("[Exercise 3]")
    count = 1
    with open("results_inline.txt", "w") as output:
        with open("resultsTriathlon.txt",'r') as inputFile:
            for l in inputFile:
                tl = l.split("\t")
                for i in range(1,len(tl)):
                    to_write = tl[0]+" "+str(i)+" "+tl[i]+"\n"
                    output.write(to_write)


def exercise4():
############################ Exercice 4 ############################################"""


    print("[Exercise 4]")

    go_on = True

    to_write = []

    while go_on :
        line = str(input('Please enter some text (enter [end] to stop):'))
        if line == "[end]" :
            go_on = False
        else:
            to_write.append(line)


    file_name = str(input('Please enter the file name:'))

    with open(file_name,"w") as output:
        for l in to_write:
            output.write(l+"\n")





exercise1()
exercise2a()
exercise2b()
exercise3()
exercise4()

