#all Q
Q1="Q1 Which of these states is also known for ‘Aligarh ke taale’, ‘Bareilly ka surma’ and ‘Firozabad ki chudiyan’?"
Q2="Q2 Who became the first chancellor of the Aligarh Muslim University in 1920?"
Q3="Q3 Rajat Sharma, Sonia Singh, Rahul Kanwal and Sumit Awasthi are all associated with which profession?"
Q4="Q4 Dadra, Nagar Haveli, Daman and the island of Diu were all under which European colonial power?"
Q5="Q5 Which was the colour of the saree worn by Madhuri Dixit in the song ‘Didi tera dewar deewana,’ which triggered a fashion trend in the country?"
Q6="Q6 In Sept 2020, which iconic motorcycle brand announced that it is shutting down its manufacturing facilities in India?"
Q7="Q7 Where in Singapore did Netaji Subhash Chandra Bose make the first proclamation of an Azad Hind government?"
Q8="Q8 Which of the following will be heavier than 1450 g of iron?"
Q9="Q9 During the Battle of Kurukshetra, Krishna deceived the Kauravas by hiding the sun behind clouds to enable Arjuna to kill whom?"
Q10="Q10 Which of these songs about rain does not have any rain sequence?"
Q11="Q11 In 2008, Rajasthan Royals became the first winner of which annual sporting event?"
Q12="Q12 Which novel, made into a TV series by Mira Nair in 2020, revolves around the lives of four Indian families – the Mehras, the Kapoors, the Khans and the Chatterjis?"
Q13="Q13 Which of these does not feature in the five pillars of Islam?"
Q14="Q14 What are the terms 3G, 4G and 5G related to? Grading in Schools. Population Generations Phone Networks Digital Camera"
Q15="Q15 Which of the following dynasties did the Kanva dynasty overthrow to come to power around 73 BCE in Magadha? Chera dynasty Shunga dynasty Pala dynasty Maurya dynasty"

#options
#Q1
Q1a="a Madhya Pradesh"
Q1b="b Uttar Pradesh"
Q1c="c Bihar"
Q1d="d Himachal Pradesh"
# ANS b

#Q2
Q2a='a Sultan Jahan Begum'
Q2b='b Maulana Abul Kalam Azad'
Q2c='c Sir Syed Ahmad Khan'
Q2d='d Mir Usman Ali Khan'
# ANS a
#Q3
Q3a='a Journalism'
Q3b='b Astrology'
Q3c='c Law'
Q3d='d Medicine'
# ANS a

#Q4
Q4a='a Portugal'
Q4b='b Denmark'
Q4c='c France'
Q4d='d Britain'
# ANS a

#Q5
Q5a='a Purple'
Q5b='b Yellow'
Q5c='c Red'
Q5d='d Green'
# ANS a

#Q6
Q6a='a Triumph'
Q6b='b Harley Davidson'
Q6c='c Arctic cat'
Q6d='d Indian'
# ANS b

#Q7
Q7a='a Fort Canning park'
Q7b='b National Gallery of Singapore'
Q7c='c Cathay cinema hall'
Q7d='d National University of Singapore'
# ANS c

#Q8
Q8a='a 1.3 kg of husk'
Q8b='b 1 kg of rice'
Q8c='c 1.4 kg of paper'
Q8d='d 1.7 kg of cotton'
# ANS d

#Q9
Q9a='a Jayadratha'
Q9b='b Shakuni'
Q9c='c Dronacharya'
Q9d='d Dushasana'
# ANS a

#Q10
Q10a='a Ghanan ghanan (Lagaan)'
Q10b='b Barso re (Guru)'
Q10c='c Tip tip barsa paani (Mohra)'
Q10d='d Rimjhim ghire saawan (Manzil)'
# ANS d

#Q11
Q11a='a PSL'
Q11b='b BBS'
Q11c='c IPL'
Q11d='d BPL'
# ANS C

#Q12
Q12a='a Golden Gate'
Q12b='b A Suitable Boy'
Q12c='c A Fine Balance'
Q12d='d The Great Indian Novel'
# ANS B
#Q13
Q13a='a Salat'
Q13b='b Zakat'
Q13c='c Hadith'
Q13d='d Hajj'
# ANS C
#Q14
Q14a='a Mobile Telecommunications Technology'
Q14b='b Phone Networks'
Q14c='c Wireless Communication Standards'
Q14d='d Cellular Network Technology'
# Ans b

#Q15
Q15a='a Nanda dynasty'
Q15b='b Maurya dynasty'
Q15c='c Gupta dynasty'
Q15d='d Shunga dynasty'
# Ans d


quesations=[
    [
        Q1,Q1a,Q1b,Q1c,Q1d,"b"
    ],[
        Q2,Q2a,Q2b,Q2c,Q2d,"a"
    ],[
        Q3,Q3a,Q3b,Q3c,Q3d,"a"
    ],[
        Q4,Q4a,Q4b,Q4c,Q4d,"a"
    ],[
        Q5,Q5a,Q5b,Q5c,Q5d,"a"
    ],[
        Q6,Q6a,Q6b,Q6c,Q6d,"b"
    ],[
        Q7,Q7a,Q7b,Q7c,Q7d,"c"
    ],[
        Q8,Q8a,Q8b,Q8c,Q8d,"d"
    ],[
        Q9,Q9a,Q9b,Q9c,Q9d,"a"
    ],[
        Q10,Q10a,Q10b,Q10c,Q10d,"d"
    ],[
        Q11,Q11a,Q11b,Q11c,Q11d,"c"
    ],[
        Q12,Q12a,Q12b,Q12c,Q12d,"b"
    ],[
        Q13,Q13a,Q13b,Q13c,Q13d,"c"
    ],[
        Q14,Q14a,Q14b,Q14c,Q14d,"b"
    ],[
        Q15,Q15a,Q15b,Q15c,Q15d,"d"
    ]
    ]









levels= [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 ]

for i in range(0,len(quesations)):
    quesation=quesations[i]
    print(quesation[0])
    print(f'.{quesation[1]}')
    print(f'.{quesation[2]}')
    print(f'.{quesation[3]}')
    print(f'.{quesation[4]}')
    
    
    reply=input("type your ans between 1 to 4:  ")
    
    if reply==quesation[-1]:
        print(f"right answer you won {levels[i]} paise")
        
    else :
        break
    