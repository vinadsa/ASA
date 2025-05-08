def solve():
    n, m, q = map(int, input().split())
    a_costs = list(map(int, input().split())) # Biaya warp Ai untuk planet i+1

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    travel_sequence = list(map(int, input().split()))
    
    # Ubah urutan planet menjadi 0-indexed
    travel_sequence = [p - 1 for p in travel_sequence]

    memo_components = {} # Untuk menyimpan komponen yang sudah dihitung

    def get_connected_component(start_node):
        if start_node in memo_components:
            # Cek apakah komponen yang tersimpan masih valid
            # (misal, jika adj list bisa berubah antar pemanggilan, tapi di sini tidak)
            # Untuk kasus ini, komponen tidak berubah, jadi bisa langsung return
            # Namun, untuk kejelasan, kita bisa hitung ulang atau pastikan tidak ada dependensi aneh
            # Untuk soal ini, lebih aman menghitung ulang jika ada keraguan,
            # tapi karena adj tetap, memoization sederhana bisa dipakai.
            # Untuk simplisitas, kita akan hitung ulang saja setiap kali jika tidak ingin kompleksitas memo
            pass # Lanjut ke perhitungan jika tidak pakai memo atau memo tidak ditemukan

        q_dfs = [start_node]
        visited_comp = {start_node}
        component_nodes = {start_node}
        
        head = 0
        while head < len(q_dfs):
            curr = q_dfs[head]
            head += 1
            for neighbor in adj[curr]:
                if neighbor not in visited_comp:
                    visited_comp.add(neighbor)
                    component_nodes.add(neighbor)
                    q_dfs.append(neighbor)
        return component_nodes

    total_travel_cost = 0

    for i in range(len(travel_sequence) - 1):
        planet_s_idx = travel_sequence[i]
        planet_e_idx = travel_sequence[i+1]

        if planet_s_idx == planet_e_idx:
            segment_cost = 0
        else:
            comp_s_nodes = get_connected_component(planet_s_idx)
            
            if planet_e_idx in comp_s_nodes: # Terhubung
                segment_cost = 0
            else: # Tidak terhubung
                min_a_in_comp_s = float('inf')
                for node_idx in comp_s_nodes:
                    min_a_in_comp_s = min(min_a_in_comp_s, a_costs[node_idx])
                
                comp_e_nodes = get_connected_component(planet_e_idx)
                min_a_in_comp_e = float('inf')
                for node_idx in comp_e_nodes:
                    min_a_in_comp_e = min(min_a_in_comp_e, a_costs[node_idx])
                
                segment_cost = min_a_in_comp_s + min_a_in_comp_e
        
        total_travel_cost += segment_cost
        
    print(total_travel_cost)

if __name__ == '__main__':
    solve()