"""3) for ციკლის საშვალებით გამოთვალეთ 10-იდან 50-ის ჩათვლით ყველა რიცხვის ჯამი"""


# sum = 0
# for num in range(10, 51):
#     sum += num

# print(sum)


"""5) for ციკლის საშვალებით გამოთვალეთ 7-ის ფაქტორიალი. რიცხვის ფაქტორიალი არის ყველა რიცხვის ნამრავლი ამ რიცხვიდან 1-მდე"""

# 1, 2, 3, 4, 5, 6, 7
# 7, 6, 5, 4, 3, 2, 1

product = 1

for num in range(1, 8):
    product *= num

print(product)