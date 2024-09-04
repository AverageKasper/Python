num = int(input("Syötä kokonaisluku: "))
if num > 1:
    for n in range(2, (num//2)+1):
        if num % n == 0:
            print(f"Luku {num} ei ole alkuluku.")
            break
    else:
        print(f"Luku {num} on alkuluku")
else:
    print(f"Luku {num} ei ole alkuluku.1")