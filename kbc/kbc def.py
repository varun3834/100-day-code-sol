total =0
while True:
    print("Q1 Which of these states is also known for ‘Aligarh ke taale’, ‘Bareilly ka surma’ and ‘Firozabad ki chudiyan’?")
    print("a Madhya Pradesh" , "b Uttar Pradesh" , "c Bihar" , "d Himachal Pradesh")
    
    A=input("Enter answer : ")
    if A=='b':
        total = total +1
        print ("total score = ",total)
    else:
        print("Wrong answer")
        print ("total score = ",total)
        break
    
    print("Q2 Who became the first chancellor of the Aligarh Muslim University in 1920?")
    print('a Sultan Jahan Begum' "/n" 'b Maulana Abul Kalam Azad'"/n"'c Sir Syed Ahmad Khan'"/n"'d Mir Usman Ali Khan')
    
    A=input("Enter answer : ")
    if A=='a':
        total = total +1
        print ("total score = ",total)
    else:
        print("Wrong answer")
        print ("total score = ",total)
        break
    
        