#checks pali-------------------
def ispali(text):
    words = text.split()
    for terms in words:
        cpy_words = ""
        for points in terms:
            cpy_words = points+cpy_words
        if cpy_words == terms:
            print("Is pali")
        else:
            print("Not pali")
#vowels-------------
def vwls(text):
    vowels = "aeiou"
    words = text.split()
    n1 = 0
    for terms in words:
        for points in terms:
            if points in vowels:
                n1 += 1
    return n1
#word count---------
def cont(text):
    words = text.split()
    n2 =0
    for terms in words:
        n2+=1
    return n2
#calling----------------
def fre(text):
    free = {
        "mango":0,
        "apple":0,
        "banana":0
    }
    words = text.split()
    for x in words:
        if x == "mango":
            free["mango"] += 1
        elif x == "apple":
            free["apple"] += 1
        else:
            free["banana"] += 1
    return free
#----------------------------

Sentence = input("Enter sentence: ")
ispali(Sentence)
print(vwls(Sentence))
print(cont(Sentence))
print(fre(Sentence))
