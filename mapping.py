import matplotlib.pyplot as plt
import numpy as np


triangle = np.array([1+2j, 2+2j, 3+3j])
rectangle = np.array([1+2j, 4+2j, 4+4j, 1+4j])

def plot_figure(vertices):
    plt.plot(np.append(vertices.real,vertices.real[0]),
             np.append(vertices.imag,vertices.imag[0]))
    plt.axis('equal')
    plt.xlabel('Real axis')
    plt.ylabel('Imaginary Axis')
    plt.grid(visible=True,linestyle='--')
    

def translate(points,translation):
    return points + translation

def magnify(points,magnification):
    return points * magnification

def rotate(points,angle):
    return points * np.exp(1j*angle)


tr_triangle = translate(triangle,1+2j)
magnify_rect = magnify(rectangle,3)
trmr_triangle = rotate(triangle,np.pi/2)

print("1. Translation of Triangle in Complex Plane")
print(f'Vertices of Triangle are - {triangle}')
plt.title('Z - Plane')
plot_figure(triangle)
plt.xlim(0,6)
plt.ylim(0,6)
plt.show()
plot_figure(tr_triangle)
print("Translation factor - 1+2j")
print(f'Verteces of Translated Triangle are - {tr_triangle}')
plt.title('W - Plane')
plt.xlim(0,6)
plt.ylim(0,6)
plt.show()

print("2. Magnification of Rectangle in Complex Plane")
print(f'Vertices of Rectangle are - {rectangle}')
plt.title('Z - Plane')
plot_figure(rectangle)
plt.xlim(0,15)
plt.ylim(0,15)
plt.show()
print("Magnification factor - 3")
print(f'Vertices of Magnified rectangle are - {magnify_rect}')
plt.title('W - Plane')
plot_figure(magnify_rect)
plt.xlim(0,15)
plt.ylim(0,15)
plt.show()

print("3. Rotation of Triangle in Complex Plane")
print(f'Vertices of Triangle are - {triangle}')
plt.title('Z - Plane')
plot_figure(triangle)
plt.show()
print("Rotation factor - π/2")
print(f'Vertices of Rotated Triangle are - {trmr_triangle}')
plt.title('W - Plane')
plot_figure(trmr_triangle)
plt.show()


