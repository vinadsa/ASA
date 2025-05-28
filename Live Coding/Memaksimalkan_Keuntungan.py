# PUNYA KEVIN ADI SANTOSO
import random
from dataclasses import dataclass
from typing import List, Tuple

# class barang
class Barang:
    def __init__(self, no, nama, panjang, lebar, tinggi, harga):
        self.no = no
        self.nama = nama
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.harga = harga

        # hitung dimensi dan rasio
        self.dimensi = self.panjang + self.lebar + self.tinggi
        if self.dimensi != 0:
            self.ratio = self.harga / self.dimensi
        else:
            self.ratio = 0

best_profit = 0
best_items = []

def BnB(items, kapasitas, index=0, current_weight=0, current_profit=0, current_items=None):
    global best_profit, best_items
    if current_items is None: # basis: sudah cek smua item
        current_items = []

    if index >= len(items):
        if current_profit > best_profit:
            best_profit = current_profit
            best_items = current_items[:]
        return

    # pruning
    remaining_kapasitas = kapasitas - current_weight
    max_possible_profit = current_profit
    i = index
    while i < len(items):
        if items[i].dimensi <= remaining_kapasitas:
            max_possible_profit = max_possible_profit + items[i].harga
            remaining_kapasitas = remaining_kapasitas - items[i].dimensi
        i = i + 1
    if max_possible_profit <= best_profit:
        return
    current_item = items[index]
    
    # branch 1 item di ambil
    if current_weight + current_item.dimensi <= kapasitas:
        BnB(items, kapasitas, index + 1,
                         current_weight + current_item.dimensi,
                         current_profit + current_item.harga,
                         current_items + [current_item])
    
    # branch 2 item diskip
    BnB(items, kapasitas, index + 1,
                     current_weight, current_profit, current_items)


def solve_knapsack(barang_list, kapasitas):
    global best_profit, best_items
    best_profit = 0
    best_items = []

    # filter barang valid (dimensi <= 5)
    valid_items = []
    for b in barang_list:
        if b.dimensi <= 5 and b.dimensi <= kapasitas:
            valid_items.append(b)

    # sort berdasarkan rasio
    for i in range(len(valid_items)):
        for j in range(i + 1, len(valid_items)):
            if valid_items[j].ratio > valid_items[i].ratio:
                temp = valid_items[i]
                valid_items[i] = valid_items[j]
                valid_items[j] = temp
    BnB(valid_items, kapasitas)
    return best_items[:], best_profit

def generate_barang(n):
    items = []
    for i in range(1, n + 1):
        nama = "BRG" + str(i).zfill(3) #BRG artinya barang
        p = random.randint(1, 3)
        l = random.randint(1, 3)
        t = random.randint(1, 3)
        harga = random.randint(20, 150)
        items.append(Barang(i, nama, p, l, t, harga))
    return items


def print_hasil(selected, profit, kapasitas):
    print("Hasil (kapasitas:", kapasitas, ")")
    if not selected:
        print("Tidak ada barang dipilih")
        return
    total_dim = 0
    for item in selected:
        total_dim = total_dim + item.dimensi
        print(item.nama, item.harga, item.dimensi)
    print("Jumlah:", len(selected))
    print("Total dimensi:", total_dim)
    print("Total keuntungan:", profit)

def run_test(n_items, kapasitas):
    print("\n==================================================")
    print("TEST:", n_items, "barang, kapasitas", kapasitas)
    print("==================================================")
    items = generate_barang(n_items)

    print("Sample 3 barang pertama:")
    for item in items[:3]:
        print(" ", item.nama + ": P=" + str(item.panjang) + ", L=" + str(item.lebar) + ", T=" + str(item.tinggi) + ", Dim=" + str(item.dimensi) + ", Harga=" + str(item.harga))
    
    selected, profit = solve_knapsack(items, kapasitas)
    print_hasil(selected, profit, kapasitas)

def main():
    print("Algoritma yg dipakai Branch and Bound")
    random.seed(42)
    tests = [
        (10, 30),
        (30, 50),
        (100, 100)
    ]

    for test in tests:
        run_test(test[0], test[1])
    print("==================================================")
    print("PENJELASAN ALGORITMA:")
    print("1. Filter barang dengan dimensi <= 5")
    print("2. Sort berdasarkan rasio harga/dimensi")
    print("3. Rekursi: coba ambil/skip setiap barang")
    print("4. Pruning: skip jika estimasi tidak lebih baik")
    print("5. Simpan kombinasi terbaik")
    print("==================================================")

if __name__ == "__main__":
    main()

    print("PRINT OUT STEP BY STEP (SEMOGA KELAR)")
    print("Ternyata tidak sempat")

