fish_size = float(input("Kuhan koko: "))
if fish_size >= 37:
    print("Hyvän kokoinen kuha, eikun vaa syömään!")
else:
    cm = 37 - fish_size
    print(f"Nyt on {cm:.1f} senttiä liian pieni, heitäppä takasin mereen")