## API Call Sequence 임베딩 및 임베딩 벡터를 이용한 악성코드 탐지 연구

### 문제 정의
실행 파일(.exe)의 IAT(Import Address Table)으로 실행 파일이 import 하는 .dll과 함수(function)들을 확인 할 수 있다. 사용한 함수들의 개수는 파일마다 다르기 때문에, 머신러닝의 피처(feature)로 사용하기 위해서는 전처리가 필요하다. 

- 본 프로젝트는 쿠쿠 샌드박스(Cuckoo Sandbox)의 파일 분석 결과로 얻을 수 있는 API Call Sequence를 활용하여 API 함수를 임베딩한다. 이로써 학습된 API 함수 임베딩 벡터로 함수들을 실수 벡터로 표현 할 수 있어 함수들을 피처화 가능하게 된다. 

- 임베딩 모델은 Negative Sampling Word2Vec(Skip-gram) 모델을 사용하였다. 

- 데이터 4만 개(악성 3만 개, 정상 1만 개)를 실험에 사용하였다.

1. 머신러닝

- 한 파일의 등장하는 함수들을 임베딩 된 실수 벡터로 변환 후 elementwise maximum 을 사용하여 모든 함수 벡터들을 단일 벡터로 임베딩한다.

- 임베딩 기법의 성능 비교를 위해 피처 해싱(Feature Hashing) 기법을 사용한 성능과 비교했다. 성능 평가는 5 폴드 교차 검증으로 검증을 진행했다. 사용한 피처는 다음과 같다.

- IAT 함수만 사용
- File Header + Optional Header + Data Directory + IAT 함수 사용

2. 딥러닝

- GatedCNN + Bi-LSTM 모델을 사용하여 API Call Sequence 학습

## A Study on Malware Detection Using API Call Sequence Embedding and Embedding Vector

### Problem Definition
We can check the .dlls and functions imported by the executable file with the IAT (Import Address Table) of the executable file (.exe). Since the number of functions used in executable file is different for each file, pre-processing is required to use them as features in machine learning.

- This project embeds functions using API Call Sequence that can be obtained as a result of file analysis of Cuckoo Sandbox. As a result, learned function embedding vector can be expressed as float vectors, making it possible to use as feature of machine learning .

- We use Negative Sampling Word2Vec (Skip-gram) model as an embedding model.

- 40,000 data (30,000 malware, 10,000 normal) were used in the experiment.

1. Machine Learning

- After converting the functions appeared in a file into an embedded float vector, the elementwise maximum is used to embed all vectors into a single vector.

- To compare the performance of the embedding technique, it was compared with the performance using the feature hashing technique. The performance evaluation was verified by 5-fold cross-validation. The features are used as follows.
- Use only IAT function
- Use File Header + Optional Header + Data Directory + IAT function

2. Deep Learning

- Learning API Call Sequence using GatedCNN + Bi-LSTM model


## Reference
- https://rguigoures.github.io/word2vec_pytorch/
- https://programmer.group/pytorch-implements-word2vec.html
- Zhaoqi Zhang, Panpan Qi, Wei Wang, "Dynamic Malware Analysis with Feature Engineering and Feature Learning", AAAI 2019 (https://arxiv.org/abs/1907.07352)
