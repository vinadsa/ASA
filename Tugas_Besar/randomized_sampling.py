import random
import copy
import time
import math

try:
    from inventory_generator import generate_random_inventory # Jika diperlukan untuk testing random manual
except ImportError:
    print("File 'inventory_generator.py' tidak ditemukan.")
    exit()

GOLD_BAR_WEIGHT = 35
GOLD_BAR_VALUE = 10005
MAX_GOLD_BARS = 37

def randomized_sampling_optimization(initial_inventory, carry_capacity, num_iterations=10000):
    """
    Algoritma Randomized Sampling untuk mencari solusi "cukup baik" dengan cepat.

    Strategi:
    1. Lakukan N iterasi.
    2. Di setiap iterasi, tentukan target emas acak.
    3. Pisahkan item secara acak menjadi "pasti disimpan" dan "kandidat drop".
    4. Mencoba memenuhi target dengan membuang kandidat drop yang paling tidak efisien.
    5. Evaluasi profit dan simpan solusi terbaik yang ditemukan.
    """
    start_time = time.time()
    
    best_profit = -float('inf')
    best_gold_bars = 0
    best_dropped_summary = {}
    best_dropped_value = 0
    
    # Hitung dulu rasio untuk semua item sekali saja untuk efisiensi
    inventory_with_ratio = copy.deepcopy(initial_inventory)
    for item in inventory_with_ratio:
        item['Ratio_Value_Weight'] = (item['Nilai_Satuan'] / item['Berat_Satuan']) if item['Berat_Satuan'] > 0 else float('inf')

    # Loop Utama
    for _ in range(num_iterations):
        # --- 1. Menghasilkan satu konfigurasi/solusi acak ---
        # Menentukan target emas acak
        target_gold_bars = random.randint(1, MAX_GOLD_BARS)
        space_needed_for_gold = target_gold_bars * GOLD_BAR_WEIGHT
        
        # Memisah item menjadi 'keep' dan 'candidates for drop' secara acak
        items_to_keep = []
        candidate_items_for_dropping = []
        for item_type in inventory_with_ratio:
            # 50% probability untuk jadi kandidat drop
            if random.random() < 0.5:
                candidate_items_for_dropping.append(item_type)
            else:
                items_to_keep.append(item_type)
        
        # Menghitung state awal dari item yang 'pasti disimpan'
        weight_of_kept_items = sum(item['Berat_Satuan'] * item['Jumlah'] for item in items_to_keep)
        
        # Solusi tidak valid jika item yang 'kept/disimpan' sudah melebihi kapasitas
        if weight_of_kept_items > carry_capacity:
            continue
            
        # Menghitung berapa banyak ruang yang harus dibuat
        total_initial_weight = weight_of_kept_items + sum(item['Berat_Satuan'] * item['Jumlah'] for item in candidate_items_for_dropping)
        space_to_create = (total_initial_weight + space_needed_for_gold) - carry_capacity
        
        current_dropped_value = 0
        current_dropped_summary = {}

        # Ruang cukup, tidak perlu drop apa-apa
        if space_to_create <= 0:
            pass # Skip ke evaluasi dengan 0 drop
        else:
            # --- 2. Coba memenuhi target dengan membuang kandidat ---
            droppable_units = []
            for item_type in candidate_items_for_dropping:
                for _ in range(item_type['Jumlah']):
                    droppable_units.append({
                        'Nama_Item': item_type['Nama_Item'],
                        'Berat_Satuan': item_type['Berat_Satuan'],
                        'Nilai_Satuan': item_type['Nilai_Satuan'],
                        'Efisiensi': item_type['Ratio_Value_Weight']
                    })
            
            droppable_units.sort(key=lambda x: x['Efisiensi'])
            
            weight_created = 0
            possible = False
            for unit in droppable_units:
                weight_created += unit['Berat_Satuan']
                current_dropped_value += unit['Nilai_Satuan']
                current_dropped_summary[unit['Nama_Item']] = current_dropped_summary.get(unit['Nama_Item'], 0) + 1
                
                if weight_created >= space_to_create:
                    possible = True
                    break
            
            if not possible:
                continue

        # --- 3. Evaluasi solusi valid yang dihasilkan ---
        final_weight_of_kept_items = total_initial_weight - current_dropped_value # Ini salah, harusnya berat
        weight_of_dropped_items_calc = sum(item['Berat_Satuan'] * count for name, count in current_dropped_summary.items() for item in inventory_with_ratio if item['Nama_Item'] == name)
        
        final_weight_of_items_on_player = total_initial_weight - weight_of_dropped_items_calc
        
        actual_space_left = carry_capacity - final_weight_of_items_on_player
        actual_gold_taken = 0
        if actual_space_left > 0:
            actual_gold_taken = min(target_gold_bars, math.floor(actual_space_left / GOLD_BAR_WEIGHT))

        current_profit = (actual_gold_taken * GOLD_BAR_VALUE) - current_dropped_value
        
        if current_profit > best_profit:
            best_profit = current_profit
            best_gold_bars = actual_gold_taken
            best_dropped_summary = current_dropped_summary
            best_dropped_value = current_dropped_value

    end_time = time.time()
    execution_time = end_time - start_time
    
    nodes_or_iterations = num_iterations
    
    return best_gold_bars, best_dropped_summary, best_profit, best_dropped_value, execution_time, nodes_or_iterations

# --- FUNGSI HELPER UNTUK MENJALANKAN DAN MENCETAK HASIL ---
def run_and_print_rs_test(test_name, inventory, capacity, iterations):
    print(f"\n==================== {test_name} (Iterasi: {iterations}) ====================")
    
    if not inventory:
        print("Inventory tidak valid. Tes dilewati.")
        return

    print(f"Kapasitas: {capacity} lbs, Jumlah jenis item: {len(inventory)}")
    
    print("\nMemulai Randomized Sampling...")
    
    gold_taken, items_dropped, profit, val_dropped, exec_time, nodes = randomized_sampling_optimization(
        inventory, capacity, iterations
    )

    print("\n--- Hasil Optimasi Randomized Sampling ---")
    print(f"Waktu Eksekusi: {exec_time:.4f} detik")
    print(f"Jumlah Iterasi Dilakukan: {nodes}")
    print(f"Emas Batangan Diambil: {gold_taken}")
    print("Item yang Dikorbankan (Solusi Terbaik Ditemukan):")
    if items_dropped:
        for name, count in items_dropped.items():
            print(f"- {name} (x{count})")
    else:
        print("- Tidak ada item yang dikorbankan.")
    print(f"Total Nilai Item Dikorbankan: {val_dropped}")
    print(f"PROFIT BERSIH TERBAIK: {profit} Caps")
    print("================================================================")

# --- BAGIAN EKSEKUSI UTAMA ---
if __name__ == "__main__":
    
    from testcases import test_cases, hard_testcases
    print("---------------MENJALANKAN TESTCASES UTAMA---------------")
    for test in test_cases:
        run_and_print_rs_test(test["name"], test["inventory"], test["capacity"], 1000)


    print("---------------MENJALANKAN HARD TESTCASES---------------")
    for hard_test in hard_testcases:
        run_and_print_rs_test(hard_test["name"], hard_test["inventory"], hard_test["capacity"], 1000)
