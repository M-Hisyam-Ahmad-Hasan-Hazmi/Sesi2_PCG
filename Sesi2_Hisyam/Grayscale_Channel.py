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

gray = 0.299 * red + 0.587 * green + 0.144 * blue

image_gray = np.zeros_like(image)
image_gray[:,:,0] = gray
image_gray[:,:,1] = gray
image_gray[:,:,2] = gray

img.imwrite("Gray_DNpepaya.jfif", image_gray)

print("Proses Berhasil")
