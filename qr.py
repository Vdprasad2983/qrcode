import qrcode
import csv
with open("movie.csv","r") as f:
    x1=csv.reader(f)
    l1=list(x1)
    for i in range(1,len(l1)):
        d=l1[i][1]+"\n"+l1[i][2]+"\n"+l1[i][3]+"\n"+l1[i][4]+"\n"+l1[i][5]+"\n"+l1[i][6]
        img = qrcode.make(d)
        img.save(f"C:\\Users\\ABC\\Desktop\\prasad files\\vs code\\qrcodes\\{l1[i][0]}.png")
        