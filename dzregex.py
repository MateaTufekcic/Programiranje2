import re
result=None
while not result:
    unos=input("Unesite:")
    reg="^M[0-5]+ T$"
    result=re.match(reg,unos)
    print(result)

    


