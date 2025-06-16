test_cases = [
    {
        "name": "Test Case 1: Normal",
        "capacity": 60,
        "inventory": [
            {'Nama_Item': 'Fat Man', 'Berat_Satuan': 30, 'Nilai_Satuan': 4000, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': 'Leather Armor', 'Berat_Satuan': 15, 'Nilai_Satuan': 120, 'Jumlah': 2, 'Stackable': False},
            {'Nama_Item': 'Stimpak', 'Berat_Satuan': 0.1, 'Nilai_Satuan': 75, 'Jumlah': 10, 'Stackable': True},
        ]
    },
    {
        "name": "Test Case 2: Kompleks",
        "capacity": 80,
        "inventory": [
            {'Nama_Item': 'Service Rifle', 'Berat_Satuan': 7, 'Nilai_Satuan': 800, 'Jumlah': 2, 'Stackable': False},
            {'Nama_Item': 'Combat Armor', 'Berat_Satuan': 25, 'Nilai_Satuan': 800, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': 'Mini Nuke', 'Berat_Satuan': 6, 'Nilai_Satuan': 500, 'Jumlah': 5, 'Stackable': True},
            {'Nama_Item': 'Scrap Metal', 'Berat_Satuan': 2, 'Nilai_Satuan': 8, 'Jumlah': 10, 'Stackable': True},
        ]
    },
    {
        "name": "Test Case 3: Kapasitas Sangat Terbatas",
        "capacity": 40,
        "inventory": [
            {'Nama_Item': 'Fat Man', 'Berat_Satuan': 30, 'Nilai_Satuan': 4000, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': 'Sniper Rifle', 'Berat_Satuan': 8, 'Nilai_Satuan': 1500, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': 'Combat Armor', 'Berat_Satuan': 25, 'Nilai_Satuan': 800, 'Jumlah': 1, 'Stackable': False},
        ]
    },
    {
        "name": "Test Case 4: Banyak Item 'Sampah'",
        "capacity": 80,
        "inventory": [
            {'Nama_Item': 'Scrap Metal', 'Berat_Satuan': 2, 'Nilai_Satuan': 8, 'Jumlah': 25, 'Stackable': True},
            {'Nama_Item': 'Botol Nuka-Cola Kosong', 'Berat_Satuan': 0.5, 'Nilai_Satuan': 1, 'Jumlah': 30, 'Stackable': True},
            {'Nama_Item': 'Service Rifle', 'Berat_Satuan': 7, 'Nilai_Satuan': 800, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': '9mm Pistol', 'Berat_Satuan': 1.5, 'Nilai_Satuan': 150, 'Jumlah': 1, 'Stackable': False}
        ]
    },
    {
        "name": "Test Case 5: Dilema Berat vs. Nilai",
        "capacity": 100,
        "inventory": [
            {'Nama_Item': 'T-45d Power Armor', 'Berat_Satuan': 45, 'Nilai_Satuan': 1500, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': 'Service Rifle', 'Berat_Satuan': 7, 'Nilai_Satuan': 800, 'Jumlah': 4, 'Stackable': False},
            {'Nama_Item': 'Mini Nuke', 'Berat_Satuan': 6, 'Nilai_Satuan': 500, 'Jumlah': 5, 'Stackable': True},
        ]
    },
    {
        "name": "Test Case 6: Kapasitas Cukup (Trade-off Optimal)",
        "capacity": 80,
        "inventory": [
            {'Nama_Item': 'Service Rifle', 'Berat_Satuan': 7, 'Nilai_Satuan': 800, 'Jumlah': 2, 'Stackable': False},
            {'Nama_Item': 'Combat Armor', 'Berat_Satuan': 25, 'Nilai_Satuan': 800, 'Jumlah': 1, 'Stackable': False},
        ]
    },
    {
        "name": "Test Case 7: Full Inventory dari Generator(NO. 1)",
        "capacity": 180,
        "inventory": [
            {'Nama_Item': 'Karton Rokok', 'Berat_Satuan': 0.5, 'Nilai_Satuan': 50, 'Jumlah': 21, 'Stackable': True},
            {'Nama_Item': 'Botol Nuka-Cola Kosong', 'Berat_Satuan': 0.5, 'Nilai_Satuan': 1, 'Jumlah': 18, 'Stackable': True},
            {'Nama_Item': 'Rad-X', 'Berat_Satuan': 0.1, 'Nilai_Satuan': 40, 'Jumlah': 7, 'Stackable': True},
            {'Nama_Item': 'Metal Armor', 'Berat_Satuan': 30.0, 'Nilai_Satuan': 350, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': 'Mini Nuke', 'Berat_Satuan': 6.0, 'Nilai_Satuan': 500, 'Jumlah': 6, 'Stackable': True},
            {'Nama_Item': 'Bobby Pin', 'Berat_Satuan': 0.0, 'Nilai_Satuan': 1, 'Jumlah': 91, 'Stackable': True},
            {'Nama_Item': 'Combat Armor', 'Berat_Satuan': 25.0, 'Nilai_Satuan': 800, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': 'Pisau Lempar', 'Berat_Satuan': 0.5, 'Nilai_Satuan': 20, 'Jumlah': 1, 'Stackable': True},
            {'Nama_Item': 'Super Stimpak', 'Berat_Satuan': 0.1, 'Nilai_Satuan': 150, 'Jumlah': 11, 'Stackable': True},
            {'Nama_Item': 'Tas Dokter', 'Berat_Satuan': 2.0, 'Nilai_Satuan': 125, 'Jumlah': 5, 'Stackable': True},
            {'Nama_Item': 'Air Murni', 'Berat_Satuan': 1.0, 'Nilai_Satuan': 20, 'Jumlah': 46, 'Stackable': True}
        ]
    },
    {
        "name": "Test Case 8: Full Inventory dari Generator(NO. 2)",
        "capacity": 220,
        "inventory": [
            {'Nama_Item': '9mm Pistol', 'Berat_Satuan': 1.5, 'Nilai_Satuan': 150, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': 'Fat Man', 'Berat_Satuan': 30.0, 'Nilai_Satuan': 4000, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': 'Broc Flower', 'Berat_Satuan': 0.1, 'Nilai_Satuan': 5, 'Jumlah': 28, 'Stackable': True},
            {'Nama_Item': 'Nuka-Cola', 'Berat_Satuan': 1.0, 'Nilai_Satuan': 20, 'Jumlah': 1, 'Stackable': True},
            {'Nama_Item': 'Pisau Lempar', 'Berat_Satuan': 0.5, 'Nilai_Satuan': 20, 'Jumlah': 5, 'Stackable': True},
            {'Nama_Item': 'Karton Rokok', 'Berat_Satuan': 0.5, 'Nilai_Satuan': 50, 'Jumlah': 14, 'Stackable': True},
            {'Nama_Item': 'Air Murni', 'Berat_Satuan': 1.0, 'Nilai_Satuan': 20, 'Jumlah': 19, 'Stackable': True},
            {'Nama_Item': 'Tas Dokter', 'Berat_Satuan': 2.0, 'Nilai_Satuan': 125, 'Jumlah': 5, 'Stackable': True},
            {'Nama_Item': 'Scrap Metal', 'Berat_Satuan': 2.0, 'Nilai_Satuan': 8, 'Jumlah': 59, 'Stackable': True}
        ]
    },
    {
        "name": "Test Case 9: Full Inventory dari Generator(NO. 3)",
        "capacity": 190,
        "inventory": [
            {'Nama_Item': 'Peluru .308', 'Berat_Satuan': 0.03, 'Nilai_Satuan': 8, 'Jumlah': 14, 'Stackable': True},
            {'Nama_Item': 'Botol Nuka-Cola Kosong', 'Berat_Satuan': 0.5, 'Nilai_Satuan': 1, 'Jumlah': 23, 'Stackable': True},
            {'Nama_Item': 'Mini Nuke', 'Berat_Satuan': 6.0, 'Nilai_Satuan': 500, 'Jumlah': 2, 'Stackable': True},
            {'Nama_Item': 'Nuka-Cola', 'Berat_Satuan': 1.0, 'Nilai_Satuan': 20, 'Jumlah': 10, 'Stackable': True},
            {'Nama_Item': 'Super Stimpak', 'Berat_Satuan': 0.1, 'Nilai_Satuan': 150, 'Jumlah': 11, 'Stackable': True},
            {'Nama_Item': 'Sensor Module', 'Berat_Satuan': 1.0, 'Nilai_Satuan': 200, 'Jumlah': 23, 'Stackable': True},
            {'Nama_Item': 'Fat Man', 'Berat_Satuan': 30.0, 'Nilai_Satuan': 4000, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': '9mm Pistol', 'Berat_Satuan': 1.5, 'Nilai_Satuan': 150, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': 'Metal Armor', 'Berat_Satuan': 30.0, 'Nilai_Satuan': 350, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': 'Bobby Pin', 'Berat_Satuan': 0.0, 'Nilai_Satuan': 1, 'Jumlah': 42, 'Stackable': True},
            {'Nama_Item': 'Scrap Metal', 'Berat_Satuan': 2.0, 'Nilai_Satuan': 8, 'Jumlah': 27, 'Stackable': True}
        ]
    }
]

hard_testcases = [
    {
        "name": "HARD - Inventory 1",
        "capacity": 220,
        "inventory": [
            {'Nama_Item': 'RadAway', 'Berat_Satuan': 0.1, 'Nilai_Satuan': 100, 'Jumlah': 2, 'Stackable': True},
            {'Nama_Item': 'Stimpak', 'Berat_Satuan': 0.1, 'Nilai_Satuan': 75, 'Jumlah': 27, 'Stackable': True},
            {'Nama_Item': 'Mini Nuke', 'Berat_Satuan': 6.0, 'Nilai_Satuan': 500, 'Jumlah': 16, 'Stackable': True},
            {'Nama_Item': 'Super Stimpak', 'Berat_Satuan': 0.1, 'Nilai_Satuan': 150, 'Jumlah': 11, 'Stackable': True},
            {'Nama_Item': 'Metal Armor', 'Berat_Satuan': 30.0, 'Nilai_Satuan': 350, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': 'Service Rifle', 'Berat_Satuan': 7.0, 'Nilai_Satuan': 800, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': 'Tas Dokter', 'Berat_Satuan': 2.0, 'Nilai_Satuan': 125, 'Jumlah': 3, 'Stackable': True},
            {'Nama_Item': 'Karton Rokok', 'Berat_Satuan': 0.5, 'Nilai_Satuan': 50, 'Jumlah': 19, 'Stackable': True},
            {'Nama_Item': 'Sensor Module', 'Berat_Satuan': 1.0, 'Nilai_Satuan': 200, 'Jumlah': 11, 'Stackable': True},
            {'Nama_Item': 'Air Murni', 'Berat_Satuan': 1.0, 'Nilai_Satuan': 20, 'Jumlah': 37, 'Stackable': True},
            {'Nama_Item': 'Bobby Pin', 'Berat_Satuan': 0.0, 'Nilai_Satuan': 1, 'Jumlah': 72, 'Stackable': True},
            {'Nama_Item': 'Peluru 5.56mm', 'Berat_Satuan': 0.02, 'Nilai_Satuan': 4, 'Jumlah': 477, 'Stackable': True}
        ]
    },
    {
        "name": "HARD - Inventory 2",
        "capacity": 250,
        "inventory": [
            {'Nama_Item': 'Peluru 9mm', 'Berat_Satuan': 0.014, 'Nilai_Satuan': 1, 'Jumlah': 496, 'Stackable': True},
            {'Nama_Item': 'Scrap Metal', 'Berat_Satuan': 2.0, 'Nilai_Satuan': 8, 'Jumlah': 61, 'Stackable': True},
            {'Nama_Item': 'Bobby Pin', 'Berat_Satuan': 0.0, 'Nilai_Satuan': 1, 'Jumlah': 38, 'Stackable': True},
            {'Nama_Item': 'Uang Pra-Perang', 'Berat_Satuan': 0.0, 'Nilai_Satuan': 10, 'Jumlah': 734, 'Stackable': True},
            {'Nama_Item': 'RadAway', 'Berat_Satuan': 0.1, 'Nilai_Satuan': 100, 'Jumlah': 4, 'Stackable': True},
            {'Nama_Item': 'Peluru .308', 'Berat_Satuan': 0.03, 'Nilai_Satuan': 8, 'Jumlah': 132, 'Stackable': True},
            {'Nama_Item': 'Fat Man', 'Berat_Satuan': 30.0, 'Nilai_Satuan': 4000, 'Jumlah': 1, 'Stackable': False},
            {'Nama_Item': 'Karton Rokok', 'Berat_Satuan': 0.5, 'Nilai_Satuan': 50, 'Jumlah': 18, 'Stackable': True},
            {'Nama_Item': 'Stimpak', 'Berat_Satuan': 0.1, 'Nilai_Satuan': 75, 'Jumlah': 5, 'Stackable': True},
            {'Nama_Item': 'Nuka-Cola', 'Berat_Satuan': 1.0, 'Nilai_Satuan': 20, 'Jumlah': 21, 'Stackable': True},
            {'Nama_Item': 'T-45d Power Armor', 'Berat_Satuan': 45.0, 'Nilai_Satuan': 1500, 'Jumlah': 1, 'Stackable': False}
        ]
    }
]