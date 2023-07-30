



text=(input("type text:  "))
t=text.split(" ")

r=int(input('''cooding 0
        decoding 1:  '''))


if  r==0:
    text=text[1:] + text[0]
    
    pass
elif r==1:
    text=text[-1] + text[0:-1]
    pass
else:
    print("error")