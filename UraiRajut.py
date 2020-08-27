def urai(kata):                    # membuat fungsi bernama urai dengan 1 argumen yaitu 'kata'
    char = ''                      # membuat variabel berisi string kosong bernama char
    hasil = ''                     # membuat variabel berisi string kosong barnama hasil
    for i in kata:                 # membuat loop dengan i yang merupakan huruf pada 'kata, pada kasus 'Code', maka i adalah C, o, d dan e
        char += i                  # menambahkan i pada str kosong char, sehingga char = 'C', char ='Co', char ='Cod', char ='Code'
        hasil += char              # menambahkan str char pada hasil, sehingga hasil = 'C', hasil = 'CCo', hasil = 'CCoCod' , hasil = 'CCoCodCode'
    return hasil                   # output fungsi berupa str hasil

print(urai('Code'))
print(urai('Python'))
print(urai('Purwadhika'))


def rajut(kata):                             # membuat fungsi bernama urai dengan 1 argumen yaitu 'kata'
    unik = []                               # membuat list kosong untuk menampung huruf yang unique pada kata
    for i in kata:                          # membuat looping dengan i merupakan karakter pada 'kata'
        if i not in unik:                   # membuat kondisi jika i yang mewakili huruf pada kata belum terdapat dalam list unik, maka akan dimasukkan kedalam list unik
            unik.append(i)
    for i in unik:                          # membuat loop dengan i merupakan element pada list unik
        if i.lower() != i:                  # untuk melihat jika i merupakan huruf kapital atau bukan, karena kata diawali dengan huruf kapital
            i_kapital = unik.index(i)       # mencari index huruf kapital pada list unik
    pjg_kata = kata.count(unik[i_kapital])  # untuk mencari panjang dari kata yang akan dicari, karena jumlah huruf kapital = panjang kata sebenarnya
    return kata[len(kata) - pjg_kata:]      # [len(kata) - pjg_kata:] untuk mengambil element yang berada di panjang data - panjang kata yang dicari, sehingga fungsi akan mengembalikan kata yang diinginkan 

print(rajut('PPyPytPythPythoPython'))
print(rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
print(rajut('CCoCodCode'))