import pandas as pd
import random

def generate_random_inventory(master_list_path="./MasterList Inventory.csv",
                              target_carry_capacity_percentage_min=0.70, # Minimal 70% kapasitas terisi
                              target_carry_capacity_percentage_max=0.95, # Maksimal 95% kapasitas terisi
                              base_carry_weight=150):
    """
    Menghasilkan inventaris acak untuk pemain berdasarkan master list item,
    dengan Strength (STR) acak dan kapasitas bawa yang disesuaikan.

    Args:
        master_list_path (str): Path ke file CSV master list item.
        target_carry_capacity_percentage_min (float): Persentase minimal kapasitas bawa
                                                      yang ingin diisi inventaris awal.
        target_carry_capacity_percentage_max (float): Persentase maksimal kapasitas bawa
                                                       yang ingin diisi inventaris awal.
        base_carry_weight (int): Berat bawa dasar pemain sebelum modifikasi STR.

    Returns:
        tuple: (player_inventory, actual_carry_capacity, strength_value)
               player_inventory (list): Daftar item di inventaris pemain, masing-masing
                                        item adalah dictionary {'Nama_Item': str,
                                                              'Jumlah': int,
                                                              'Berat_Satuan': float,
                                                              'Nilai_Satuan': int,
                                                              'Total_Berat_Item': float,
                                                              'Total_Nilai_Item': int,
                                                              'Kategori_Item': str,
                                                              'Stackable': bool}
               actual_carry_capacity (int): Kapasitas bawa pemain setelah STR.
               strength_value (int): Nilai STR pemain yang dirandom.
    """
    try:
        master_df = pd.read_csv(master_list_path)
    except FileNotFoundError:
        print(f"Error: File master list '{master_list_path}' tidak ditemukan.")
        return None, None, None
    except Exception as e:
        print(f"Error saat membaca CSV: {e}")
        return None, None, None

    # 1. Randomize Strength (STR) dan hitung Kapasitas
    strength_value = random.randint(1, 10)
    actual_carry_capacity = base_carry_weight + (strength_value * 10)

    # 2. menentukan target berat inventaris awal
    target_inventory_fill_percentage = random.uniform(target_carry_capacity_percentage_min,
                                                     target_carry_capacity_percentage_max)
    target_inventory_weight = actual_carry_capacity * target_inventory_fill_percentage

    player_inventory = []
    current_inventory_weight = 0
    available_items_df = master_df.copy()

    # 3. Proses Pemilihan Item
    max_attempts_to_add_item = len(master_df) * 5

    for _ in range(max_attempts_to_add_item):
        if current_inventory_weight >= target_inventory_weight:
            break

        if available_items_df.empty:
            break

        random_item_series = available_items_df.sample(n=1).iloc[0]

        item_name = random_item_series['Nama_Item']
        item_weight = random_item_series['Berat_Item']
        item_value = random_item_series['Nilai_Item']
        item_category = random_item_series['Kategori_Item']
        is_stackable = random_item_series['Stackable'] # CSV pakai TRUE/FALSE
        max_stack = random_item_series['Max_Stack_Jika_Stackable']

        num_to_add = 1
        if is_stackable:
            try:
                max_s = int(max_stack) if not pd.isna(max_stack) else 1
                num_to_add = random.randint(1, max(1, max_s))
            except ValueError:
                num_to_add = 1

        weight_of_items_to_add = item_weight * num_to_add

        if current_inventory_weight + weight_of_items_to_add <= actual_carry_capacity:
            existing_item_index = -1
            if is_stackable:
                for i, inv_item in enumerate(player_inventory):
                    if inv_item['Nama_Item'] == item_name:
                        existing_item_index = i
                        break
            
            if is_stackable and existing_item_index != -1:
                player_inventory[existing_item_index]['Jumlah'] += num_to_add
                player_inventory[existing_item_index]['Total_Berat_Item'] += weight_of_items_to_add
                player_inventory[existing_item_index]['Total_Nilai_Item'] += item_value * num_to_add
            else:
                player_inventory.append({
                    'Nama_Item': item_name,
                    'Jumlah': num_to_add,
                    'Berat_Satuan': item_weight,
                    'Nilai_Satuan': item_value,
                    'Total_Berat_Item': weight_of_items_to_add,
                    'Total_Nilai_Item': item_value * num_to_add,
                    'Kategori_Item': item_category,
                    'Stackable': is_stackable
                })

            current_inventory_weight += weight_of_items_to_add

            if not is_stackable:
                available_items_df = available_items_df[available_items_df['Nama_Item'] != item_name]
        
        elif not available_items_df[available_items_df['Berat_Item'] <= (actual_carry_capacity - current_inventory_weight)].empty:
            continue
        else:
            break

    
    return player_inventory, actual_carry_capacity, strength_value

if __name__ == "__main__":
    # HARUS PUNYA MasterList Inventory.csv
    generated_inventory, capacity, strength = generate_random_inventory()

    if generated_inventory:
        print(f"Nilai STR Pemain: {strength}")
        print(f"Kapasitas Bawa Aktual: {capacity} lbs")
        print("\nInventaris Pemain yang Dihasilkan:")
        total_berat_inv = 0
        total_nilai_inv = 0
        for item in generated_inventory:
            print(
                f"- {item['Nama_Item']} (x{item['Jumlah']}), "
                f"Total Berat: {item['Total_Berat_Item']:.2f} lbs, "
                f"Total Nilai: {item['Total_Nilai_Item']} Caps, "
                f"Kategori: {item['Kategori_Item']}, "
                f"Stackable: {item['Stackable']}"
            )
            total_berat_inv += item['Total_Berat_Item']
            total_nilai_inv += item['Total_Nilai_Item']
        
        print(f"\nTotal Berat Inventaris: {total_berat_inv:.2f} lbs")
        print(f"Total Nilai Inventaris: {total_nilai_inv} Caps")
        print(f"Persentase Kapasitas Terisi: {(total_berat_inv / capacity) * 100:.2f}%")

        emas_batangan_berat = 35
        emas_batangan_nilai = 10005
        print(f"\nInfo Emas Batangan Sierra Madre:")
        print(f"- Berat per Batang: {emas_batangan_berat} lbs")
        print(f"- Nilai per Batang: {emas_batangan_nilai} Caps")
        print(f"- Jumlah Batang Tersedia: 37")
        print(f"- Total Berat Semua Emas: {37 * emas_batangan_berat} lbs\n")

        for item in generated_inventory:
            print(item['Jumlah'])
            print("\n")