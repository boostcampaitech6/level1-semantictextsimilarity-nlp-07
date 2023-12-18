import os
import sys
sys.path.append('/data/ephemeral/home/level1-semantictextsimilarity-nlp-07/code')

import pandas as pd
from down_sampling import down_sample

import yaml
def load_config(config_file):
    with open(config_file) as file:
        config = yaml.safe_load(file)
    return config

config = load_config("/data/ephemeral/home/level1-semantictextsimilarity-nlp-07/code/config.yaml")

train_df = down_sample(config, data_name="train_path")
val_df = pd.read_csv(config["paths"]["dev_path"])
add_df = train_df.sample(frac=0.15, ignore_index=True)

train_df = train_df[~train_df.index.isin(add_df.index)].reset_index()
val_df = pd.concat([val_df, add_df], ignore_index=True)

# train_df.to_csv('/data/ephemeral/home/level1-semantictextsimilarity-nlp-07/data/processed_train.csv', index=False)
# val_df.to_csv('/data/ephemeral/home/level1-semantictextsimilarity-nlp-07/data/processed_dev.csv', index=False)