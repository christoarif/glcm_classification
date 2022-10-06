'''
from a ndarray structure e.g. (119, 74, 8,7) or (20,20, 8,7), generate feature of the tree.
for e.g. a feature of the tree can be any combination of MEAN, VAR, SKEW, KURTOSIS of
ANY CHANNELS of ANY FEATURES
Example:
np.mean[:,:, i, j] where i=7, j=8 means MEAN_GREEN_CORRELATION of the tree
'''

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
import numpy as np
from glcm_loader import load_glcm

def generate_feature_from_tree(tree):
    tree_features = []
    for i in range(tree.shape[-2]):
        for j in range(tree.shape[-1]):
            tree_features.append(np.mean(tree[:,:, i, j].flatten())) # is flatten the right way to do it?
    #tree_features_series = pd.Series(tree_features) # make it so easier to put in table later
    return tree_features

# #%%
# tree = load_glcm('data/glcm_18Dec2020_3rad_2step_128bins_1xDownScale_Clausena Excavata_11.npz')
# feature = generate_feature_from_tree(tree)
#
# # feature[0] would be MEAN_WBRED_NONE
# #feature[1] would be MEAN_WBRED_HOMOGEINITY
# #feature[56] would be MEAN_GREEN_CORRELATION