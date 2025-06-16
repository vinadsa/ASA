import math
import sys
import copy
import time

sys.setrecursionlimit(3000)

try:
    from inventory_generator import generate_random_inventory # Jika diperlukan untuk testing random manual
    from greedy import greedy_optimization # Untuk implementasi greedy pada BnB
except ImportError:
    print("File 'inventory_generator.py' tidak ditemukan.")
    exit()

GOLD_BAR_WEIGHT = 35
GOLD_BAR_VALUE = 10005
MAX_GOLD_BARS = 37


class BnBSolver:
    """
    Algoritma Branch and Bound untuk mencari solusi optimal dalam memaksimalkan profit bersih
    dari pengambilan emas dengan mengorbankan item dari inventory.

    Strategi:
    1. Gunakan hasil algoritma Greedy sebagai initial bound (lower bound) untuk pruning yang lebih efektif.
    2. Urutkan item berdasarkan rasio nilai/berat (efisiensi) secara menurun untuk eksplorasi yang lebih baik.
    3. Untuk setiap item, buat cabang (branch) dengan semua kemungkinan jumlah yang akan di-drop (0 hingga jumlah maksimal).
    4. Pada setiap node, hitung upper bound optimis dengan asumsi sisa kapasitas diisi penuh dengan emas.
    5. Lakukan pruning jika upper bound tidak lebih baik dari solusi terbaik yang sudah ditemukan.
    6. Pada leaf node, hitung profit aktual dan update solusi terbaik jika ditemukan yang lebih optimal.
    7. Gunakan rekursi dengan batas kapasitas untuk menjelajahi semua kombinasi valid.
    """
    def __init__(self, initial_inventory, carry_capacity):
        self.initial_inventory = initial_inventory
        self.carry_capacity = carry_capacity
        self.unique_item_types = []
        
        self.max_profit = -float('inf')
        self.best_dropped_summary = {}
        self.best_gold_bars = 0
        self.best_dropped_value = 0
        self.nodes_visited = 0

    def _recursive_solve(self, current_index, current_weight_kept, current_value_dropped, current_dropped_config):
        self.nodes_visited += 1

        # --- Bounding ---
        # Asumsi semua sisa ruang diisi emas, dan tidak ada lagi item yang didrop.
        remaining_capacity_for_ub = self.carry_capacity - current_weight_kept
        if remaining_capacity_for_ub >= 0:
            optimistic_gold_bars = min(MAX_GOLD_BARS, math.floor(remaining_capacity_for_ub / GOLD_BAR_WEIGHT)) if GOLD_BAR_WEIGHT > 0 else MAX_GOLD_BARS
            optimistic_profit = (optimistic_gold_bars * GOLD_BAR_VALUE) - current_value_dropped
            if optimistic_profit <= self.max_profit:
                return # Prune
        else:
            return # Melebihi kapasitas

        # --- Base Case ---
        if current_index == len(self.unique_item_types):
            remaining_capacity = self.carry_capacity - current_weight_kept
            gold_taken = min(MAX_GOLD_BARS, math.floor(remaining_capacity / GOLD_BAR_WEIGHT)) if GOLD_BAR_WEIGHT > 0 else MAX_GOLD_BARS
            
            final_profit = (gold_taken * GOLD_BAR_VALUE) - current_value_dropped
            if final_profit > self.max_profit:
                self.max_profit = final_profit
                self.best_gold_bars = gold_taken
                self.best_dropped_summary = current_dropped_config.copy()
                self.best_dropped_value = current_value_dropped
            return

        # --- Branching ---
        item_type = self.unique_item_types[current_index]
        for num_to_drop in range(item_type['Jumlah'] + 1):
            num_to_keep = item_type['Jumlah'] - num_to_drop
            
            weight_added_by_kept = num_to_keep * item_type['Berat_Satuan']
            value_added_to_dropped = num_to_drop * item_type['Nilai_Satuan']
            
            if current_weight_kept + weight_added_by_kept <= self.carry_capacity:
                next_dropped_config = current_dropped_config.copy()
                if num_to_drop > 0:
                    next_dropped_config[item_type['Nama_Item']] = num_to_drop

                self._recursive_solve(
                    current_index + 1,
                    current_weight_kept + weight_added_by_kept,
                    current_value_dropped + value_added_to_dropped,
                    next_dropped_config
                )

    def solve(self, use_greedy_initial_bound=True):
        self.max_profit = -float('inf')
        self.nodes_visited = 0
        
        if use_greedy_initial_bound:
            try:
                greedy_gold, greedy_dropped, greedy_profit, greedy_dropped_value = greedy_optimization(copy.deepcopy(self.initial_inventory), self.carry_capacity)
                self.max_profit = greedy_profit
                self.best_gold_bars = greedy_gold
                self.best_dropped_summary = greedy_dropped
                self.best_dropped_value = greedy_dropped_value
                print(f"DEBUG BnB: Inisialisasi dengan hasil Greedy - Gold: {greedy_gold}, Dropped Value: {greedy_dropped_value}, Profit: {self.max_profit}")
            except Exception as e:
                print(f"DEBUG BnB: Gagal mendapatkan initial bound dari Greedy. Melanjutkan tanpa: Error: {e}")
                pass

        self.unique_item_types = copy.deepcopy(self.initial_inventory)
        for item in self.unique_item_types:
            item['Ratio_Value_Weight'] = (item['Nilai_Satuan'] / item['Berat_Satuan']) if item['Berat_Satuan'] > 0 else float('inf')
        
        # Pengurutan berdasarkan rasio
        self.unique_item_types.sort(key=lambda x: x['Ratio_Value_Weight'], reverse=True)
        
        start_time = time.time()
        self._recursive_solve(0, 0, 0, {})
        end_time = time.time()
        
        execution_time = end_time - start_time
        
        return self.best_gold_bars, self.best_dropped_summary, self.max_profit, self.best_dropped_value, execution_time, self.nodes_visited

# --- FUNGSI HELPER UNTUK MENJALANKAN DAN MENCETAK HASIL ---
def run_and_print_bnb_test(test_name, inventory, capacity):
    print(f"\n==================== {test_name} ====================")
    
    if not inventory:
        print("Inventory tidak valid. Tes dilewati.")
        return

    print(f"Kapasitas Bawa: {capacity} lbs")
    print(f"Jumlah jenis item unik: {len(inventory)}")
    
    bnb_solver = BnBSolver(inventory, capacity)
    
    print("\nMemulai Branch and Bound...")
    
    gold_taken, items_dropped, profit, val_dropped, exec_time, nodes = bnb_solver.solve(use_greedy_initial_bound=True)

    print("\n--- Hasil Optimasi Branch and Bound ---")
    print(f"Waktu Eksekusi: {exec_time:.4f} detik")
    print(f"Jumlah Node Dikunjungi: {nodes}")
    print(f"Emas Batangan Diambil: {gold_taken}")
    print("Item yang Dikorbankan (Optimal):")
    if items_dropped:
        for name, count in items_dropped.items():
            print(f"- {name} (x{count})")
    else:
        print("- Tidak ada item yang dikorbankan.")
    print(f"Total Nilai Item Dikorbankan: {val_dropped}")
    print(f"PROFIT BERSIH (Optimal): {profit} Caps")
    print("====================================================")


# --- BAGIAN EKSEKUSI UTAMA ---
if __name__ == "__main__":

    from testcases import test_cases, hard_testcases

    print("---------------MENJALANKAN TESTCASES UTAMA---------------")
    for test in test_cases:
        for item in test['inventory']:
            item['Total_Berat_Item'] = item['Berat_Satuan'] * item['Jumlah']
            item['Total_Nilai_Item'] = item['Nilai_Satuan'] * item['Jumlah']
    
    for test in test_cases:
        run_and_print_bnb_test(test['name'], test['inventory'], test['capacity'])


    print("---------------MENJALANKAN HARD TESTCASES---------------")
    for hard_test in hard_testcases:
        for item in hard_test['inventory']:
            item['Total_Berat_Item'] = item['Berat_Satuan'] * item['Jumlah']
            item['Total_Nilai_Item'] = item['Nilai_Satuan'] * item['Jumlah']

    for hard_test in hard_testcases:
        run_and_print_bnb_test(hard_test['name'], hard_test['inventory'], hard_test['capacity'])
