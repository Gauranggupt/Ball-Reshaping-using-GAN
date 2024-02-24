import cv2
import os
import shutil


image_folder = "/home/asad/Desktop/Asad_CV/02_data_prep/data_yolo/images/train"
blur_folder = "/home/asad/Desktop/Asad_CV/02_data_prep/data_yolo/gan_images/sharp"
sharp_folder = "/home/asad/Desktop/Asad_CV/02_data_prep/data_yolo/gan_images/sharp"
delete_folder = "/home/asad/Desktop/Asad_CV/02_data_prep/data_yolo/gan_images/del"

os.makedirs(blur_folder, exist_ok=True)
os.makedirs(sharp_folder, exist_ok=True)
os.makedirs(delete_folder, exist_ok=True)


image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

for image_file in image_files:
    image_path = os.path.join(image_folder, image_file)

  
    img = cv2.imread(image_path)

   
    height, width, _ = img.shape
    aspect_ratio = width / height
    new_width = 1280  # 720p width
    new_height = int(new_width / aspect_ratio)
    img_resized = cv2.resize(img, (new_width, new_height))

    cv2.imshow('Resized Image', img_resized)
    key = cv2.waitKey(0)

    if key == ord('b'):
        shutil.move(image_path, os.path.join(blur_folder, image_file))
    elif key == ord('s'):
        shutil.move(image_path, os.path.join(sharp_folder, image_file))
    elif key == ord('d'):
        shutil.move(image_path, os.path.join(delete_folder, image_file))

    # Close the image window
    cv2.destroyAllWindows()
