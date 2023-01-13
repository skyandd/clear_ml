from clearml import Dataset
import os
import shutil
import pandas as pd
from tqdm import tqdm


# annotation = pd.read_csv('data/clearml_data/annotations/train.csv')
# metas = set(annotation['meta'].values)
# for meta in metas:
#     os.makedirs(f'data/clearml_data/{meta}', exist_ok=True)
#
# metas = annotation['meta']
# filenames = annotation['filename']
# print(len(filenames))
# for filename, meta in tqdm(zip(filenames, metas)):
#     src = os.path.join('data/clearml_data/images', filename)
#     dst = os.path.join(f'data/clearml_data/{meta}', filename)
#     print(src, dst)
#     shutil.copyfile(src, dst)


dataset = Dataset.create(
    dataset_name="test_dataset_grouped",
    dataset_project="dataset examples"
)
dataset.add_files(path='data/clearml_data')
dataset.upload()
dataset.finalize()
