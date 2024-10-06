import numpy as np
import imageio.v3 as img

image_path = "C:/Users/Aspire_Black/Documents/PCG_Smes5_Hisyam/Sesi2_Hisyam/Foto/DNPepaya.jfif"
image = img.imread(image_path)

if len (image.shape) < 3 or image.shape[2] != 3:
    print("Format Gambar Harus RGB")
    exit()

red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

image_blue = np.zeros_like(image)
image_blue[:,:,2] = blue

img.imwrite("Blue_DNpepaya.jfif", image_blue)

print("Proses Berhasil")
