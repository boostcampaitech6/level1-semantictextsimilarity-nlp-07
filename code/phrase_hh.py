# konlpy 설치: pip install konlpy (설치 오류 시 먼저 apt-get install default-jdk 설치하기)
from konlpy.tag import Okt

# PyKoSpacing 설치: pip install git+https://github.com/haven-jeon/PyKoSpacing.git
from pykospacing import Spacing

def sufflePhrase():  # 문장 내 어구 shuffle하기(미구현)
    None

def normalize_okt(wrongSent):  # 문장 정규화 처리
    okt = Okt()
    return okt.normalize(wrongSent)

def spacing_okt(wrongSent):  # 문장 띄어쓰기 처리(okt)
    okt = Okt()
    tagged = okt.pos(wrongSent)
    corrected = ""
    for i in tagged:
        if i[1] in ('Josa', 'PreEomi', 'Eomi', 'Suffix', 'Punctuation'):
            corrected += i[0]
        else:
            corrected += " "+i[0]
    if corrected[0] == " ":
        corrected = corrected[1:]
    return corrected
# 출처: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=roootwoo&logNo=221590316102

def spacing_pykos(wrongSent):  # 문장 띄어쓰기 처리(PyKoSpacing)
    spacing = Spacing()
    return spacing(wrongSent) 

def word_extractor(sentences):  # 데이터 내 문장 토크나이저(output: 단어별 빈도 score)
    word_extractor = WordExtractor(min_frequency=100,
                                    min_cohesion_forward=0.05, 
                                    min_right_branching_entropy=0.0)

    word_extractor.train(sentences) # list of str
    words = word_extractor.extract()
    cohesion_scores = {word:score.cohesion_forward for word, score in words.items()}
    return cohesion_scores

def spacing_soynlp(wrongSent, scores):  # 토큰 기반 문장 띄어쓰기 함수
    tokenizer = MaxScoreTokenizer(scores=scores)
    wrongSent = emoticon_normalize(wrongSent, num_repeats=2)  # 반복되는 단어 삭제(예: ㅋㅋㅋㅋㅋㅋㅋㅋ => ㅋㅋㅋ)
    #wrongSent = only_hangle_number(wrongSent)  # 한글 및 숫자만 나타내기(문장부호 삭제)
    return ' '.join(tokenizer.tokenize(wrongSent))



# soynlp 설치: pip install soynlp
from soynlp.word import WordExtractor  # 토큰화
from soynlp.normalizer import *  # 맞춤법 교정
from soynlp.tokenizer import MaxScoreTokenizer  # 띄어쓰기 교정
import re

def normalize_soynlp(wrongSent, num_repeats):  # 반복되는 단어 삭제(예: ㅋㅋㅋㅋㅋㅋㅋㅋ => ㅋㅋ)
    sent = emoticon_normalize(wrongSent, num_repeats=num_repeats)
    sent = re.sub('\.+', '.', sent)
    sent = re.sub('…+', '.', sent)
    sent = re.sub(',+', ',', sent)
    sent = re.sub('\?+', '?', sent)
    sent = re.sub('!+', '!', sent)
    return sent

def simple_spacing(wrongSent):  # 문장부호 뒤 띄어쓰기
    sent = wrongSent.replace('.', '. ').replace(',', ', ').replace('?', '? ').replace('!', '! ')  # 문장부호 분리
    sent = sent.replace('&',' N ')  # csv의 문장 내에 '&'가 있을 때 오류 존재 => ' N '으로 바꾸기
    return sent


from hanspell import spell_checker
def check_naver(wrongSent):  # 네이버 맞춤법 교정
    # 오류 시 다음 링크 참조: https://github.com/ssut/py-hanspell/issues/41
    spelled_sent = spell_checker.check(wrongSent)
    checked_sent = spelled_sent.checked
    return checked_sent

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
    num_repeats = 2
    for idx in sent_idx_list[:10]:
        print("origin sentence_1: ", sentence_1[idx])
        print("origin sentence_2: ", sentence_2[idx],'\n')
        print("correct sentence_1:", check_naver(simple_spacing(normalize_soynlp(sentence_1[idx], num_repeats))))
        print("correct sentence_2:", check_naver(simple_spacing(normalize_soynlp(sentence_2[idx], num_repeats))))
        print("label:", label[idx])
        print("="*20)
