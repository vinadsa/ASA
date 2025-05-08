import math

def largest_values_in_tree_levels(nodes_list_str_repr):
    """
    Menemukan ukuran gambar terbesar di setiap tingkat koleksi pohon biner.

    Args:
        nodes_list_str_repr (str): String yang merepresentasikan node dalam bentuk level order,
                                   dengan "null" untuk node kosong, dipisahkan spasi.
                                   Contoh: "1 3 2 5 3 null 9"

    Returns:
        list: Sebuah list integer yang berisi ukuran gambar terbesar di setiap tingkat pohon.
    """
    # Jika string input kosong atau hanya berisi spasi, kembalikan list kosong.
    if not nodes_list_str_repr.strip():
        return []

    node_values_str = nodes_list_str_repr.split()
    m = len(node_values_str)

    # Jika setelah di-split tidak ada elemen (misalnya input string hanya spasi),
    # kembalikan list kosong.
    if m == 0:
        return []

    nodes = []
    for s_val in node_values_str:
        if s_val == "null":
            nodes.append(None)
        else:
            # Nilai node bisa negatif sesuai constraint
            nodes.append(int(s_val))

    result = []
    current_index = 0  # Indeks untuk iterasi melalui list 'nodes'
    level = 0          # Tingkat pohon saat ini (dimulai dari 0)

    while current_index < m:
        # Jumlah node maksimum yang mungkin ada di level ini secara teoretis
        # Level 0: 2^0 = 1 node
        # Level 1: 2^1 = 2 node
        # Level 2: 2^2 = 4 node, dst.
        num_nodes_theoretically_at_this_level = 1 << level # Sama dengan 2**level

        max_val_for_level = -float('inf') # Inisialisasi dengan nilai negatif tak terhingga
        found_node_in_level = False       # Flag apakah ada node non-null di level ini
        
        # Jumlah node aktual yang diproses dari list input untuk level ini
        nodes_processed_from_input_for_this_level = 0
        
        # Iterasi sebanyak jumlah node teoretis di level ini
        for i in range(num_nodes_theoretically_at_this_level):
            actual_node_idx_in_list = current_index + i
            
            # Pastikan tidak melebihi panjang list input 'nodes'
            if actual_node_idx_in_list < m:
                node_val = nodes[actual_node_idx_in_list]
                if node_val is not None:
                    if node_val > max_val_for_level:
                        max_val_for_level = node_val
                    found_node_in_level = True
                # Hitung node ini sebagai bagian dari slot yang diproses untuk level ini
                nodes_processed_from_input_for_this_level += 1
            else:
                # Sudah mencapai akhir dari list input, hentikan iterasi untuk level ini
                break 
        
        if found_node_in_level:
            result.append(max_val_for_level)
        
        # Pindahkan current_index sejumlah node yang telah diproses/dilihat untuk level ini
        current_index += nodes_processed_from_input_for_this_level
        
        # Jika tidak ada node yang diproses sama sekali dari input untuk iterasi level ini,
        # ini berarti semua node dari input telah dialokasikan ke level-level sebelumnya.
        # Kondisi `while current_index < m` akan menangani penghentian loop secara alami.
        if nodes_processed_from_input_for_this_level == 0:
             break # Semua node input telah dipertimbangkan.

        level += 1 # Pindah ke level berikutnya
        
    return result

if __name__ == '__main__':
    # Baris pertama: Jumlah node n 
    # (tidak secara langsung digunakan dalam logika inti jika baris kedua sudah definitif mengenai isinya)
    n_count_str = input() 
    # n_count = int(n_count_str) # Bisa dikonversi jika perlu validasi atau penggunaan lain

    # Baris kedua: List node dalam bentuk level order
    nodes_input_line = input()
    
    # Panggil fungsi untuk mendapatkan list hasil
    final_result_list = largest_values_in_tree_levels(nodes_input_line)
    
    if final_result_list:
        # Cetak list dengan elemen dipisahkan spasi
        print(*(str(x) for x in final_result_list))
    else:
        # Jika list hasil kosong (misal, untuk 0 node atau input kosong),
        # cetak baris kosong sesuai ekspektasi umum untuk output kosong.
        print("")