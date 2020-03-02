import os
import shutil
source_dir = os.listdir('/home/mihir/Desktop/Abhijeet/Datasets/e_optha_EX1/e_ophtha_EX/e_optha_EX/EX/')
dest_dir = '/home/mihir/Desktop/Abhijeet/Datasets/optha_EX/'
for f in source_dir:
    print (f)
    file_path = '/home/mihir/Desktop/Abhijeet/Datasets/e_optha_EX1/e_ophtha_EX/e_optha_EX/EX/' + f
    print('-'*70)
    print(file_path)
    print('-'*70)
    images = os.listdir(file_path)
    for image in images:
        print (images)
        os.rename(file_path, dest_dir)
        shutil.move(image,dest_dir)
