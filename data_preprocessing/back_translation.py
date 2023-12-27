from deep_translator import GoogleTranslator
import pandas as pd
from tqdm.auto import tqdm

def extract_sample(df, per=0.15):
    sample = df.sample(frac=per, random_state=123)
    return sample

def back_translate(sentence):
    # 한국어에서 영어로 번역
    translated_en = GoogleTranslator(source='auto', target='en').translate(text=sentence)
    # 영어에서 다시 한국어로 번역
    translated_ko = GoogleTranslator(source='auto', target='ko').translate(text=translated_en)
    return translated_ko

def augment_df(sample_df):
    augmented_sentences_1 = []
    augmented_sentences_2 = []
    
    for sentence in tqdm(sample_df['sentence_1']):
        # back translation을 통한 sentence_1 증강
        augmented_sentence = back_translate(sentence)
        augmented_sentences_1.append(augmented_sentence)
        # time.sleep(random.uniform(1, 3))
        
    for sentence in tqdm(sample_df['sentence_2']):
        # back translation을 통한 sentence_2 증강
        augmented_sentence = back_translate(sentence)
        augmented_sentences_2.append(augmented_sentence)
        # time.sleep(random.uniform(1, 3))
  
        
    # 데이터프레임에 추가
    df_2 = pd.DataFrame({'id': sample_df["id"], 'source': sample_df["source"], "sentence_1" : augmented_sentences_1, "sentence_2" : augmented_sentences_2,
                        "label": sample_df["label"], "binary-label" : sample_df["binary-label"]})    
    return df_2