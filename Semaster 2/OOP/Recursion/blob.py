def blob(img, r, c):
    if ((r < 0) or (c < 0) or (r >= NR) or (c >= NC)):
        return 0
    if (img[r][c] == 1):
        # print(f"{chr(c+65)}{r+1}")
        img[r][c] = 0
        return 1 + blob(img, r-1, c-1) + blob(img, r-1, c) + blob(img, r-1, c+1) + blob(img, r, c+1) + blob(img, r+1, c+1) + blob(img, r+1, c) + blob(img, r+1, c-1) + blob(img, r, c-1)
    else:
        return 0
        
file = open("Recursion/blob_img.txt")
row = file.readline()
print(row)
M = [] # image array 
# while (row exist)
while (row != ""):
    row = row[:-1] # remove '\n' character from row at last
    row = row.split("\t")
    row = list(map(int, row))
    M.append(row)
    row = file.readline()
file.close()

NR = len(M)
NC = len(M[0])
length_of_rivers = 0
for r in range(NR):
    for c in range(NC):
        if M[r][c] == 1:
            length_of_rivers += blob(M, r, c)        
            
print(length_of_rivers)