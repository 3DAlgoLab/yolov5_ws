# %%
import os
import shutil
import random
from pathlib import Path

# preparing folder structure
full_data_path = 'data/obj/'

split_percentage = 90

images_path = 'data/images/'
if os.path.exists(images_path):
    shutil.rmtree(images_path)
os.mkdir(images_path)

labels_path = 'data/labels/'
if os.path.exists(labels_path):
    shutil.rmtree(labels_path)
os.mkdir(labels_path)


def mk_subdir(parent, sub):
    p: Path = Path(parent) / sub
    p.mkdir()

# %%
# Make sub folders


mk_subdir(labels_path, 'training')
mk_subdir(labels_path, 'validation')

mk_subdir(images_path, 'training')
mk_subdir(images_path, 'validation')

# %%
p = Path(full_data_path)
files = list(p.glob('*.jpg'))

random.shuffle(files)

training_split = int(split_percentage * len(files) / 100)

copied = map(lambda f: shutil.copy(f, Path(images_path) /
                                   'training'), files[:training_split])

list(copied)

# %%
copied = map(lambda f: shutil.copy(f, Path(images_path) /
                                   'validation'), files[training_split:])

list(copied)
#
# %%
# Label Data Handling
copied = map(lambda f: shutil.copy(f.parent / (f.stem + ".txt"), Path(labels_path) /
                                   'training'), files[:training_split])
list(copied)

copied = map(lambda f: shutil.copy(f.parent / (f.stem + ".txt"), Path(labels_path) /
                                   'validation'), files[training_split:])
list(copied)
# %%
print("Data Preparation Finished!")
