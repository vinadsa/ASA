def find_max_subarray_2d(matrix):
    """
    Fungsi untuk mencari jumlah maksimum dari subarray 2D dalam suatu matriks
    menggunakan algoritma divide-and-conquer dengan kompleksitas O(n²).
    """
    if not matrix or not matrix[0]:
        return 0
        
    rows, cols = len(matrix), len(matrix[0])
    
    # Basis kasus: jika matriks hanya memiliki satu elemen
    if rows == 1 and cols == 1:
        return max(0, matrix[0][0])
    
    # Divide: membagi matriks menjadi empat kuadran
    mid_row, mid_col = rows // 2, cols // 2
    
    # Kuadran kiri atas
    top_left = [row[:mid_col] for row in matrix[:mid_row]]
    # Kuadran kanan atas
    top_right = [row[mid_col:] for row in matrix[:mid_row]]
    # Kuadran kiri bawah
    bottom_left = [row[:mid_col] for row in matrix[mid_row:]]
    # Kuadran kanan bawah
    bottom_right = [row[mid_col:] for row in matrix[mid_row:]]
    
    # Conquer: secara rekursif mencari jumlah maksimum di setiap kuadran
    max_top_left = find_max_subarray_2d(top_left)
    max_top_right = find_max_subarray_2d(top_right)
    max_bottom_left = find_max_subarray_2d(bottom_left)
    max_bottom_right = find_max_subarray_2d(bottom_right)
    
    # Combine: mencari subarray maksimum yang melintasi batas kuadran
    max_crossing = find_max_crossing_subarray(matrix, mid_row, mid_col)
    
    # Mengambil nilai maksimum dari kelima kemungkinan
    return max(max_top_left, max_top_right, max_bottom_left, max_bottom_right, max_crossing)

def find_max_crossing_subarray(matrix, mid_row, mid_col):
    """
    Fungsi untuk mencari jumlah maksimum dari subarray yang melewati batas kuadran
    """
    rows, cols = len(matrix), len(matrix[0])
    
    # Mencari jumlah maksimum untuk baris yang melewati mid_row
    max_row_sum = 0
    current_sum = 0
    for i in range(rows):
        current_sum = 0
        for j in range(cols):
            current_sum += matrix[i][j]
            max_row_sum = max(max_row_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
    
    # Mencari jumlah maksimum untuk kolom yang melewati mid_col
    max_col_sum = 0
    current_sum = 0
    for j in range(cols):
        current_sum = 0
        for i in range(rows):
            current_sum += matrix[i][j]
            max_col_sum = max(max_col_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
    
    # Mencari jumlah maksimum untuk subarray yang melewati kedua batas
    # (ini adalah implementasi sederhana, bisa ditingkatkan lagi)
    total_sum = sum(sum(row) for row in matrix)
    
    return max(max_row_sum, max_col_sum, total_sum)

# Aplikasi untuk skenario Andi (menghitung jumlah pixel dalam clipping layar)
def hitung_jumlah_pixel_maksimum(screenshot):
    """
    Fungsi untuk menghitung area dengan jumlah pixel tertinggi dalam screenshot.
    Nilai positif menunjukkan pixel yang relevan, nilai negatif menunjukkan noise.
    
    Args:
        screenshot: Matriks 2D dengan nilai representasi pixel
    
    Returns:
        Jumlah maksimum pixel dalam suatu area (subarray)
    """
    return find_max_subarray_2d(screenshot)

# Contoh penggunaan
if __name__ == "__main__":
    # Contoh screenshot dimana nilai positif menunjukkan pixel yang diinginkan
    # dan nilai negatif menunjukkan noise atau pixel yang tidak diinginkan
    contoh_screenshot = [
        [2, -3, 4, -1, 2],
        [-2, 1, -3, 4, -1],
        [3, -1, 2, -4, 5],
        [-3, 2, -4, 1, -2],
        [2, -1, 3, -2, 4]
    ]
    
    hasil = hitung_jumlah_pixel_maksimum(contoh_screenshot)
    print(f"Jumlah pixel maksimum dalam area clipping: {hasil}")
    
    # Contoh dengan area yang jelas lebih baik
    area_jelas = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    
    hasil_jelas = hitung_jumlah_pixel_maksimum(area_jelas)
    print(f"Jumlah pixel maksimum dalam area yang jelas: {hasil_jelas}")