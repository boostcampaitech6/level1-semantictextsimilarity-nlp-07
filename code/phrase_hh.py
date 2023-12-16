# hanspell 설치: pip install py-hanspell
from hanspell import spell_checker
import re

def remove_punc_and_emoticon(wrongSent):  # 문장부호 및 간단한 이모티콘 다듬기
    sent = wrongSent
    # 문장부호 반복 제거 및 문장부호 뒤 띄어쓰기 횟수 획일화
    punctuations = [r'\.',',',r'\?','!','~',';',':','…',r'\&']
    correct_punctuations = ['.',',','?','!','~',';',':','.',' N ']
    for idx in range(len(punctuations)):
        sent = re.sub(punctuations[idx]+'+',correct_punctuations[idx],sent)
        sent = re.sub(' '+punctuations[idx],correct_punctuations[idx],sent)
        sent = re.sub(punctuations[idx]+' +',correct_punctuations[idx],sent)

    # 반복되는 이모티콘 언어 제거 및 주변 띄어쓰기 획일화
    emotions = ['ㅋㅋ','ㅎㅎ','ㅜㅜ','ㅠㅠ','ㅡㅡ']
    correct_emoticons = ['ㅋㅋ','ㅎㅎ','ㅜㅜ','ㅜㅜ','ㅡㅡ']
    for idx in range(len(emotions)):
        sent = re.sub(emotions[idx]+'+',correct_emoticons[idx],sent)
        sent = re.sub(' '+emotions[idx],correct_emoticons[idx],sent)
        sent = re.sub(emotions[idx]+'\s+',correct_emoticons[idx]+' ',sent)
    return sent
    sent = wrongSent.replace('.', '. ').replace(',', ', ').replace('?', '? ').replace('!', '! ')  # 문장부호 분리
    sent = sent.replace('&',' N ')  # csv의 문장 내에 '&'가 있을 때 오류 발생 => ' N '으로 바꾸기
    return sent

def check_naver(wrongSent):  # 네이버 맞춤법 교정
    # 오류 시 다음 링크 또는 노션 페이지 참조: https://github.com/ssut/py-hanspell/issues/41
    spelled_sent = spell_checker.check(wrongSent)
    checked_sent = spelled_sent.checked
    return checked_sent

def check_ques(wrongSent):  # 글첵(https://wikidocs.net/186245) 맞춤법 교정기
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
        print("correct sentence_1:", check_naver(remove_punc_and_emoticon(sentence_1[idx])))
        print("correct sentence_2:", check_naver(remove_punc_and_emoticon(sentence_2[idx])))
        print("label:", label[idx])
        print("="*20)
