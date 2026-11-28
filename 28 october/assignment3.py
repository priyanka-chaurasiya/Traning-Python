# calculate profit and loss with given cost price and selling price.


cp = float(input("Enter Cost Price: "))
sp = float(input("Enter Selling Price: "))

if sp > cp:
    profit = sp - cp
    print("Profit =", profit)
else:
    if cp > sp:
        loss = cp - sp
        print("Loss =", loss)
    else:
        print("No Profit No Loss")
