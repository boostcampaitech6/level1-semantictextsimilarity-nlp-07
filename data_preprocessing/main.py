import os
import sys
sys.path.append('/data/ephemeral/home/level1-semantictextsimilarity-nlp-07/code')

import pandas as pd

from down_sampling import down_sample
from eda import eda_aug
from grammar_check import final_grammar
from back_translation import extract_sample, augment_df

# config
import yaml
def load_config(config_file):
    with open(config_file) as file:
        config = yaml.safe_load(file)
    return config

config = load_config("/data/ephemeral/home/level1-semantictextsimilarity-nlp-07/code/config.yaml")

# Down sampling 및 데이터 불러오기
train_df = down_sample(config, data_name="train_process_path")
val_df = pd.read_csv(config["paths"]["dev_process_path"])
test_df = pd.read_csv(config["paths"]["predict_path"])

# train-validation split
add_df = train_df.sample(frac=0.15, random_state=123, ignore_index=True)  # 합쳤을 때 대략 20%가 될 수 있게 15%를 가져옴 (original val data는 6% 정도)

train_df = train_df[~train_df.index.isin(add_df.index)].reset_index()   # val에 들어 갈 데이터 train에서 빼주기
val_df = pd.concat([val_df, add_df], ignore_index=True)     # val과 train에서 뗀 데이터 붙이기

# EDA
train_df = eda_aug(train_df)
# val_df = eda_aug(val_df)

# 번역
sample_train = extract_sample(train_df, 0.15)
# sample_train = extract_sample(train_df, 0.3)
bt_df = augment_df(sample_train)
train_df = pd.concat(train_df, bt_df)

# 맞춤법
final_train_df = final_grammar(train_df)
final_val_df = final_grammar(val_df)
final_test_df = final_grammar(test_df)

# 데이터 저장
final_train_df.to_csv('/data/ephemeral/home/level1-semantictextsimilarity-nlp-07/data/final_train.csv', index=False)
final_val_df.to_csv('/data/ephemeral/home/level1-semantictextsimilarity-nlp-07/data/final_dev.csv', index=False)
final_test_df.to_csv('/data/ephemeral/home/level1-semantictextsimilarity-nlp-07/data/final_test.csv', index=False)