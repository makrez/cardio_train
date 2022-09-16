# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 11:35:11 2022

@author: i1B252778
"""

# Python ≥3.5 is required
import sys
assert sys.version_info >= (3, 5)

# Scikit-Learn ≥0.20 is required
import sklearn
assert sklearn.__version__ >= "0.20"

# Common imports
import numpy as np
import os

# To plot pretty figures
# %matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

# Where to save the figures
PROJECT_ROOT_DIR = "."
CHAPTER_ID = "end_to_end_project"
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
os.makedirs(IMAGES_PATH, exist_ok=True)

def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)

# Ignore useless warnings (see SciPy issue #5998)
import warnings
warnings.filterwarnings(action="ignore", message="^internal gelsd")



import pandas as pd

def load_cardio_data(cardio_path=os.getcwd()):
    csv_path = os.path.join(cardio_path, "cardio_train.csv")
    return pd.read_csv(csv_path)

csv_path = os.path.join(os.getcwd(), "cardio_train.xlsx")
card_vasc = pd.read_excel(csv_path)
card_vasc.head


card_vasc["age"].value_counts()


card_vasc["age"]=card_vasc["age"]/365
card_vasc["age"].hist()

%matplotlib inline
import matplotlib.pyplot as plt
card_vasc.hist(bins=50, figsize=(20,15))
save_fig("attribute_histogram_plots")
plt.show()

# to make this notebook's output identical at every run
np.random.seed(42)
print(np.random.seed(42))


from sklearn.model_selection import train_test_split

train_set, test_set = train_test_split(card_vasc, test_size=0.2, random_state=42)