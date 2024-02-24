#122140054_Casey Z.D Manurung

n= int(input("Height: "))

for i in range(1, n + 1):
    # Mencetak spasi sebelum bintang
    for j in range(0, n - i):
        print(" ", end="")
    
    # Mencetak bintang
    for j in range(1, i + 1):
        print("* ", end="")
    
    # Pindah baris setelah satu baris selesai
    print()
