# hanspell 설치: pip install py-hanspell
from hanspell import spell_checker
import re

# PyKoSpacing 설치: pip install git+https://github.com/haven-jeon/PyKoSpacing.git
from pykospacing import Spacing

# soyNLP 설치: 
from soynlp.word import WordExtractor
from soynlp.normalizer import *
from soynlp.tokenizer import MaxScoreTokenizer

def remove_repeat(wrongSent, num_repeats=2):  # soynlp 기반 반복되는 어구 제거
    return emoticon_normalize(wrongSent, num_repeats=num_repeats)

def space_kospacing(wrongSent):  # PyKoSpacing 패키지 기반 띄어쓰기 처리
    spacing = Spacing()
    return spacing(wrongSent)

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
    # 오류 시 다음 링크 참조: https://github.com/ssut/py-hanspell/issues/41
    # 또는 다음 노션 페이지 참조: https://www.notion.so/Naver-11bd887e891d46f5bee9c6a7a79ca02d?pvs=4
    spelled_sent = spell_checker.check(wrongSent)
    checked_sent = spelled_sent.checked
    return checked_sent

# 내부 데이터 기반 토크나이징용 말뭉치 score 만들기
import pandas as pd
import math

train_data = pd.read_csv('../data/train.csv')
corpus = []
corpus += train_data['sentence_1'].to_list()
corpus += train_data['sentence_2'].to_list()

word_extractor = WordExtractor()
word_extractor.train(corpus)
words = word_extractor.extract()

def word_score(score):
    # 즐겨쓰는 방법 중 하나는 cohesion_forward에 right_branching_entropy를 곱하는 것
    # (1) 주어진 음절이 유기적으로 연결되어 함께 자주 나타나고,
    # (2) 그 단어의 우측에 다양한 조사, 어미, 혹은 다른 단어가 등장하여 단어의 우측의 branching entropy가 높다는 의미
    return (score.cohesion_forward * math.exp(score.right_branching_entropy))

scores_custom = {word: word_score(score) for word, score in words.items()}  # word_score 함수 처리한 점수
scores_cohesion_forward = {word: score.cohesion_forward for word, score in words.items()}  # cohesion_forward 점수
scores_right_branching_entropy = {word: score.right_branching_entropy for word, score in words.items()}  # right_branching_entropy 점수

def space_soynlp(wrongSent, scores=scores_custom):  # soynlp 기반 띄어쓰기 교정
    # https://github.com/lovit/soynlp/blob/master/tutorials/wordextractor_lecture.ipynb
    maxscore_tokenizer = MaxScoreTokenizer(scores=scores)
    return ' '.join(maxscore_tokenizer.tokenize(wrongSent))

def check_geulcheck(wrongSent):  # 글첵(https://wikidocs.net/186245) 맞춤법 교정기(진행 중)
    # https://github.com/ychoi-kr/ko-prfrdr 참고해서 함수 작성해야지~
    pass

if __name__ == '__main__':
    import pandas as pd
    import random

    # train.csv 불러오기
    train_data = pd.read_csv('../data/train.csv')

    # 인덱스 무작위 재배치
    sent_idx_list = [i for i in range(len(train_data))]
    random.shuffle(sent_idx_list)

    # sentence_1 및 sentence_2 리스트 추출
    sentence_1, sentence_2 = train_data['sentence_1'].values.tolist(), train_data['sentence_2'].values.tolist()
    label = train_data['label'].values.tolist()

    # 무작위 10개만 추리기
    for idx in sent_idx_list[:10]:
        print("origin sentence_1: ", sentence_1[idx])
        print("origin sentence_2: ", sentence_2[idx],'\n')
        print("correct sentence_1:", space_soynlp(remove_punc_and_emoticon(sentence_1[idx])))
        print("correct sentence_2:", space_soynlp(remove_punc_and_emoticon(sentence_2[idx])))
        #print("correct sentence_1:", check_naver(space_kospacing(remove_punc_and_emoticon(sentence_1[idx]))))
        #print("correct sentence_2:", check_naver(space_kospacing(remove_punc_and_emoticon(sentence_2[idx]))))
        print("label:", label[idx])
        print("="*20)
