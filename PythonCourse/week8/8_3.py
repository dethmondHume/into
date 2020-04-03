def bouquets(narcissus_price, tulip_price, rose_price, summ):
    result = 0
    for i in range(int(summ / narcissus_price + 1)):
        for j in range(int(summ / tulip_price + 1)):
            for k in range(int(summ / rose_price + 1)):
                if (i + j + k) % 2 != 0 and narcissus_price*i + tulip_price*j + rose_price*k <= summ:
                    result += 1
    return result

print bouquets(1,1,1,5) # 34
print bouquets(2,3,4,10) # 12
print bouquets(2,3,4,100) # 4019
print bouquets(200,300,400,10000) # 4019
print bouquets(15.5,4.1,5.99,21.75)
print bouquets(21.25,13.6,10.5,100)
