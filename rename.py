import os
from tqdm import tqdm

def rename_images(input_folder):

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    for i, image_file in enumerate(tqdm(image_files, desc="Renaming images", unit="image", ncols=80)):
  
        new_name = f"{i+1}.png"
        
        old_path = os.path.join(input_folder, image_file)
        new_path = os.path.join(input_folder, new_name)

     
        os.rename(old_path, new_path)

if __name__ == "__main__":
  
    input_folder = "/home/asad/Desktop/Asad_CV/pix2pix-pytorch/dataset/ball/test/a"

    rename_images(input_folder)
