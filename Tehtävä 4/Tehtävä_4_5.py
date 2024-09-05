usercor = str('python')
pwcor = str('rules')
attempt = 1
while usercor and pwcor:
    user = input("Syötä käyttäjä: ")
    if attempt == 5:
        print("lukittu")
        break
    if user == usercor:
        pw = input("salasana: ")
        if pw == pwcor:
            print("sisään")
            break
        else:
            attempt = attempt + 1
            print("yritä uudestaan")
    else:
        attempt = attempt + 1
        print("käyttäjä väärin")