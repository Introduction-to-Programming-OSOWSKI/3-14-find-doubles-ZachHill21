def findDoubles(w):
    for i in range(0, len(w)):
        if w[i] == "l":
            return True 
        else: 
            return False
print (findDoubles("log"))
