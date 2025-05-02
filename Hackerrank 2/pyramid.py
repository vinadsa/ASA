# Punya Kevin Adi Santoso
def piramida(batu):
    # Basis rekursif: jika hanya satu batu, kembalikan sebagai list berisi satu tingkat.
    if len(batu) == 1:
        return [batu]
    else:
        # Hitung tingkat berikutnya dengan menjumlahkan pasangan batu.
        next_level = [batu[i] + batu[i+1] for i in range(len(batu)-1)]
        # Panggil fungsi secara rekursif untuk mendapatkan piramida di atas tingkat ini.
        piramida_atas = piramida(next_level)
        # Tambahkan tingkat saat ini ke piramida.
        piramida_atas.append(batu)
        return piramida_atas

# Contoh penggunaan:
n = int(input())
batu = [int(x) for x in input().split()]
piramida = piramida(batu)

# Output dari atas ke bawah:
for level in piramida:
    print(" ".join(map(str, level)))
