import math

# fungsi bil prima
def isPrima(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def count_prima(bilangan):
    return sum(1 for x in bilangan if isPrima(x))

def getPrima(jumlah):
    daftar_prima = []
    angka = 2
    while len(daftar_prima) < jumlah:
        if isPrima(angka):
            daftar_prima.append(angka)
        angka += 1
    return daftar_prima

# fungsi pembantu
def count_tidakcocok(aktual, ekspektasi):
    jumlah_tidak_cocok = 0
    indeks_tidak_cocok_pertama = None
    for i, (a, e) in enumerate(zip(aktual, ekspektasi)):
        if a != e:
            jumlah_tidak_cocok += 1
            if indeks_tidak_cocok_pertama is None:
                indeks_tidak_cocok_pertama = i
    return jumlah_tidak_cocok, indeks_tidak_cocok_pertama

def isPerfectKuadrat(n):
    akar = math.isqrt(n)
    return akar * akar == n

# fungsi pembuat pola
def pola_aritmatika(deret):
    beda = deret[1] - deret[0]
    return [deret[0] + beda * i for i in range(len(deret))]

def lanjutan_aritmatika(deret, jumlah):
    beda = deret[1] - deret[0]
    awal = deret[-1]
    return [awal + beda * (i+1) for i in range(jumlah)]

def pola_geometri(deret):
    rasio = deret[1] / deret[0]
    return [int(deret[0] * (rasio ** i)) for i in range(len(deret))]

def lanjutan_geometri(deret, jumlah):
    rasio = deret[1] / deret[0]
    awal = deret[-1]
    return [int(awal * (rasio ** (i+1))) for i in range(jumlah)]

def pola_fibonacci(deret):
    if len(deret) < 2: return deret[:]
    hasil = deret[:2]
    for i in range(2, len(deret)):
        hasil.append(hasil[i-1] + hasil[i-2])
    return hasil

def lanjutan_fibonacci(deret, jumlah):
    if len(deret) < 2: return []
    a, b = deret[-2], deret[-1]
    hasil = []
    for _ in range(jumlah):
        c = a + b
        hasil.append(c)
        a, b = b, c
    return hasil

def pola_kuadrat(deret):
    akar = math.isqrt(deret[0])
    return [(akar + i) ** 2 for i in range(len(deret))]

def lanjutan_kuadrat(deret, jumlah):
    akar_terakhir = math.isqrt(deret[-1]) if isPerfectKuadrat(deret[-1]) else math.isqrt(deret[0]) + len(deret) - 1
    return [(akar_terakhir + i + 1) ** 2 for i in range(jumlah)]

def pola_prima(deret):
    return getPrima(len(deret))

def lanjutan_prima(deret, jumlah):
    semua_prima = getPrima(len(deret) + jumlah)
    return semua_prima[len(deret):]

# deteksi pola utama
def deteksi_pola(deret):
    kandidat_pola = [
        ("kuadrat", pola_kuadrat, lanjutan_kuadrat),
        ("aritmatika", pola_aritmatika, lanjutan_aritmatika),
        ("geometri", pola_geometri, lanjutan_geometri),
        ("fibonacci", pola_fibonacci, lanjutan_fibonacci),
        ("prima", pola_prima, lanjutan_prima)
    ]
    
    terbaik = (None, None, None, float('inf'), None)
    for nama, fungsi_pola, fungsi_lanjutan in kandidat_pola:
        # lewati pola yg tdk berlaku
        if nama == "kuadrat" and not isPerfectKuadrat(deret[0]):
            continue
        if nama == "geometri" and deret[0] == 0:
            continue
            
        ekspektasi = fungsi_pola(deret)
        tidak_cocok, pertama_tidak_cocok = count_tidakcocok(deret, ekspektasi)
        
        if tidak_cocok < terbaik[3]:
            terbaik = (nama, fungsi_pola, fungsi_lanjutan, tidak_cocok, pertama_tidak_cocok)
    
    return terbaik

###########################################################################################################
# main
def analisis_deret(arr):
    n = len(arr)
    
    # if mayoritas prima
    if count_prima(arr) >= n / 2:
        ekspektasi = getPrima(n)
        tidak_cocok, pertama_tidak_cocok = count_tidakcocok(arr, ekspektasi)
        if tidak_cocok > 0:
            return pertama_tidak_cocok
        else:
            return None
    
    # partisi
    tengah = (n + 1) // 2
    kiri = arr[:tengah]
    kanan = arr[tengah:]
    
    # Deteksi pola pada kedua bagian
    hasil_kiri = deteksi_pola(kiri)
    hasil_kanan = deteksi_pola(kanan)
    
    # assign tuple hasil ke masing2 var
    nama_kiri, _, lanjut_kiri, tidak_cocok_kiri, pertama_tidak_cocok_kiri = hasil_kiri
    nama_kanan, _, lanjut_kanan, tidak_cocok_kanan, pertama_tidak_cocok_kanan = hasil_kanan
    
    # calon yg nanti diproses
    if tidak_cocok_kiri > 0:
        target = "kiri"
    elif tidak_cocok_kanan > 0:
        target = "kanan"
    else:
        if nama_kiri is None and nama_kanan is None:
            return None
        if nama_kiri is None:
            target = "kanan"
        elif nama_kanan is None:
            target = "kiri"
        else:
            target = "kiri" if len(kiri) >= len(kanan) else "kanan"
    
    # proses kanan atau kiri
    if target == "kiri":
        if tidak_cocok_kiri > 0:
            return pertama_tidak_cocok_kiri
        ekspektasi_kanan = lanjut_kiri(kiri, len(kanan))
        tidak_cocok, pertama_tidak_cocok = count_tidakcocok(kanan, ekspektasi_kanan)
        if tidak_cocok > 0:
            return tengah + pertama_tidak_cocok
    else:  # target == "kanan"
        if tidak_cocok_kanan > 0:
            return tengah + pertama_tidak_cocok_kanan
        ekspektasi_kiri = lanjut_kanan(kanan, len(kiri))
        tidak_cocok, pertama_tidak_cocok = count_tidakcocok(kiri, ekspektasi_kiri)
        if tidak_cocok > 0:
            return pertama_tidak_cocok
    
    return None

# input
arr = [int(x) for x in input().split()]
hasil = analisis_deret(arr)
print(hasil)