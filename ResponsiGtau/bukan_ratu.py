# Punya Kevin Adi Santoso
def bukan_ratu(start, goal):
    
    # konversi posisi
    kolom_start = ord(start[0]) - 1
    baris_start = int(start[1]) - 1
    kolom_goal = ord(goal[0]) - 1
    baris_goal = int(goal[1]) - 1

    # benteng
    langkah_benteng = 0
    # awal dan tujuan sama
    if kolom_start == kolom_goal and baris_start == baris_goal:
        langkah_benteng = 0
    elif kolom_start == kolom_goal or baris_start == baris_goal:
        langkah_benteng = 1
    else:
        langkah_benteng = 2

    # menteri
    langkah_menteri = 0
    # awal dan tujuan sama
    if kolom_start == kolom_goal and baris_start == baris_goal:
        langkah_menteri = 0
    # warna kotak beda
    elif (kolom_start + baris_start) % 2 != (kolom_goal + baris_goal) % 2:
        langkah_menteri = 0
        
    else:  # warna kotak sama
        if abs(kolom_start - kolom_goal) == abs(baris_start - baris_goal): # bisa sekali diagonal
            langkah_menteri = 1
        else:
            langkah_menteri = 2

    # raja
    langkah_raja = max(abs(kolom_start - kolom_goal), abs(baris_start - baris_goal))
    
    return langkah_benteng, langkah_menteri, langkah_raja



start, goal = input().split()
hasil = bukan_ratu(start, goal)

langkah_benteng, langkah_menteri, langkah_raja = hasil

print(f"{langkah_benteng} {langkah_menteri} {langkah_raja}")