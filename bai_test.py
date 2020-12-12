chuoi_ban_dau = "acccaaaaaaaaaaaaaaaaaxxxxxxxxxxe"
ky_tu_ban_dau = chuoi_ban_dau[0]
chuoi_bi_cat = []
chuoi_moi = chuoi_ban_dau
while len(chuoi_moi):
    dem = 0
    cac_ky_tu = list()
    for j in range(len(chuoi_moi)):
        if chuoi_moi[j] == ky_tu_ban_dau:
            cac_ky_tu.append(chuoi_moi[j])
            dem += 1
        else:
            ky_tu_ban_dau = chuoi_moi[j]
            break
    if dem > 0:
        chuoi_moi = chuoi_moi[dem:]
        chuoi_bi_cat.append(''.join(cac_ky_tu))
ky_tu_bi_trung = ''
x = max(chuoi_bi_cat, key=len)
print("Chuoi co do dai lon nhat la: ", x)
for val in chuoi_bi_cat:
    if len(val) == 1:
        continue
    if not ky_tu_bi_trung:
        ky_tu_bi_trung = list(set(val))[0]
        print("Ky tu bi trung la: ", ky_tu_bi_trung)
    print('Vi tri cua chuoi "{}" la: {}'.format(val, chuoi_ban_dau.index(val)))