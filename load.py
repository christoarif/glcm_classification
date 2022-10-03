# to load tree array from .npz

import pickle

def load_glcm(data_dir):
    with open(data_dir, "rb") as f:
        tree = pickle.load(f)
    return tree

#%%
tree = load_glcm('data/glcm_18Dec2020_3rad_2step_128bins_1xDownScale_Clausena Excavata_11.npz')

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