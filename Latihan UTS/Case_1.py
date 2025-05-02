def search_artifact(territory, low, high):
    """
    Fungsi ini mensimulasikan misi pencarian artefak "Mata Naga" dalam Kerajaan Ardan.
    
    Setiap wilayah yang dicari direpresentasikan sebagai sebuah sub-array di dalam list 'territory'.
    - Basis kasus: Jika wilayah tersebut hanya memiliki satu petunjuk (low == high),
      kembalikan nilai petunjuk tersebut.
    - Rekurensif: Bagi wilayah menjadi dua, kirim dua scout untuk mencari
      petunjuk di masing-masing bagian.
    - Combine: Gabungkan petunjuk dari kedua wilayah dengan operasi konstan (penjumlahan).
    
    Kompleksitas waktu: T(n) = 2T(n/2) + k, di mana k adalah biaya konstan penggabungan.
    """
    # Basis kasus: hanya ada satu wilayah/petunjuk
    if low == high:
        # Di sinilah scout menemukan petunjuk dasar
        print(f"Scout menemukan petunjuk di wilayah {low}: {territory[low]}")
        return territory[low]
    
    # Bagi wilayah menjadi dua bagian
    mid = (low + high) // 2
    
    # Dispatch dua scout ke masing-masing bagian wilayah secara rekurensif
    print(f"Memerintahkan scout untuk menjelajah wilayah {low} sampai {mid} dan {mid+1} sampai {high}")
    clue_left = search_artifact(territory, low, mid)
    clue_right = search_artifact(territory, mid + 1, high)
    
    # Gabungkan kedua petunjuk dengan operasi konstan (misal, penjumlahan)
    combined_clue = clue_left + clue_right
    print(f"Menggabungkan petunjuk dari wilayah {low}-{mid} dan {mid+1}-{high}: {clue_left} + {clue_right} = {combined_clue}")
    
    return combined_clue

# Contoh eksekusi cerita pencarian artefak "Mata Naga"
if __name__ == '__main__':
    # Setiap angka dalam daftar mewakili petunjuk yang ditemukan di masing-masing wilayah kecil.
    # Misalnya, nilai yang lebih tinggi dapat menandakan petunjuk yang lebih kuat.
    territory = [5, 3, 8, 2, 7, 4, 6, 1]
    
    print("=== Misi Pencarian 'Mata Naga' Dimulai ===")
    final_clue = search_artifact(territory, 0, len(territory) - 1)
    print("=== Misi Selesai ===")
    print("Petunjuk gabungan untuk menemukan artefak 'Mata Naga':", final_clue)
