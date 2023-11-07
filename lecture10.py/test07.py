#อ่านข้อมูลจากไฟล์
f_dti = open('myfile01.txt', 'r', encoding='uft-8')

try :
    data = f_dti.read()

    for data_by_line in data :
        print(f'SAU{data_by_line}')
   

except Exception :
    print('ติดต่อ Admin 00255888...')
finally :
    f_dti.close()