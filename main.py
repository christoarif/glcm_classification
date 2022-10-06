#%%
import os
import pandas as pd

from glcm_loader import load_glcm
from augment_tree import sample_a_tree
from generate_feature import generate_feature_from_tree

# CONFIGURATIONS
DATA_FOLDER = 'data/'
SAMPLE_COUNT = 20
SAMPLE_CROP_SIZE = 20 # 20 X 20 samples
#%%
def dataloader(data_folder, sample_count, sample_crop_size):
    for treefile in (os.listdir(DATA_FOLDER)):
        glcm_features = pd.DataFrame()
        tree = load_glcm(DATA_FOLDER + treefile)
        x = treefile.split('_')
        name = x[6]
        for i in range(SAMPLE_COUNT):
            tree_sample = sample_a_tree(tree, SAMPLE_CROP_SIZE)
            sample_features = generate_feature_from_tree(tree_sample)
            sample_features.insert(0, name)
            sample_features_series = pd.Series(sample_features)
            glcm_features = glcm_features.append(sample_features_series, ignore_index=True)
    return glcm_features

#%%
dataset = dataloader(DATA_FOLDER,SAMPLE_COUNT,SAMPLE_CROP_SIZE)






