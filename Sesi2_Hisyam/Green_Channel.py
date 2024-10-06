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

image_green = np.zeros_like(image)
image_green[:,:,1] = green

img.imwrite("green_singkong.jpg", image_green)

print("Proses Berhasil")
