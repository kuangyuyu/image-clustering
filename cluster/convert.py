# -*- coding: utf-8 -*-
from PCV.tools.imtools import get_imlist #导入PCV模块
from PIL import Image
import os
import pickle

filelist = get_imlist('results/1/') #获取convert_images_format_test文件夹下的图片文件名(包括后缀名)
os.mkdir('last')
imlist = file('last/imlist.txt','w') #将获取的图片文件列表保存到imlist.txt中
pickle.dump(filelist,imlist) #序列化
imlist.close()

for infile in filelist:
    outfile = os.path.splitext(infile)[0] + ".tif" #分离文件名与扩展名
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print ("cannot convert", infile)