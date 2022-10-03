'''
since we have very limited instances of tree,
for each tree we sample X number of bounding box.

the intuition is that every bounding box would have similar but slightly different features,
so we can augment the number of samples for each tree
'''
import random

#%%
from sklearn.feature_extraction import image

# tree ndarray structure
# (119, 74, 8,7)
# (Height, Width, Channel, Features)
#channels:
'''
Wideband Red = 0
Wideband Green = 1
Wideband Blue = 2
RedEdge = 3
Blue = 4
NIR = 5
Red = 6
Green = 7
'''

#features:
'''
NONE = 0
HOMOGENEITY = 1
CONTRAST = 2
ASM = 3
MEAN_I = 4
MEAN_J = 5
VAR_I = 6
VAR_J = 7
CORRELATION = 8
'''
from glcm_loader import load_glcm

def augment_trees(tree, bb_size, sample_number):
    trees = []

    max_x = (tree.shape[0] - bb_size)
    max_y = (tree.shape[1] - bb_size)
    x = random.randint(0, max_x)
    y = random.randint(0, max_y)
    for i in range(sample_number):
        sample = (tree[x:x+bb_size,y:y+bb_size,:,:]) # is there a better way to generate the random samples?
        trees.append(sample)

    return samples

#%%
tree = load_glcm('data/glcm_18Dec2020_3rad_2step_128bins_1xDownScale_Clausena Excavata_11.npz')
#%%
samples = augment_trees(tree, 20, 20) # this maintain a list of augmented tree crowns. from 1 labeled bounding box of a tree,
# we now have 20 'instances' of the said tree