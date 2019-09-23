
d = []
def readcurrency(currencyfile):
    with open("currenciesforquiz1.txt", "r") as contents:
        new_file = contents.readlines()
        for l in new_file:
            lines = l.split(" ")
            d.append("symbols"[0])
            d.append(dict(l))
    print(new_file)
readcurrency("currenciesforquiz1.txt")

        
