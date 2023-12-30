import numpy as mk

def menu():
    
        print("""
================MENU====================
1. Penjumlahan dan Pengurangan Matriks
2. Matriks Transpose
3. Matriks Balikan
4. Determinan
5. Sistem Persamaan Liner
6. Exit
========================================
""")
        pilihmenu = int(input("Pilih no di atas : "))
        if pilihmenu in range(1,7):
                return pilihmenu
        else:
                print("Tidak Diketahui ")
                

def no1():
    print("""1. Penjumlahan
2. Pengurangan""")
    pilih = int(input("Pilih no di atas : "))
    if pilih == 1:
            a11, a12, a21, a22 = map(float, input("Masukan Matriks A [a11 a12 a21 a22] : ").split())   
            b11, b12, b21, b22 = map(float, input("Masukan Matriks B [b11 b12 b21 b22] : ").split())
            
            m_a = mk.array([[a11, a12],
                            [a21, a22]])
            m_b = mk.array([[b11, b12],
                            [b21, b22]])
            hasil = m_a + m_b
            print(f"Hasil nya : \n{hasil}")
    
    elif pilih == 2:
            a11, a12, a21, a22 = map(float, input("Matriks A [a11 a12 a21 a22] : ").split())   
            b11, b12, b21, b22 = map(float, input("Matriks B [a11 a12 a21 a22] : ").split())
            m_a = mk.array([[a11, a12],
                            [a21, a22]])
            m_b = mk.array([[b11, b12],
                            [b21, b22]])
            hasil = m_a - m_b
            print(f"Hasil nya : \n{hasil}")
    else:
            print("Tidak Diketahui")
            
            

def no2():
     print("""
1. Ordo 2x2
2. Ordo 3x3 """)
     pilih = int(input("Pilih No Di Atas : "))
     if pilih == 1:
         a11, a12 = map(float, input("Masukan Nilai Matriks [a11 a12] : ").split()) 
         a21, a22 = map(float, input("Masukan Nilai Matriks [a21 a22] : ").split())
         m_a = mk.array([[a11, a12],
                         [a21, a22]])
         print("Hasil transpose matriks : \n", mk.transpose(m_a))
         
     elif pilih == 2:
         a11, a12, a13 = map(float, input("Masukkan Nilai Matriks [a11 a12 a13] : ").split())
         a21, a22, a23 = map(float, input("Masukkan Nilai Matriks [a21 a22 a23] : ").split())
         a31 ,a32, a33 = map(float, input("Masukkan Nilai Matriks [a31 a32 a33] : ").split())
         m_a = mk.array([[a11, a12, a13] ,
                         [a21, a22, a23] ,
                         [a31 ,a32, a33]])
         print("Hasil transpose matriks : \n", mk.transpose(m_a))
     else:
         ("Tidak Diketahui")


def no3():
    a11, a12, a21, a22 = map(float, input("Masukan Nilai Matriks [a11 a12 a21 a22] : ").split()) 
    m_a = mk.array([[a11, a12],
                    [a21, a22]])
    hasil = mk.linalg.inv(m_a)
    print(f"Hasilnya Adalah : \n{hasil}")
    
    
 
def no4():
    print("1. Ordo 2x2")
    print("2. Ordo 3x3")
    pilih = int(input("Pilih no di atas : "))
    if pilih == 1:
        a11, a12 = map(float, input("Masukan Nilai Matriks [a11 a12] : ").split()) 
        a21, a22 = map(float, input("Masukan Nilai Matriks [a21 a22] : ").split()) 
        
        m_a = mk.array([[a11, a12],
                        [a21, a22]])
         
        hasil = mk.linalg.det(m_a)
        hasil =  (a11 * a22) - (a12 * a21)
        
        print(f"Determinan nya adalah : \n{hasil}")
        
    elif pilih == 2:
        a11, a12, a13 = map(int, input("Masukkan Matriks a1 [a11 a12 a13] : ").split())
        a21, a22, a23 = map(int, input("Masukkan Matriks a2 [a21 a22 a23] : ").split())
        a31, a32, a33 = map(int, input("Masukkan Matriks a3 [a31 a32 a33] : ").split())
        
        m_a= mk.array([[a11, a12, a13], 
                       [a21, a22,a23], 
                       [a31,a32,a33]])
        
        hasil = mk.linalg.det(m_a) 
        hasil =  a11*(a22*a33 - a23*a32) - a12*(a21*a33 - a23*a31) + a13*(a21*a32 - a22*a31)
        
        print(f"Determinan nya adalah : \n{hasil}")
        
    else:
        print("Tidak Diketahui")
            

def no5():
   
   a11,a12,b1=map(float,input('Masukan [x1 x2] b1] :').split())
   a21,a22,b2=map(float,input('Masukan [x1 x2] b2] :').split())
   m_a = mk.array([[a11,a12],
                   [a21,a22]])
   m_b = mk.array([[b1],
                   [b2]])
   print(' x1 |  x2 |  b')
   print(a11,'|',a12,'|',b1)
   print(a21,'|',a22,'|',b2)
   x = mk.linalg.solve(m_a, m_b)
   print(x)

                
                                
if __name__ == "__main__":
    while True:
        pilih = menu()
        if pilih == 1:
            no1()
        elif pilih == 2:
            no2()
        elif pilih == 3:
            no3()
        elif pilih == 4:
            no4()
        elif pilih == 5:
            no5()
        elif pilih == 6:
            print("Terima Kasih telah menggunakan aplikasi ini \n")
            break
        else:
            print("Silakan pilih no yang ada di atas")
                        
                       
                            
                 