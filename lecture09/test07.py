import test06 #User(Dev)-define module
import math  #Bild-in module

from test08 import calSquareArea, calTriagleArea, calCircleArea

print(f'ผลรวมของ10 + 20 = {test06.sumNumber(10,20)}')

test06.showHi()

print(f'ราคาสินค้า 20000 ภาษีเป็นเงิน{2000 * test06.VAT}')

print(f'7 ยกกำลัง 15 มีค่า {math.pow(7, 15)}')

print(f'พื้อนที่วงกลม รัศมี 3 มีค่า{math.pi* math.pow(3, 2)}')

print(f'พื้นที่วงกลม รัศมี8 มีค่า{calCircleArea(8)}')

print(f'พื้นท่วงกลมสี่เหลี่ยม กว้าง 10 ยาว5 เท่า{calCircleArea(10, 5)}')