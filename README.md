
# 👋 Level 1 Project :: STS(Semantic Text Similarity)

## 📕 프로젝트 소개
> 본 대회의 목표는 STS 데이터 셋을 활용해 두 문장의 유사도를 측정하는 AI 모델을 구축하는 것으로, [두 개의 문장과 ID, 유사도 정보가 담긴 CSV]를 입력받아 [문장 쌍에 대한 ID, 유사도 점수가 담긴 CSV]를 출력하여 피어슨 상관계수를 통해 평가한다.
> 
> STS는 문장 간의 의미적 유사성을 판단하는 기술로, 다양한 응용 분야에서 중요한 역할을 한다. 예를 들어, “결제는 어디에서 하나요?”와 “계산하는 곳은 어디인가요?”와 같이 서로 다르게 표현되었지만 같은 의미를 담고 있는 문장들을 식별하는 데 사용된다. 이를 통해 질문-답변 시스템, 문장 요약, 챗봇의 질문 제안, 중복 문장 탐지 등 다양한 실제 상황에 적용할 수 있는 능력을 키울 수 있다.
프로젝트의 목표는 STS 데이터셋을 활용해 두 문장의 유사도를 측정하는 AI 모델을 구축하여, 0~5 사이의 유사도 점수 예측을 진행한다.

## 🐣 멤버 소개
|이지인|구다연|오수종|이민아|이헌효|장수정|
|:---:|:---:|:---:|:---:|:---:|:---:|
|![image](https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-07/assets/153268935/0ee055b6-c879-4e89-a3a8-9a20990e4300)|![image](https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-07/assets/153268935/31e9fe6c-c4e3-4aa0-bab9-76c6b58d7030)|![image](https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-07/assets/153268935/443f2311-9605-4780-aeb8-5e16765f2d79)|![image](https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-07/assets/153268935/f30af8f0-d693-42c7-a8d0-8b62ca3ef493)|![image](https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-07/assets/153268935/854d4d70-6dcc-44ca-997b-dd63877b4e2f)|![image](https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-07/assets/153268935/454b7a79-271a-4785-a005-de07b0e1dd2a)|
|[![badgeImage](https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Boribori12)|[![badgeImage](https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/9ooDa)|[![badgeImage](https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/suta777)|[![badgeImage](https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/minari1505)|[![badgeImage](https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/AlpacaParker4592)|[![badgeImage](https://img.shields.io/badge/github-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/jo9392)|

### 🐥 멤버별 역할
|성명|역할|
|:--:|:---|
|이지인|데이터 전처리 - EDA(Easy Data Augmentation), Back Translation|
|구다연|GitHub 연결, 데이터 전처리 aggregation, 적합한 모델 탐색 및 적용|
|오수종|데이터 분석, 모델 Ensemble, 적합한 모델 탐색 및 적용|
|이민아|Loss function 적합도 판단, 적합한 모델 탐색 및 적용|
|이헌효|데이터 전처리 - 맞춤법 교정 및 문장 다듬기, Optimizer별 모델 실행 및 비교 분석|
|장수정|프로젝트 기초 설정, Wandb 도입, 적합한 모델 탐색 및 적용|

## 💻 개발 환경
- **팀 구성 및 컴퓨팅 환경**
  - 6인 1팀, 인당 V100 서버를 VSCode와 SSH로 연결하여 사용
- **협업 환경**
  - ![notion](https://img.shields.io/badge/Notion-FFFFFF?style=flat-square&logo=Notion&logoColor=black) ![github](https://img.shields.io/badge/Github-181717?style=flat-square&logo=Github&logoColor=white) ![WandB](https://img.shields.io/badge/WeightsandBiases-FFBE00?style=flat-square&logo=WeightsandBiases&logoColor=white)
- **의사소통**
  - ![zoom](https://img.shields.io/badge/Zoom-0B5CFF?style=flat-square&logo=Zoom&logoColor=white) ![slack](https://img.shields.io/badge/Slack-4A154B?style=flat-square&logo=Slack&logoColor=white)
- **버전 정보**
  - transformers==4.35.2 pytorch-lightning==2.1.2 pandas==2.1.3
  
## 📈 사용 데이터
|데이터|사용 데이터셋|목적|구성|
|---|---|---|---|
|학습 데이터|훈련 데이터(train.csv) 및 검증 데이터(dev.csv)|학습 데이터셋에 기반한 모델(model.pt) 생성|색인(index)<br>문장 출처(source)<br>비교할 문장(sentence_1, sentence_2)<br>0.0~5.0까지의 연관도(label)<br>연관도를 binary하게 나타낸 값(binary_level)|
|평가 데이터|평가 데이터(test.csv)|학습 데이터 및 모델에 기반한 두 문장 간 연관도(label) 예측|색인(index)<br>문장 출처(source)<br>비교할 문장(sentence_1, sentence_2)|

## 🖇️ 파일 구조
```
.
|-- code
|   |-- __pycache__
|   |-- config.py
|   |-- config.yaml
|   |-- inference.py
|   |-- lightning_logs
|   |-- model
|   |-- requirements.txt
|   |-- train.py
|   `-- wandb
|-- data
|   |-- dev.csv
|   |-- output
|   |-- sample_submission.csv
|   |-- test.csv
|   `-- train.csv
`-- data_preprocessing
    |-- __pycache__
    |-- back_translation.py
    |-- down_sampling.py
    |-- eda.py
    |-- grammar_check.py
    |-- main.py
    `-- wordnet.pickle
```

## Appendix
<details><summary>
  
  ### 🔧 ```KeyError: 'result'``` 문제 해결하기(py-hanspell 패키지 관련 문제)
  
  </summary>
  
#### 원인

* 네이버 맞춤법 검사기가 업데이트되어 패키지 차원에서 ```passportKey```와 ```callback``` 변수를 제공해야 하지만, py-hanspell 패키지가 업데이트되지 않아 발생한 문제

#### 해결 방법

1. ```.../lib/python3.10/site-packages/hanspell/spell_checker.py``` 부분을 ```Ctrl``` + 클릭하여 패키지 파일 들어가기
2. 네이버 맞춤법 검사기에서 ```passportKey```, ```_callback``` 변수값을 copy하기
3. ```spell_checker.py``` 패키지 파일 수정하기

    1. 개발자 툴을 지원하는 브라우저(예: Chrome)로 [네이버 맞춤법 검사기 링크](https://search.naver.com/search.naver?where=nexearch&query=%EB%84%A4%EC%9D%B4%EB%B2%84+%EB%A7%9E%EC%B6%A4%EB%B2%95+%EA%B2%80%EC%82%AC%EA%B8%B0&ie=utf8&sm=tab_she&qdt=0)에 접속한 후 ```F12``` 버튼 눌러 개발자 툴 들어가기
    2. 개발자 툴에서 ```Network``` 채널 버튼 클릭하기
       ![Untitled](https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-07/assets/153268935/8cd40659-8d70-49eb-8897-a8b51aa64e6a)
    3. 맞춤법 검사기에 아무 문구를 넣고 ```Network``` 채널 창에 "spell" 검색하기
       ![Untitled](https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-07/assets/153268935/4245b1cc-e848-4c35-a29a-47c333ba8c92)
    4. ```SpellerProxy?…``` 변수를 클릭하여 ```Header``` 채널의 ```RequestURL``` 변수를 확인하기
    5. ```RequestURL``` 변수에서 ```passportKey``` 및 ```_callback``` 변수값을 복사하기
       ![Untitled](https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-07/assets/153268935/90608c61-ee20-4b65-96e2-53b83c112d80)
       여기서는 ```passportKey=db951c57dce59ab5bda4148db8a11fe7e1277e6a```, ```_callback=jQuery112407861628390335917_1702639286516```라 나옴.
   6. ```spell_checker.py```로 돌아가 아래와 같이 수정하기
      * 수정 전
        ```python
        ...
        
        data = json.loads(r.text)
        
        ...
        
        payload = {'q': text, 'color_blindness': '0' }
        
        ...
        ```
      * 수정 후
        ```python
        ...
        
        import re
        json_data = re.search(r'\((.*)\)', r.text).group(1)
        data = json.loads(json_data)
        
        ...
        
        payload = {'passportKey': 'curl값 copy하기',
					  '_callback': 'curl값 copy하기',
					  'q': text,
					  'color_blindness': '0' }
        
        ...
        ```

  
</details>
