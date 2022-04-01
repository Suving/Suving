isk = input("Sisetage isikukood: ")
if isk[0] == '5':
    tgl_lahir_nik = isk[1:7]
    
    aast = tgl_lahir_nik[:2]
    kuu_pav = tgl_lahir_nik[2:]
    
    
    hari_asli = str(aast)
    tgl_lahir_asli = hari_asli + kuu_pav
    
    
    from datetime import datetime
    
    sund = datetime.strptime(tgl_lahir_asli, "%y%m%d")
    print(sund.year)
    
    import datetime
    
    x = datetime.datetime.now()
    print(x.year)
    
    van = x.year - sund.year
    print(van)

else:
    tgl_lahir_nik = isk[1:7]
    
    aast = tgl_lahir_nik[:2]
    kuu_pav = tgl_lahir_nik[2:]
    
    
    hari_asli = str(int(aast))
    tgl_lahir_asli = hari_asli + kuu_pav
    
    
    from datetime import datetime
    
    sund = datetime.strptime(tgl_lahir_asli, "%y%m%d")
    print(sund.year)
    
    
    import datetime
    
    x = datetime.datetime.now()
    print(x.year)
    
    van = x.year - sund.year
    print(van)