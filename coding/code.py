# Disini saya menggunakan fenwick tree pada beberapa manipulasi list
# Fenwick, Peter M. 1994. “A New Data Structure for Cumulative Frequency Tables.” Software: Practice and Experience 24 (3): 327–36.
# Secara garis besar untuk kompleksitas dari fungsi yg saya buat adalah O(n^2) karena ada nested loop pada fungsi

from fenwick import FenwickTree

def totalCost(scores):
    """
    Fungsi totalCost. Menghitung total bonus yang didapatkan oleh karyawan
    input : list jumlah top skor dari jam pertama
    output : biaya yg dikeluarkan oleh perusahaan 
    """
    a = [] # inisialiasi array kosong
    n = len(scores)
    fenwick_tree = FenwickTree(n) # inisialiasi struktur data fenwick pada fenwick_tree
    for i in range(n):
        a.append(scores[i]) # menambahkan setiap elemen pada list scores satu-persatu ke array a
        max = scores[i] # pada setiap perulangan, nilai max adalah nilai maximum pada array
        for j in a: # looping untuk menghitung ada berapa elemen pada list a yang kurang dari max
            if j < max:
                fenwick_tree.add(i, 1) # update nilai fenwick tree
    return(fenwick_tree.prefix_sum(n) + (10*n))

if __name__ == '__main__':
    scores = [1874, 1339, 5617, 8331, 5424, 9667]
    x = totalCost(scores)
    print(x)
