#function แบบที่2 - Have parameter/no re
#parameters คือ เป็นตัวแปรประเภทหนึ่ง เอาไว้รับค่ามาใช้เฉพาะฟังก์ชั้นนั้นๆ เท่านั้น

def funcA(x, y ) :
    print(f'X is {x}')
    print(f'Y is {y}')
    print(f'SUM {x} + {y} = {x+y}')

funcA(10,20) #call function ข้อมุลที่สุงให้ paramester อาร์กิวเมนด์
funcA(1,4)
print('DTI....')
funcA(5,5)