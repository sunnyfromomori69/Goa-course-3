"https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python"
#Descending Order
def descending_order(num):
    str_num = str(num)
    
    order = sorted(str_num)[::-1]
    combine ="".join(order)
    
    return int(combine)