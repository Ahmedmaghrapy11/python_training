def bonAppetit(bill, k, b):
    
    bill = list(bill)
    bill.remove(bill[k])
    annaBill = bill

    bActual = sum(annaBill) / 2

    if bActual == b:
        print('Bon Appetit')
    else:
        print(int(b - bActual))

bonAppetit([3, 10, 2, 9], 1, 7)

