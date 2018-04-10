 # -*- coding: utf-8 -*-
import os
from PIL import Image
from hcluster import *
from matplotlib.pyplot import *
from numpy import *
# import shutil

# create a list of images
path = 'nonrigid/'
imlist = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
# extract feature vector (8 bins per color channel)
features = zeros([len(imlist), 512])
for i, f in enumerate(imlist):
    im = array(Image.open(f))
    # multi-dimensional histogram
    h, edges = histogramdd(im.reshape(-1, 3), 8, normed=True, range=[(0, 255), (0, 255), (0, 255)])
    features[i] = h.flatten()
tree = hcluster(features)

# visualize clusters with some (arbitrary) threshold
clusters = tree.extract_clusters(0.23 * tree.distance)
print('total clusters:' + str(len(clusters)))
# plot images for clusters with more than 3 elements
os.mkdir('results')
c_num = 0
for c in clusters:
    elements = c.get_cluster_elements()
    nbr_elements = len(elements)
    print('elements in cluster:' + str(nbr_elements))
    print(elements)
    os.mkdir('results/' + str(c_num))
    for p in range(nbr_elements):
        im = array(Image.open(imlist[elements[p]]))
        imsave('results/' + str(c_num) + '/' + str(p) + '.jpg', im)
    c_num = c_num + 1