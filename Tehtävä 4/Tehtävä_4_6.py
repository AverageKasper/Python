import random
amount = int(input("Syötä montako toistoa: "))
amount_done = 0
inside = 0
while amount > amount_done:
    CORX = random.uniform(1, -1)
    CORY = random.uniform(1, -1)
    if CORX**2+CORY**2<1:
        inside = inside + 1
    amount_done = amount_done + 1
    if amount == amount_done:
        almost_pi = (inside / amount) * 4
        print(f"Pi:n likiarvo : {almost_pi}")
        break
