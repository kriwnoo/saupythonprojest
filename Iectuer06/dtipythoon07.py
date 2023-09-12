#คำสั่ง break กับ
for x in range(5) :
    if x == 3 :
        break; #brak ทำงานเมื่อไหร่จบ loop ทันที
    print(f'SAU...{x}')

print('++++++++++++++++++++')

for y in range(5) :
    if y == 3 :
        continue; #continue ทำงานเมื่อไหร่จบรอบนั้น ไปรอบต่อไปทีนที
print(f'DIT...{y}')