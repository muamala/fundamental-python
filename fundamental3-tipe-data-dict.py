"""
Tipe data dictionary sekedar menghubungkan antara KEY dan Value
KVP = Key Value Pair
Dictionary = kamus
"""

kamus_ind_eng = {'anak': 'child', 'istri': 'wife', 'ayah': 'father', 'ibu': 'mother'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('Data ini dikirimkan oleh server Gojek, untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [{'nama': 'Faruq', 'Jarak': 10},
                    {'nama': 'Faris', 'Jarak': 30},
                    {'nama': 'Wildan', 'Jarak': 100},
                    {'nama': 'Syakur', 'Jarak': 1000}]
}
print(data_dari_server_gojek)
print(f"\nDriver di sekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['Jarak']} meter")