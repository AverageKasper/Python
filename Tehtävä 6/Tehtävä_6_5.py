numlist = [1,2,3,4,5,6,7,8,9]

def laskuri(num: list):
    evennum = []    
    evennum = list(num)
    for i in evennum:
        if i % 2 > 0:
            evennum.remove(i)
    return(evennum)

print(f"Uusi Lista {laskuri(numlist)}. Vanha Lista {numlist}.")