import cmath as cm
import matplotlib.pyplot as plt

z = complex(3,1)
print('z = ',z)
print('real z = ',z.real)
print('imaginary z = ',z.imag)
print('argument - ',cm.phase(z))
print('polar - ',cm.polar(z))
print('rectangular - ',cm.rect(abs(z),cm.phase(z)))
print('modulus - ',abs(z))
z2 = complex(4,1)
print('z2 = ',z2)
print('z+z2 = ',z+z2)
print('z-z2 = ',z-z2)
print('z*z2 = ',z*z2)
print('z/z2 = ',z/z2)
print('conjugate z = ',complex(z.real,-z.imag))
print('z*conjugate(z) = ',z*complex(z.real,-z.imag))

x = complex(3,1)
a = [0,x.real]
b = [0,x.imag]
polar = cm.polar(x)

plt.plot(a,b, marker='o')
plt.axhline()
plt.axvline()
plt.show()
plt.polar(polar[1],polar[0],marker='o')
print('polar - ',polar)
plt.show()

