import math
import time

try:
    from inventory_generator import generate_random_inventory # Jika diperlukan untuk testing random manual
except ImportError:
    print("File 'inventory_generator.py' tidak ditemukan.")
    exit()

def greedy_optimization(initial_inventory_list, carry_capacity):
    """
    Algoritma Greedy untuk memaksimalkan profit bersih dari pengambilan emas
    dengan mengorbankan item dari inventaris.

    Strategi:
    1. Prioritaskan mengambil emas jika sudah ada ruang.
    2. Jika tidak ada ruang, atau ingin mengambil lebih banyak emas,
       buang item dari inventaris dimulai dari yang paling tidak efisien
       (nilai/berat terendah) satu unit pada satu waktu.
    3. Setiap kali item dibuang dan ruang tercipta, coba ambil emas.
    4. Hanya lakukan drop dan ambil emas jika profit bersih tetap positif atau meningkat.
       (Untuk versi ini, kita akan lebih sederhana: drop untuk buat ruang, lalu isi emas)
    """
    
    # Copy agar tidak merubah inventory asli
    current_inventory = []
    for item_orig in initial_inventory_list:
        current_inventory.append(item_orig.copy())

    # 1. Tambahkan key efisiensi dan siapkan item untuk didrop
    # Item yang akan didrop akan displit menjadi unit-unit individual jika stackable
    droppable_units = []
    for item in current_inventory:
        berat_satuan = item['Berat_Satuan']
        nilai_satuan = item['Nilai_Satuan']

        # Pengecualian untuk items dengan berat 0
        item['Efisiensi'] = nilai_satuan / berat_satuan if berat_satuan > 0 else float('inf')
        
        # Untuk item stackable, split menjadi unit individual untuk dipertimbangkan drop
        if item['Stackable'] and item['Jumlah'] > 0 :
            for _ in range(item['Jumlah']):
                droppable_units.append({
                    'Nama_Item': item['Nama_Item'],
                    'Berat_Satuan': berat_satuan,
                    'Nilai_Satuan': nilai_satuan,
                    'Efisiensi': item['Efisiensi'] 
                })
        elif not item['Stackable'] and item['Jumlah'] > 0 : # Non-stackable juga dianggap 1 unit
             droppable_units.append({
                'Nama_Item': item['Nama_Item'],
                'Berat_Satuan': berat_satuan,
                'Nilai_Satuan': nilai_satuan,
                'Efisiensi': item['Efisiensi']
            })


    # Pengurutan droppable_units berdasarkan efisiensi (Ascending)
    # Item dengan berat 0 (efisiensi inf) ditempatkan di akhir
    droppable_units.sort(key=lambda x: x['Efisiensi'])

    current_weight = sum(item['Total_Berat_Item'] for item in initial_inventory_list)
    gold_bars_taken = 0
    value_of_dropped_items = 0
    dropped_item_details = [] # Melacak apa yang didrop

    # Constants untuk properti emas
    gold_bar_weight = 35
    gold_bar_value = 10005

    # 2. Fase Pengambilan Emas Awal (jika sudah ada ruang)
    while current_weight + gold_bar_weight <= carry_capacity and gold_bars_taken < 37: # 37 adalah max emas
        current_weight += gold_bar_weight
        gold_bars_taken += 1
        # print(f"DEBUG: Mengambil emas awal ke-{gold_bars_taken}, berat sekarang: {current_weight:.2f}")


    # 3. Fase Drop Item untuk membuat ruang, lalu ambil emas
    for unit_to_drop in droppable_units:
        if gold_bars_taken >= 37:
            break

        # Cek apakah perlu drop item untuk mengambil emas lagi
        if current_weight + gold_bar_weight <= carry_capacity:
             while current_weight + gold_bar_weight <= carry_capacity and gold_bars_taken < 37:
                current_weight += gold_bar_weight
                gold_bars_taken += 1
             continue

        # Simulasi drop
        potential_new_weight = current_weight - unit_to_drop['Berat_Satuan']
        
        if unit_to_drop['Berat_Satuan'] <= 0:
            continue # Lewati item berat 0

        # Lakukan drop
        current_weight = potential_new_weight
        value_of_dropped_items += unit_to_drop['Nilai_Satuan']
        dropped_item_details.append(unit_to_drop['Nama_Item'])
        # print(f"DEBUG: Drop {unit_to_drop['Nama_Item']}, nilai drop: {value_of_dropped_items}, berat: {current_weight:.2f}")


        # Coba ambil emas lagi
        while current_weight + gold_bar_weight <= carry_capacity and gold_bars_taken < 37:
            current_weight += gold_bar_weight
            gold_bars_taken += 1
            # print(f"DEBUG: Mengambil emas (setelah drop) ke-{gold_bars_taken}, berat: {current_weight:.2f}")


    final_profit = (gold_bars_taken * gold_bar_value) - value_of_dropped_items
    
    # Hapus duplikat nama item dan sum
    final_dropped_summary = {}
    for name in dropped_item_details:
        final_dropped_summary[name] = final_dropped_summary.get(name, 0) + 1
    
    # return gold_bars_taken, final_dropped_summary, final_profit, value_of_dropped_items, droppable_units
    return gold_bars_taken, final_dropped_summary, final_profit, value_of_dropped_items

# --- FUNGSI HELPER UNTUK MENJALANKAN DAN MENCETAK HASIL ---
def run_and_print_greedy_test(test_name, inventory, capacity):
    print(f"\n==================== {test_name} ====================")
    
    if not inventory:
        print("Inventory tidak valid. Tes dilewati.")
        return

    print(f"Kapasitas Bawa: {capacity} lbs, Jumlah jenis item: {len(inventory)}")
    
    for item in inventory:
        if 'Total_Berat_Item' not in item:
            item['Total_Berat_Item'] = item['Berat_Satuan'] * item['Jumlah']
        if 'Total_Nilai_Item' not in item:
            item['Total_Nilai_Item'] = item['Nilai_Satuan'] * item['Jumlah']
    
    print("\nMemulai Greedy Optimization...")
    
    start_time = time.time()
    gold_taken, items_dropped, profit, val_dropped = greedy_optimization(inventory, capacity)
    end_time = time.time()
    
    execution_time = end_time - start_time

    print("\n--- Hasil Optimasi Greedy ---")
    print(f"Waktu Eksekusi: {execution_time:.4f} detik")
    print(f"Emas Batangan Diambil: {gold_taken}")
    print("Item yang Dikorbankan:")
    if items_dropped:
        for name, count in items_dropped.items():
            print(f"- {name} (x{count})")
    else:
        print("- Tidak ada item yang dikorbankan.")
    print(f"Total Nilai Item Dikorbankan: {val_dropped}")
    print(f"PROFIT BERSIH: {profit} Caps")
    print("=======================================================")


# --- BAGIAN EKSEKUSI UTAMA ---
if __name__ == "__main__":

    from testcases import test_cases, hard_testcases

    print("---------------MENJALANKAN TESTCASES UTAMA---------------")
    for test in test_cases:
        for item in test['inventory']:
            item['Total_Berat_Item'] = item['Berat_Satuan'] * item['Jumlah']
            item['Total_Nilai_Item'] = item['Nilai_Satuan'] * item['Jumlah']

    for test in test_cases:
        run_and_print_greedy_test(test['name'], test['inventory'], test['capacity'])


    print("---------------MENJALANKAN HARD TESTCASES---------------")
    for hard_test in hard_testcases:
        for item in hard_test['inventory']:
            item['Total_Berat_Item'] = item['Berat_Satuan'] * item['Jumlah']
            item['Total_Nilai_Item'] = item['Nilai_Satuan'] * item['Jumlah']

    for hard_test in hard_testcases:
        run_and_print_greedy_test(hard_test['name'], hard_test['inventory'], hard_test['capacity'])

