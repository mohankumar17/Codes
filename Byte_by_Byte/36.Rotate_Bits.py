def rotate(n,k):
    ans=n>>k
    return ans

a=rotate( 0xFFFF0000 , 8 )
print(a)
a=rotate( 0x13579BDF , 12 )
print(a)
a=rotate( 0b10110011100011110000111110000000 , 17 )
print(a)
print()
print(0x00FFFF00)
print(0xBDF13579)
print(0b00011111000000010110011100011110)
