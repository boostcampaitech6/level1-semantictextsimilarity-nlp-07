
# 👋 Level 1 Project :: STS(Semantic Text Similarity)

## 📕 프로젝트 소개
> 본 대회의 목표는 STS 데이터 셋을 활용해 두 문장의 유사도를 측정하는 AI 모델을 구축하는 것으로, [두 개의 문장과 ID, 유사도 정보가 담긴 CSV]를 입력받아 [문장 쌍에 대한 ID, 유사도 점수가 담긴 CSV]를 출력하여 피어슨 상관계수를 통해 평가한다.
> 
> STS는 문장 간의 의미적 유사성을 판단하는 기술로, 다양한 응용 분야에서 중요한 역할을 한다. 예를 들어, “결제는 어디에서 하나요?”와 “계산하는 곳은 어디인가요?”와 같이 서로 다르게 표현되었지만 같은 의미를 담고 있는 문장들을 식별하는 데 사용된다. 이를 통해 질문-답변 시스템, 문장 요약, 챗봇의 질문 제안, 중복 문장 탐지 등 다양한 실제 상황에 적용할 수 있는 능력을 키울 수 있다.
프로젝트의 목표는 STS 데이터셋을 활용해 두 문장의 유사도를 측정하는 AI 모델을 구축하여, 0~5 사이의 유사도 점수 예측을 진행한다.

## 🐣 멤버 소개(사진 및 깃헙 링크는 추후 기재)
|이지인|구다연|오수종|이민아|이헌효|장수정|
|:---:|:---:|:---:|:---:|:---:|:---:|
|![image](https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-07/assets/153268935/0ee055b6-c879-4e89-a3a8-9a20990e4300)|![image](https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-07/assets/153268935/31e9fe6c-c4e3-4aa0-bab9-76c6b58d7030)|![image](https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-07/assets/153268935/443f2311-9605-4780-aeb8-5e16765f2d79)|![image](https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-07/assets/153268935/f30af8f0-d693-42c7-a8d0-8b62ca3ef493)|![image](https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-07/assets/153268935/854d4d70-6dcc-44ca-997b-dd63877b4e2f)|![image](https://github.com/boostcampaitech6/level1-semantictextsimilarity-nlp-07/assets/153268935/454b7a79-271a-4785-a005-de07b0e1dd2a)|
|깃헙|깃헙|깃헙|깃헙|깃헙|깃헙|

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
  - Notion, GitHub, WandB
- **의사소통**
  - Zoom, Slack
- **버전 정보**
  - transformers==4.35.2 pytorch-lightning==2.1.2 pandas==2.1.3
  
## 📈 사용 데이터
|데이터|사용 데이터셋|목적|구성|
|:---|:---|:---|:---|
|학습 데이터|훈련 데이터(train.csv) 및 검증 데이터(dev.csv)|학습 데이터셋에 기반한<br>모델(model.pt) 생성|색인(index)<br>문장 출처(source)<br>비교할 문장(sentence_1, sentence_2)<br>0.0~5.0까지의 연관도(label)<br>연관도를 binary하게 나타낸 값(binary_level)|
|평가 데이터|평가 데이터(test.csv)|학습 데이터 및 모델에 기반한<br>두 문장 간 연관도(label) 예측|색인(index)<br>문장 출처(source)<br>비교할 문장(sentence_1, sentence_2)|

## 🖇️ 파일 구조
  - 
