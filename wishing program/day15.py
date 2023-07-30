import time as t 
# task 2

name="VK"
curtime=t.strftime('%H,%M,%S')

print(curtime)
curhr=t.strftime('%H')
print(curhr)
curhr=int(curhr)
# while curhr<24:
#     curhr=int(input('enter hour between 0 to 24: '))
#     if curhr<=17 and curhr>=12:
#            print( "good afternoon" ,name )
#     elif curhr>=17 and curhr<=21:
#            print( "good evening" ,name )
#     elif curhr>=21 and curhr<=24:
#            print( "good night" ,name )
#     elif curhr>=00 and curhr<=5:
#            print( "good night" ,name )
#     elif curhr>=5 and curhr<=12:
#            print( "good morning" ,name )
#     else :
#             print('error')
# else :
#        print('error')

       
if curhr<=17 and curhr>=12:
    print( "good afternoon" ,name )
elif curhr>=17 and curhr<=21:
    print( "good evening" ,name )
elif curhr>=21 and curhr<=24:
    print( "good night" ,name )
elif curhr>=00 and curhr<=5:
    print( "good night" ,name )
elif curhr>=5 and curhr<=12:
    print( "good morning" ,name )
else :
    print('error')