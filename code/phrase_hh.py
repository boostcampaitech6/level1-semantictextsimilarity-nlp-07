# hanspell 설치: pip install py-hanspell
from hanspell import spell_checker
import re

# PyKoSpacing 설치: pip install git+https://github.com/haven-jeon/PyKoSpacing.git
from pykospacing import Spacing

# soyNLP 설치: 
from soynlp.word import WordExtractor
from soynlp.tokenizer import RegexTokenizer, LTokenizer, MaxScoreTokenizer
import pickle

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
        sent = re.sub(punctuations[idx]+' +',correct_punctuations[idx],sent)

    # 반복되는 이모티콘 언어 제거 및 주변 띄어쓰기 획일화
    emoticons = ['ㅋㅋ','ㅎㅎ','ㅜㅜ','ㅠㅠ','ㅡㅡ']
    correct_emoticons = ['ㅋㅋ','ㅎㅎ','ㅜㅜ','ㅜㅜ','ㅡㅡ']
    for idx in range(len(emoticons)):
        sent = re.sub(emoticons[idx]+'+',correct_emoticons[idx],sent)
        sent = re.sub(correct_emoticons[idx]+' +',correct_emoticons[idx]+' ',sent)
        sent = re.sub(' *'+correct_emoticons[idx],' '+correct_emoticons[idx],sent)
    return sent
    sent = wrongSent.replace('.', '. ').replace(',', ', ').replace('?', '? ').replace('!', '! ')  # 문장부호 분리
    sent = sent.replace('&',' N ')  # csv의 문장 내에 '&'가 있을 때 오류 발생 => ' N '으로 바꾸기
    return sent

def check_naver(wrongSent):  # 네이버 맞춤법 교정
    # 오류 시 다음 링크 참조: https://github.com/ssut/py-hanspell/issues/41
    # 또는 다음 노션 페이지 참조: https://www.notion.so/Naver-11bd887e891d46f5bee9c6a7a79ca02d?pvs=4
    spelled_sent = spell_checker.check(wrongSent)
    checked_sent = spelled_sent.checked
    return checked_sent

def space_soynlp(wrongSent):  # soynlp 기반 띄어쓰기 교정
    # https://github.com/lovit/soynlp/blob/master/tutorials/wordextractor_lecture.ipynb
    import math
    def word_score(score):
        # 즐겨쓰는 방법 중 하나는 cohesion_forward에 right_branching_entropy를 곱하는 것
        # (1) 주어진 글자가 유기적으로 연결되어 함께 자주 나타나고,
        # (2) 그 단어의 우측에 다양한 조사, 어미, 혹은 다른 단어가 등장하여 단어의 우측의 branching entropy가 높다는 의미
        return (score.cohesion_forward * math.exp(score.right_branching_entropy))
    
    word_score_tables = None
    with open("soynlp_word_score_tables_hh.pickle","rb") as f:
        word_score_tables = pickle.load(f)
    
    word_score_table1 = word_score_tables[0]  # cohesion_forward 점수와 right_branching_entropy 점수를 조합한 함수
    word_score_table2 = word_score_tables[1]  # cohesion_forward 점수
    word_score_table3 = word_score_tables[2]  # right_branching_entropy 점수

    maxscore_tokenizer = MaxScoreTokenizer(scores=word_score_table1)
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
