from hanspell import spell_checker
import re
from tqdm.auto import tqdm


def remove_punc_and_emoticon(wrongSent):  # 문장부호 및 간단한 이모티콘 다듬기
    sent = wrongSent
    # 문장부호 반복 제거 및 문장부호 뒤 띄어쓰기 횟수 획일화
    punctuations = [r'\.',',',r'\?','!','~',';',':',r'\&']
    correct_punctuations = ['.',',','?','!','~',';',':',' N ']
    for idx in range(len(punctuations)):
        sent = re.sub(punctuations[idx]+'+',correct_punctuations[idx],sent)
        sent = re.sub(' '+punctuations[idx],correct_punctuations[idx],sent)
        sent = re.sub(punctuations[idx]+' *',correct_punctuations[idx]+" ",sent)

    # 반복되는 이모티콘 언어 제거 및 주변 띄어쓰기 획일화
    emoticons = ['ㅋㅋ','ㅎㅎ','ㅜㅜ','ㅠㅠ','ㅡㅡ']
    correct_emoticons = ['ㅋㅋ','ㅎㅎ','ㅜㅜ','ㅜㅜ','ㅡㅡ']
    for idx in range(len(emoticons)):
        sent = re.sub(emoticons[idx]+'+',correct_emoticons[idx],sent)
        sent = re.sub(correct_emoticons[idx]+' +',correct_emoticons[idx]+' ',sent)
        sent = re.sub(' *'+correct_emoticons[idx],' '+correct_emoticons[idx],sent)
    return sent

def check_naver(wrongSent):  # 네이버 맞춤법 교정
    spelled_sent = spell_checker.check(wrongSent)
    checked_sent = spelled_sent.checked
    return checked_sent

def final_grammar(dataframe):
    text_columns = ['sentence_1', 'sentence_2']

    for idx, item in tqdm(dataframe.iterrows(), desc='grammar_check', total=len(dataframe)):
        text1, text2 = (item[text_column] for text_column in text_columns)  # sentence_1, sentence_2 의미
        text1, text2 = remove_punc_and_emoticon(text1), remove_punc_and_emoticon(text2)  # 문장부호 및 이모티콘 다듬기
        text1, text2 = check_naver(text1), check_naver(text2)  # 네이버 검사기 교정
        dataframe.at[idx, 'sentence_1'] = text1
        dataframe.at[idx, 'sentence_2'] = text2
    return dataframe