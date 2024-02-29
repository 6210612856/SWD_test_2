
"""
Convert Arabic Number to Roman Number.
เขียนโปรแกรมรับค่าจาก user เพื่อแปลง input ของ user ที่เป็นตัวเลขอราบิก เป็นตัวเลขโรมัน
โดยที่ค่าที่รับต้องมีค่ามากกว่า 0 จนถึง 1000

*** อนุญาตให้ใช้แค่ตัวแปรพื้นฐาน, built-in methods ของตัวแปรและ function พื้นฐานของ Python เท่านั้น
ห้ามใช้ Library อื่น ๆ ที่ต้อง import ในการทำงาน(ยกเว้น ใช้เพื่อการ test การทำงานของฟังก์ชัน).

"""

def roman_num(num):
    roman_str = ""
    roman_dict = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
    roman_chr = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    i = 0

    while i < len(roman_dict):
        roman_str = roman_str + ((num//roman_dict[i]) * roman_chr[i])
        num = num % roman_dict[i]

        i += 1

    return roman_str


