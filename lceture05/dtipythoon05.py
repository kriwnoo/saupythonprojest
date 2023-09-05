#คำนวณเงินที่แชร์กัน ป้อนเงิน ป้อนคน แล้วคำนวณและแสดงเงินที่แชร์กันทางหน้าจอ
#โดยให้เขียนเป็นฟังก์ชัน ขอ 2 ฟังก์ชัน
#cast/conversion

#รับค่าข้อมูล
def inputMouneyperson() :
    money = float ( input('ป้อนเงิน : ') )
    person = int( input('ป้อนคน :') )
    return money, person

#คำนวณ แล้วแสดงออกมา
def calandsharemonershare(money, person ) :
    #เงิน ขอทศนิยม 2ตำแหน่ง แชร์กันขอเลขจำนวนเต็มปัดขึ้น
    print(f'จำนวนเงิน {money} บาท คน {person} คน แชร์กันคนละ {money/person} บาท')
    print("จำนวนเงิน",'%.2f' % money ,'บาท คน', person , 'คน แชร์กับคนละ', round(money/person),'บาท' )
    print("จำนวนเงิน"+" "+ str("%.2f" % money) +" "+'บาท คน'+" "+ str(person) +" "+"คน แชร์กันคนละ"+" "+ str(round/person))
    print("จำนวนเงิน{} บาท คน {} คน แชร์กันคนละ {} บาท" .format("%.2f"%money,person,round(money/person)))
    print("จำนวนเงิน %s บาท คน %s คน แชร์กันคนละ %s บาท" % ("%.2f"%money,person,round(money/person)))


money, person  = inputMouneyperson( )



calandsharemonershare(money , person)