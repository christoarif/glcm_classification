#%%
import os

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sn

from glcm_loader import load_glcm
from augment_tree import sample_a_tree
from generate_feature import generate_feature_from_tree

# CONFIGURATIONS
TRAIN_FOLDER = 'data/dec/'
TEST_FOLDER = 'data/may/'
SAMPLE_COUNT = 20
SAMPLE_CROP_SIZE = 20 # 20 X 20 samples
#%%
def dataloader(data_folder, sample_count, sample_crop_size):
    tree_files = [i for i in os.listdir(data_folder) if i[0] != "."]  # Exclude all with . in the start
    glcm_features = pd.DataFrame()
    for treefile in tree_files:
        print(data_folder + treefile)
        tree = load_glcm(data_folder + treefile)
        x = treefile.split('_')
        name = x[-2] # get name of trees from file name
        for i in range(sample_count):
            tree_sample = sample_a_tree(tree, sample_crop_size)
            sample_features = generate_feature_from_tree(tree_sample)
            sample_features.insert(0, name)
            sample_features_series = pd.Series(sample_features)
            glcm_features = glcm_features.append(sample_features_series, ignore_index=True)
    return glcm_features
def make_rf_model(X_train, y_train):
    # scaler = StandardScaler()
    # X = scaler.fit_transform(X)
    rfclassifier = RandomForestClassifier(n_estimators=100, criterion='gini', random_state=21)
    rfclassifier.fit(X_train, y_train)
    return rfclassifier

#%%
train_dataset = dataloader(TRAIN_FOLDER,SAMPLE_COUNT,SAMPLE_CROP_SIZE)
test_dataset = dataloader(TEST_FOLDER, SAMPLE_COUNT, SAMPLE_CROP_SIZE)
factor = pd.factorize(train_dataset[0])
factor_names = factor[0]
definitions = factor[1]

#%%
X_train = train_dataset.iloc[:, 1:].values
y_train = train_dataset.iloc[:, 0].values
model = make_rf_model(X_train, y_train)
X_test = test_dataset.iloc[:, 1:].values
y_test = test_dataset.iloc[:, 0].values
y_pred = model.predict(X_test)

#%%
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
# , y_pred, rownames=['Actual Species'], colnames=['Predicted Species'])
contigency_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual Species'], colnames=['Predicted Species'])
print(contigency_matrix)
fig, ax = plt.subplots(figsize=(10, 10))
sn.heatmap(ax=ax, data=contigency_matrix, annot=True, cmap="Reds")
plt.tight_layout()
plt.title('trained on Dec20, tested on May21')
plt.show()
accuracy_score(y_test, y_pred)
print(classification_report(y_test, y_pred))




