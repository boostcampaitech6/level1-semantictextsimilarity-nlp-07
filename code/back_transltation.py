from deep_translator import GoogleTranslator
import pandas as pd
import random
from tqdm import tqdm
import time
import yaml

# print(df["sentence_1"][0])
# translated = GoogleTranslator(source='auto', target='en').translate(text=df["sentence_1"][0])
# print(translated)
# translated = GoogleTranslator(source='auto', target='ko').translate(text=translated)
# print(translated)

def load_config(config_file):
    with open(config_file) as file:
        config = yaml.safe_load(file)
    return config

config = load_config("config.yaml")

df = pd.read_csv(config["paths"]["train_path"])

def back_translate(sentence):
    # 한국어에서 영어로 번역
    translated_en = GoogleTranslator(source='auto', target='en').translate(text=sentence)
    # 영어에서 다시 한국어로 번역
    translated_ko = GoogleTranslator(source='auto', target='ko').translate(text=translated_en)
    return translated_ko

def augment_df(df):
    augmented_sentences_1 = []
    augmented_sentences_2 = []
    
    for sentence in tqdm(df['sentence_1']):
        # back translation을 통한 sentence_1 증강
        augmented_sentence = back_translate(sentence)
        augmented_sentences_1.append(augmented_sentence)
        # time.sleep(random.uniform(1, 3))
        
    for sentence in tqdm(df['sentence_2']):
        # back translation을 통한 sentence_2 증강
        augmented_sentence = back_translate(sentence)
        augmented_sentences_2.append(augmented_sentence)
        # time.sleep(random.uniform(1, 3))
  
        
    # 데이터프레임에 추가
    df_2 = pd.DataFrame({'id': df["id"], 'source': df["source"], "sentence_1" : augmented_sentences_1, "sentence_2" : augmented_sentences_2,
                        "label": df["label"], "binary-label" : df["binary-label"]})    
    return df_2

# 데이터프레임 증강
df_2 = augment_df(df)

df = pd.concat([df, df_2], ignore_index = True)

df.to_csv(config["paths"]["train_aug_path"])