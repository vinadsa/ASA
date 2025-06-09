import math # Untuk float('inf')

# Asumsikan inventory_generator.py ada di direktori yang sama
# dan fungsi generate_random_inventory() sudah benar.
try:
    from inventory_generator import generate_random_inventory
except ImportError:
    print("Pastikan inventory_generator.py ada dan bisa diimpor.")
    exit()

def greedy_optimization(initial_inventory_list, carry_capacity):
    """
    Algoritma Greedy untuk memaksimalkan profit bersih dari pengambilan emas
    dengan mengorbankan item dari inventaris.

    Strategi Greedy:
    1. Prioritaskan mengambil emas jika sudah ada ruang.
    2. Jika tidak ada ruang, atau ingin mengambil lebih banyak emas,
       buang item dari inventaris dimulai dari yang paling tidak efisien
       (nilai/berat terendah) satu unit pada satu waktu.
    3. Setiap kali item dibuang dan ruang tercipta, coba ambil emas.
    4. Hanya lakukan drop dan ambil emas jika profit bersih tetap positif atau meningkat.
       (Untuk versi ini, kita akan lebih sederhana: drop untuk buat ruang, lalu isi emas)
    """
    
    # Buat salinan mendalam dari inventaris agar tidak mengubah original
    # dan agar bisa memodifikasi jumlah item
    current_inventory = []
    for item_orig in initial_inventory_list:
        current_inventory.append(item_orig.copy()) # Shallow copy per item dict cukup

    # 1. Tambahkan key efisiensi dan siapkan item untuk di-drop
    # Item yang akan di-drop akan dipecah menjadi unit-unit individual jika stackable
    droppable_units = []
    for item in current_inventory:
        berat_satuan = item['Berat_Satuan']
        nilai_satuan = item['Nilai_Satuan']
        # Hindari ZeroDivisionError jika berat adalah 0 (misal Uang Pra-Perang)
        # Item dengan berat 0 sangat efisien, jadi beri nilai inf agar tidak di-drop kecuali terpaksa
        item['Efisiensi'] = nilai_satuan / berat_satuan if berat_satuan > 0 else float('inf')
        
        # Untuk item stackable, pecah menjadi unit individual untuk dipertimbangkan drop
        # Ini menyederhanakan logika drop per unit
        if item['Stackable'] and item['Jumlah'] > 0 :
            for _ in range(item['Jumlah']):
                droppable_units.append({
                    'Nama_Item': item['Nama_Item'],
                    'Berat_Satuan': berat_satuan,
                    'Nilai_Satuan': nilai_satuan,
                    'Efisiensi': item['Efisiensi'] 
                    # Tidak perlu 'Jumlah' di sini karena ini unit tunggal
                })
        elif not item['Stackable'] and item['Jumlah'] > 0 : # Non-stackable juga dianggap 1 unit
             droppable_units.append({
                'Nama_Item': item['Nama_Item'],
                'Berat_Satuan': berat_satuan,
                'Nilai_Satuan': nilai_satuan,
                'Efisiensi': item['Efisiensi']
            })


    # Urutkan unit-unit yang bisa di-drop berdasarkan efisiensi (rendah ke tinggi)
    # Item dengan berat 0 (efisiensi inf) akan ada di akhir, jadi lebih aman.
    droppable_units.sort(key=lambda x: x['Efisiensi'])

    current_weight = sum(item['Total_Berat_Item'] for item in initial_inventory_list)
    gold_bars_taken = 0
    value_of_dropped_items = 0
    dropped_item_details = [] # Untuk melacak apa yang di-drop

    # Emas Batangan Properties
    gold_bar_weight = 35
    gold_bar_value = 10005

    # 2. Fase Pengambilan Emas Awal (jika sudah ada ruang)
    while current_weight + gold_bar_weight <= carry_capacity and gold_bars_taken < 37: # 37 adalah max emas
        current_weight += gold_bar_weight
        gold_bars_taken += 1
        # print(f"DEBUG: Mengambil emas awal ke-{gold_bars_taken}, berat sekarang: {current_weight:.2f}")


    # 3. Fase Drop Item untuk Membuat Ruang, lalu Ambil Emas
    # Kita akan iterasi melalui unit-unit yang bisa di-drop
    
    # Indeks untuk melacak unit mana yang sedang dipertimbangkan untuk di-drop
    # Ini untuk memastikan kita tidak terjebak membuang item berat 0
    # jika masih ada item berat > 0 yang bisa dibuang.
    # Namun, karena droppable_units sudah diurutkan berdasarkan efisiensi,
    # item berat 0 (efisiensi inf) akan ada di akhir.

    for unit_to_drop in droppable_units:
        # Jika kita sudah mengambil semua emas, berhenti
        if gold_bars_taken >= 37:
            break

        # Cek apakah perlu drop item untuk mengambil emas lagi
        # Jika sudah ada ruang untuk emas berikutnya, tidak perlu drop lagi untuk emas tersebut
        if current_weight + gold_bar_weight <= carry_capacity:
             # Ini seharusnya sudah ditangani fase 2, tapi sebagai safety
             while current_weight + gold_bar_weight <= carry_capacity and gold_bars_taken < 37:
                current_weight += gold_bar_weight
                gold_bars_taken += 1
                # print(f"DEBUG: Mengambil emas (post-drop check) ke-{gold_bars_taken}, berat: {current_weight:.2f}")
             continue # Cek lagi kondisi luar, mungkin sudah cukup emas/ruang

        # Jika tidak, kita *harus* drop item ini untuk *potensi* membuat ruang
        
        # Simulasikan drop
        potential_new_weight = current_weight - unit_to_drop['Berat_Satuan']
        
        # Hanya drop jika beratnya > 0. Item berat 0 tidak membantu membuat ruang.
        if unit_to_drop['Berat_Satuan'] <= 0:
            continue # Lewati item berat 0 jika kita butuh ruang

        # Lakukan drop
        current_weight = potential_new_weight
        value_of_dropped_items += unit_to_drop['Nilai_Satuan']
        dropped_item_details.append(unit_to_drop['Nama_Item']) # Bisa dibuat lebih detail jika perlu
        # print(f"DEBUG: Drop {unit_to_drop['Nama_Item']}, nilai drop: {value_of_dropped_items}, berat: {current_weight:.2f}")


        # Setelah drop, coba ambil emas lagi
        while current_weight + gold_bar_weight <= carry_capacity and gold_bars_taken < 37:
            current_weight += gold_bar_weight
            gold_bars_taken += 1
            # print(f"DEBUG: Mengambil emas (setelah drop) ke-{gold_bars_taken}, berat: {current_weight:.2f}")


    final_profit = (gold_bars_taken * gold_bar_value) - value_of_dropped_items
    
    # Hapus duplikat nama item yang di-drop untuk laporan yang lebih bersih
    # dan hitung jumlah masing-masing
    final_dropped_summary = {}
    for name in dropped_item_details:
        final_dropped_summary[name] = final_dropped_summary.get(name, 0) + 1
    
    return gold_bars_taken, final_dropped_summary, final_profit, value_of_dropped_items, droppable_units


# --- Contoh Penggunaan ---
if __name__ == "__main__":
    # Hasilkan inventaris sekali saja untuk konsistensi pengujian
    initial_player_inventory, player_capacity, player_strength = generate_random_inventory()

    if initial_player_inventory:
        print(f"--- Inventaris Awal (STR: {player_strength}, Kapasitas: {player_capacity} lbs) ---")
        total_initial_weight = 0
        total_initial_value = 0
        for item in initial_player_inventory:
            print(f"- {item['Nama_Item']} (x{item['Jumlah']}), Berat: {item['Total_Berat_Item']:.2f}, Nilai: {item['Total_Nilai_Item']}")
            total_initial_weight += item['Total_Berat_Item']
            total_initial_value += item['Total_Nilai_Item']
        print(f"Total Berat Awal: {total_initial_weight:.2f} lbs, Total Nilai Awal: {total_initial_value} Caps")
        print("--------------------------------------------------")

        gold_taken, items_dropped_summary, profit, total_value_dropped, droppable_units = greedy_optimization(
            initial_player_inventory,
            player_capacity
        )

        print("\n--- Hasil Optimasi Greedy ---")
        print(f"Emas Batangan Diambil: {gold_taken}")
        print(f"Total Nilai Emas: {gold_taken * 10005}")
        print("Item yang Dikorbankan:")
        if items_dropped_summary:
            for name, count in items_dropped_summary.items():
                print(f"- {name} (x{count})")
        else:
            print("- Tidak ada item yang dikorbankan.")
        print(f"Total Nilai Item Dikorbankan: {total_value_dropped}")
        print(f"PROFIT BERSIH: {profit} Caps")
        
        # Verifikasi berat akhir (opsional)
        # Berat item yang tersisa + berat emas =< kapasitas
        remaining_inventory_weight = total_initial_weight
        for name, count in items_dropped_summary.items():
            # Cari berat satuan item yang di-drop
            # Ini agak rumit karena kita butuh master list lagi atau simpan berat satuan
            # Untuk simplifikasi, kita tidak hitung detail berat sisa di sini
            # Tapi bisa ditambahkan jika perlu verifikasi ketat
            pass
        final_calculated_weight = (total_initial_weight - sum(item_data['Berat_Satuan'] 
                                                            for item_data_list in 
                                                                [[d for d in droppable_units if d['Nama_Item'] == name][:count] 
                                                                for name, count in items_dropped_summary.items()] 
                                                            for item_data in item_data_list)
                                  ) + (gold_taken * 35)
        # print(f"Perkiraan Berat Akhir di Inventaris (Item Sisa + Emas): {final_calculated_weight:.2f} lbs (Kapasitas: {player_capacity} lbs)")
        # Validasi lebih sederhana:
        if final_calculated_weight > player_capacity + 0.1: # Toleransi kecil untuk float
             print(f"PERINGATAN: Perkiraan berat akhir ({final_calculated_weight:.2f}) mungkin melebihi kapasitas ({player_capacity})!")


    else:
        print("Gagal menghasilkan inventaris.")