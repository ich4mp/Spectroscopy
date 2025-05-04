import cv2 as cv

img = cv.imread('cfl.png')


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

height, width = gray.shape

px = [[] for _ in range(width)]
#print(len(px))

for col in range(width):
    for row in range(height):
        #print(gray[row][col])
        px[col].append(gray[row][col])
print(len(px))

spe = []
for i in range(width):
    csum = sum(px[i])
    clen = len(px[i])
    avg = csum/clen
    spe.append(avg)

intens = []
for i in range(width):
    inten = spe[i] / max(spe)
    intens.append(inten)
    

print(len(spe))

m = 400/width

w_l = []
for i in range(width):
    if intens[i - 1] < intens[i] > intens[i + 1]:
        print('Index : ', i, 'Value : ', intens[i])

### Define a function for wavelength ### 
    w_l.append((i)*m + 400)

        
import matplotlib.pyplot as plt
plt.plot(w_l, intens)
######l = [405, 436, 546, 691]
######i = [146, 194, 250, 311]
######plt.plot(l, i)
plt.grid(True)
plt.show()
    
        
        
