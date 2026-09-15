def REstPS(x1,y1, x2,y2):
    p= (x2-x1)*2+(y2-y1)*2
    s=(x2-x1)*(y2-y1)
    return p, s
print (REstPS(1,1,6,6))