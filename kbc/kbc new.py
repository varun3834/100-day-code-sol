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

Q=[Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15]
opt1=[Q1a,Q2a,Q3a,Q4a,Q5a,Q6a,Q7a,Q8a,Q9a,Q10a,Q11a,Q12a,Q13a,Q14a,Q15a]
opt2=[Q1b,Q2b,Q3b,Q4b,Q5b,Q6b,Q7b,Q8b,Q9b,Q10b,Q11b,Q12b,Q13b,Q14b,Q15b]
opt3=[Q1c,Q2c,Q3c,Q4c,Q5c,Q6c,Q7c,Q8c,Q9c,Q10c,Q11c,Q12c,Q13c,Q14c,Q15c]
opt4=[Q1d,Q2d,Q3d,Q4d,Q5d,Q6d,Q7d,Q8d,Q9d,Q10d,Q11d,Q12d,Q13d,Q14d,Q15d]
A=[Q1,Q2,Q3,Q4,Q5,Q6,Q7,Q8,Q9,Q10,Q11,Q12,Q13,Q14,Q15]





def kbc(Q,A,opt1,opt2,opt3,opt4):

    def opt(Q,A,opt1,opt2,opt3,opt4):
        print(Q)
   
        print(opt1)
        print(opt2)
        print(opt3)
        print(opt4)
        
        Y=input("type your answer: ")
    
        
        if Y==A:
            print("correct answer")
            global total
            total=total +1
            print("your total score =",total)
        else:
            print(total)
            
    for Q in Q:
        print(Q)
        
        # for opt1 in opt1:
        #     print(opt1)
        #     for opt2 in opt2:
        #         print(opt2)
        #         for opt3 in opt3:
        #             print(opt3)
        #             for opt4 in opt4:
        #                 print(opt4)
        #                 for A in A:
        #                     pass
                            
                            
        
        
        
        return



kbc(Q,A,opt1,opt2,opt3,opt4)
