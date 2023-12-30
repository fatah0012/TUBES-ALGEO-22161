import numpy as np 


def main():
    while True:
        print("\nMENU")
        print("1. Penjumlahan dan Pengurangan Matriks")
        print("2. Matriks Transpose")
        print("3. Matriks Balikan")
        print("4. Determinan")
        print("5. Sistem Persamaan Linier")
        print("6. Keluar")

        choice = input("Pilih (1-6)    : ")

        if choice == '1':
            print("---Penjumlahan dan Pengurangan Matriks 2x2---")
            print("1. Penjumlahan matriks")
            print("2. Pengurangan matriks")
            sub_choice = input("Pilih (1-2)    : ")

            if sub_choice == '1':
                penjumlahan_matriks()
            elif sub_choice == '2':
                pengurangan_matriks()
            else:
                print("\nPilihan tidak valid.")

        elif choice == '2':
            print("---Matriks Transpose---")
            print("1. Matriks 2x2")
            print("2. Matriks 3x3")
            sub_choice = input("Pilih (1-2)    : ")

            if sub_choice == '1':
                matriks_transpose_1()
            elif sub_choice == '2':
                matriks_transpose_2()
            else:
                print("Pilihan tidak valid.")

        elif choice == '3':
            matriks_balikan()

        elif choice == '4':
            print("---Determinan---")
            print("1. Matriks 2x2")
            print("2. Matriks 3x3")
            sub_choice = input("Pilih (1-2)    : ")

            if sub_choice == '1':
                determinan_matriks_1()
            elif sub_choice == '2':
                determinan_matriks_2()
            else:
                print("Pilihan tidak valid.")

        elif choice == '5':
            sistem_persamaan_linier()

        elif choice == '6':
            print("Keluar dari aplikasi. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih angka 1-6.")

def penjumlahan_matriks():
    print("--Masukkan elemen matriks pertama--\n(pisahkan kolom dengan spasi, baris dengan enter)  :")
    
    row1_matrix1 = input().split()
    if len(row1_matrix1) != 2:
        return
    row2_matrix1 = input().split()
    if len(row2_matrix1) != 2:
        return
    
    matrix1 = [
        [int(row1_matrix1[0]), int(row1_matrix1[1])],
        [int(row2_matrix1[0]), int(row2_matrix1[1])]
    ]

    print("--Masukkan elemen matriks kedua--\n(pisahkan kolom dengan spasi, baris dengan enter)  :")
    
    row1_matrix2 = input().split()
    if len(row1_matrix2) != 2:
        return
    row2_matrix2 = input().split()
    if len(row2_matrix2) != 2:
        return

    matrix2 = [
        [int(row1_matrix2[0]), int(row1_matrix2[1])],
        [int(row2_matrix2[0]), int(row2_matrix2[1])]
    ]

    result_matrix = [[matrix1[i][j] + matrix2[i][j] 
    for j in range(len(matrix1[0]))] 
    for i in range(len(matrix1))]

    print("Hasil penjumlahan matriks   :")
    for row in result_matrix:
        print(row)
    pass

def pengurangan_matriks():
    print("--Masukkan elemen matriks pertama--\n(pisahkan kolom dengan spasi, baris dengan enter)  :")
    
    row1_matrix1 = input().split()
    if len(row1_matrix1) != 2:
        return
    row2_matrix1 = input().split()
    if len(row2_matrix1) != 2:
        return
    
    matrix1 = [
        [int(row1_matrix1[0]), int(row1_matrix1[1])],
        [int(row2_matrix1[0]), int(row2_matrix1[1])]
    ]

    print("--Masukkan elemen matriks kedua--\n(pisahkan kolom dengan spasi, baris dengan enter)  :")
    row1_matrix2 = input().split()
    if len(row1_matrix2) != 2:
        return
    row2_matrix2 = input().split()
    if len(row2_matrix2) != 2:
        return

    matrix2 = [
        [int(row1_matrix2[0]), int(row1_matrix2[1])],
        [int(row2_matrix2[0]), int(row2_matrix2[1])]
    ]

    result_matrix = [[matrix1[i][j] - matrix2[i][j] 
    for j in range(len(matrix1[0]))] 
    for i in range(len(matrix1))]

    print("Hasil pengurangan matriks   :")
    for row in result_matrix:
        print(row)
    pass

def matriks_transpose_1():
    print("--Masukkan elemen matriks 2x2--\n(pisahkan kolom dengan spasi, baris dengan enter)  :")
    
    row1 = input().split()
    if len(row1) != 2:
        return
    row2 = input().split()
    if len(row2) != 2:
        return
    
    matrix = [[int(row1[0]), int(row1[1])], [int(row2[0]), int(row2[1])]]

    transposed_matrix = [[matrix[j][i] 
    for j in range(len(matrix))] 
    for i in range(len(matrix[0]))]

    print("Matriks transpose   :")
    for row in transposed_matrix:
        print(row)

def matriks_transpose_2():
    print("--Masukkan elemen matriks 3x3--\n(pisahkan kolom dengan spasi, baris dengan enter)  :")
    
    row1 = input().split()
    if len(row1) != 3:
        return
    row2 = input().split()
    if len(row2) != 3:
        return
    row3 = input().split()
    if len(row3) != 3:
        return
    
    matrix = [
        [int(row1[0]), int(row1[1]), int(row1[2])],
        [int(row2[0]), int(row2[1]), int(row2[2])],
        [int(row3[0]), int(row3[1]), int(row3[2])]
    ]

    transposed_matrix = [[matrix[j][i] 
    for j in range(len(matrix))] 
    for i in range(len(matrix[0]))]

    print("Hasil Matriks transpose   :")
    for row in transposed_matrix:
        print(row)

def matriks_balikan():
    print("---Matriks Balikan---\n--Masukkan elemen matriks 2x2--\n(pisahkan kolom dengan spasi, baris dengan enter)  :")
    
    row1 = input().split()
    if len(row1) != 2:
        return
    row2 = input().split()
    if len(row2) != 2:
        return
    
    matrix = [
        [float(row1[0]), float(row1[1])],
        [float(row2[0]), float(row2[1])]
    ]

    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    if determinant == 0:
        print("\nMatriks tidak memiliki invers karena determinan adalah nol.")
        return

    inverse_matrix = [
        [matrix[1][1] / determinant, -matrix[0][1] / determinant],
        [-matrix[1][0] / determinant, matrix[0][0] / determinant]
    ]

    print("Hasil Matriks inverse   :")
    for row in inverse_matrix:
        print(row)
        pass

def determinan_matriks_1():  

    print("--Masukkan elemen matriks 2x2--\n(pisahkan kolom dengan spasi, baris dengan enter)  :")

    row1 = input().split()
    if len(row1) != 2:
        return
    row2 = input().split()
    if len(row2) != 2:
        return

    matrix = [
        [float(row1[0]), float(row1[1])],
        [float(row2[0]), float(row2[1])]
    ]

    print("Matriks:")
    for row in matrix:
        print(row)

    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    print("Determinan matriks nya adalah   :", determinant)
    pass

def determinan_matriks_2():  
    print("--Masukkan elemen matriks 3x3--\n(pisahkan kolom dengan spasi, baris dengan enter)  :")

    row1 = input().split()
    if len(row1) != 3:
        return
    row2 = input().split()
    if len(row2) != 3:
        return
    row3 = input().split()
    if len(row3) != 3:
        return

    matrix = [
        [float(row1[0]), float(row1[1]), float(row1[2])],
        [float(row2[0]), float(row2[1]), float(row2[2])],
        [float(row3[0]), float(row3[1]), float(row3[2])]
    ]

    print("Matriks:")
    for row in matrix:
        print(row)

    determinant = (
        matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
        matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
        matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
    )

    print("Determinan matriks nya adalah   :", determinant)
    
def sistem_persamaan_linier():

    print("---Sistem Persamaan Linier---\n--Masukkan matriks 2x3-- \n(pisahkan kolom dengan spasi, baris dengan enter)  :")

    row1 = input().split()
    if len(row1) != 3:
        return
    row2 = input().split()
    if len(row2) != 3:
        return

    augmented_matrix = np.array([
        [float(row1[0]), float(row1[1]), float(row1[2])],
        [float(row2[0]), float(row2[1]), float(row2[2])]
    ])

    try:
        solution = np.linalg.solve(augmented_matrix[:, :2], augmented_matrix[:, 2])
        print("Solusi x, y   :")
        print(solution)
        
    except np.linalg.LinAlgError:
        print("Sistem persamaan linier tidak memiliki solusi unik.")
    pass

if __name__ == "__main__":
    main()
