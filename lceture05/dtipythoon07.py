#โปรแกรมคำนวณหาพื้นที่วงกลม เส้นรอบวง และปริมาตรทรงกลมจากรัศมีมีที่ป้อนโดยผู้ใช้ทางแป้นพิมพ์ และแส้งพื้นที่ เส้นรอบ และปริมาณทางหน้าจอ

#ขอ5 ฟังก์ชัน
import math
#inputRadius
def inputRadius() :
    #r = input("ป้อนรัศมี :" )
    # return r

    #หรือ r = float(input("ป้อรัรศมี : "))
    #return r
    return float(input ("ป้อนรัศมี") : )

#calAeraCircle
def calAeraCircle(r) :
    #area = math.pi * r ** 2
    #area = math.pi * r ** r
    #area = math.pi * math.pow(r,2) 
    #return area
    return math.pi * math.pow (r,2)

#calAeraCircle 2 *pi * r


#calAeraCircle 4 / 3 * pi * r * r * r


#   showResuit ขอทั้งหมดทัศนิยม 4ตำแหน่ง
#พื้นที่วงกลม    เส้นรอบวง     ปริมาตรทรงกลมเป็น