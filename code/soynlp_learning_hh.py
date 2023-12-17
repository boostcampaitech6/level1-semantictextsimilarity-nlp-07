import urllib.request
from soynlp import DoublespaceLineCorpus
from soynlp.word import WordExtractor
import pickle
import os

filename = "2016-10-20.txt"
urllib.request.urlretrieve("https://raw.githubusercontent.com/lovit/soynlp/master/tutorials/2016-10-20.txt", filename=filename)

# 훈련 데이터를 다수의 문서로 분리
corpus = DoublespaceLineCorpus(filename)

word_extractor = WordExtractor()
word_extractor.train(corpus)
word_score_table = word_extractor.extract()

 
import math
def word_score(score):
    # 즐겨쓰는 방법 중 하나는 cohesion_forward에 right_branching_entropy를 곱하는 것
    # (1) 주어진 글자가 유기적으로 연결되어 함께 자주 나타나고,
    # (2) 그 단어의 우측에 다양한 조사, 어미, 혹은 다른 단어가 등장하여 단어의 우측의 branching entropy가 높다는 의미
    return (score.cohesion_forward * math.exp(score.right_branching_entropy))

word_score_table1 = {word: word_score(score) for word, score in word_score_table.items()}  # word_score 함수 처리한 점수
word_score_table2 = {word: score.cohesion_forward for word, score in word_score_table.items()}  # cohesion_forward 점수
word_score_table3 = {word: score.right_branching_entropy for word, score in word_score_table.items()}  # right_branching_entropy 점수

word_score_tables = [word_score_table1, word_score_table2, word_score_table3]

with open("soynlp_word_score_tables_hh.pickle","wb") as f:
    pickle.dump(word_score_tables, f) # 위에서 생성한 리스트를 word_score_tables_hh.pickle로 저장

# 부산물 txt 파일 제거
os.remove(filename)