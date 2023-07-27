from collections import Counter

def price(items_pricing, scanned_items):

    total_price = 0
    items_count = Counter(scanned_items)

    for item, n in items_count.items():

        count = n
        remaining = n
        
        if(items_pricing[item][1] != None):
            if(count - items_pricing[item][1][0] >= 0):
                count = n // items_pricing[item][1][0]                
                remaining = n % items_pricing[item][1][0]
                total_price += count * items_pricing[item][1][1]

        total_price += remaining*items_pricing[item][0]

    print (total_price)
    return total_price

items_pricing = {
    'A': (50, (3, 130)),
    'B': (30, (2, 45)),
    'C': (20, None),
    'D': (15, None),
}


assert price(items_pricing, "") == 0
assert price(items_pricing, "A") == 50
assert price(items_pricing, "AB") == 80
assert price(items_pricing, "CDBA") == 115
assert price(items_pricing, "AA") == 100
assert price(items_pricing, "AAA") == 130
assert price(items_pricing, "AAAA") == 180
assert price(items_pricing, "AAAAA") == 230
assert price(items_pricing, "AAAAAA") == 260
assert price(items_pricing, "AAAB") == 160
assert price(items_pricing, "AAABB") == 175
assert price(items_pricing, "AAABBD") == 190
assert price(items_pricing, "DABABA") == 190