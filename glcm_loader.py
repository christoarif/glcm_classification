# to load tree array from .npz
import pickle
def load_glcm(data_dir):
    with open(data_dir, "rb") as f:
        tree = pickle.load(f)
    return tree



#%%
tree = load_glcm('/Users/keristo/Desktop/year3-sem1/ureca/glcm_classification/data/dec/glcm_18Dec2020_3rad_2step_128bins_1xDownScale_Pometia Pinnata_22.npz')