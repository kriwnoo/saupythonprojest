#function 3  : no parameter /have reture
def dtil() :
    print(111)
    print(222)
    a, b, c = dti2( )
    print(f"สวัสดี {b} อายุ  {a} และ {c}")
    return 999

def dti2( ) :
    print(333)
    return 10+20, 'สมชาย' , True

print(dtil( ))
x = dtil( )
y = dtil( ) + 111 + 222
print('----------------------')