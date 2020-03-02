import cv2
import os
import pydicom

inputdir = '/home/mihir/Desktop/Abhijeet/Dummy/'

path = '/home/mihir/Desktop/CBIS_DDSM/'

outdir = '/home/mihir/Desktop/CBIS_DDSM_NEW/'
#os.mkdir(outdir)

test_list = [f for f in  os.listdir(inputdir)]

# for f in test_list[:10]:   # remove "[:10]" to convert all images 
#     ds = pydicom.read_file(inputdir + f) # read dicom image
#     img = ds.pixel_array # get image array
#     cv2.imwrite(outdir + f.replace('.dcm','.png'),img) # write png image

total_images = 0  

for root, dirs, files in os.walk(path, topdown=False):
    for name in files:
        # print(os.path.join(root, name))
        x = root.split("_P_")[1] 
        x = root.split('/')
        y = x[-3] + '_' + x[-1] + '_'  + name 
        # print(y.replace(" ", '_'))
        y = y.replace(" ", "_")

        ds = pydicom.read_file(os.path.join(root, name)) # read dicom image
        img = ds.pixel_array # get image array
        cv2.imwrite(outdir + "{}.png".format(y),img) # write png image


        # total_images += len(y)
        # print(total_images)
#    for name in dirs:
    #   print(os.path.join(root, name))

# i = 0 
# j = 0 

# test_list1 = [f for f in  os.listdir(inputdir)]
# test_list2 = []
# test_list3 = []

# for f in os.listdir(inputdir):
#     # print("Directory's name: {}".format(f))
#     test_list1[i] = (inputdir + test_list[i] + '/')
#     # print(test_list1[i])

#     for f in os.listdir(test_list1[i]):        
#         test_list2 = (test_list1[i] +f + '/')        
#         print(test_list2)

#         for f in os.listdir(test_list2[i]):        
#             test_list3 = (test_list2[i] +f + '/')        
#             print(test_list3)

#     i += 1 

    


#   Calc-Test_P_00038_LEFT_CC/08-29-2017-DDSM-96009/1-full mammogram images-63992/000000.dcm 
#   /home/mihir/Desktop/Abhijeet/Dummy/Calc-Test_P_00038_LEFT_CC/


###########################################################################################################################################################################

# import os

# files = folders = 0

# for _, dirnames, filenames in os.walk(inputdir):
#   # ^ this idiom means "we won't be using this value"
#     files += len(filenames)
#     folders += len(dirnames)
#     print("File names:", filenames)
#     print('Directory names ' ,dirnames)

# print ("{:,} files, {:,} folders".format(files, folders))

###########################################################################################################################################################################

