# hanspell 설치: pip install py-hanspell
from hanspell import spell_checker
import re

# PyKoSpacing 설치: pip install git+https://github.com/haven-jeon/PyKoSpacing.git
from pykospacing import Spacing


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