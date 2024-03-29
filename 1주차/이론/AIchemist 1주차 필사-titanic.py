# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sT_SY0PmJKzkkrbllgz_UaVYmEndgmW-
"""

#read_csv를 통해 다양한 포맷으로 된 파일을 DataFrame으로 로딩할 수 있는 API 제공
titanic_df=pd.read_csv(r'C:\Users\chkwon\Data_Hadling\titanic_train.csv')
titanic_df.head(3)

#코드의 맨 마지막에 titanic_df를 호출하면 DataFrame의 모든 데이터를 출력
titanic_df=pd.read_csv('titanic_train.csv')
print('titanic 변수 type:', type(titanic_df))
titanic_df

#DataFrame의 행과 열 크기를 알아보기 : shape를 통해 DataFrame의 행과 열을 튜플 형태로 반환
print('DataFrame 크기:', titanic_df.shape)

#DataFrame은 데이터, 칼럼의 타입, Null 데이터 개수, 데이터 분포도 등의 메타 데이터 등 조회 가능-info()와 describe()
titanic_df.info()

#숫자형 칼럼에 대한 개략적인 데이터 분포도 확인
titanic_df.describe()

#데이터의 분포도 확인
value_counts=titanic_df['Pclass'].value_counts()
print(value_counts)

#value_counts()는 많은 건수 순서로 정렬, DataFrame의 []연산자 내부에 칼럼명 입력 시 해당 칼럼에 해당하는 Series 객체 반환
titanic_pclass=titanic_df['Pclass']
print(type(titanic_pclass))

#Series와 Index는 단 하나의 칼럼으로 구성된 데이터 세트
titanic_pclass.head()

#value_counts()가 반환하는 데이터 타입 역시 Series 객체
value_counts=titanic_df['Pclass'].value_counts()
print(type(value_counts))
print(value_counts)

print('titanic_df 데이터 건수:',  titanic_df.shape[0])
print('기본 설정인 dropna=True로 value_counts()')

#value_counts()는 디폴트로 dropna=True이므로 value_counts(dropna=True)와 동일
print(titanic_df['Embarked'].value_counts())
print(titanic_df['Embarked'].value_counts(dropna=False))

import numpy as np

col_name1=['col1']
list1=[1,2,3]
array1=np.array(list1)
print('array1 shape:', array1.shape)

#리스트를 이용해 DataFrame 생성
df_list1=pd.DataFrame(list1, colums=col_name1)
print('1차원 리스트로 만든 DataFrame:\n', df_list1)

#넘파이 ndarray를 이용해 DataFrame 생성
df_array1=pd.DataFrame(array1, colums=col_name1)
print('1차원 ndarray로 만든 DataFrame:\n', df_array1)

#3개의 칼럼명이 필요함 왜냐하면 2행 3열 형태의 리스트와 ndarray를 기반으로 DataFrame을 생성
col_name2=['col1','col2','col3']

#2행*3열 형태의 리스트와 ndarray 생성한 뒤 이를 DataFrame으로 변환
list2=[[1,2,3,],
      [11,12,13]]
array2=np.array(list2)
print('array2 shape:', array2.shape)
df_list2=pd.DataFrame(list2, columns=col_name2)
print('2차원 리스트로 만든 Dataframe:\n', df_list2)
df_array2=pd.DataFrame(array2, colums=col_name2)
print('2차원 ndarray로 만든 DataFrame:\n', df_array2)

#Key는 문자열 칼럼명으로 매핑, 각 Value는 리스트형(ndarray/각 칼럼 데이터)로 매핑
dict={'col1':[1,11], 'col2':[2,22], 'col3':[3,33]}
df_dict=pd.DataFrame(dict)
print('딕셔너리로 만든 DataFrame:\n', df_dict)

#DataFrame을 ndarray로 변환
array3=df_dict.values
print('df_dict.values 타입:', type(array3), 'df_dict.values shape:', array3.shape)
print(array3)

#DataFrame을 리스트로 변환 value를!
list3=df_dict.values.tolist()
print('df_dict.values.tolist() 타입:', type(list3))
print(list3)

#DataFrame을 딕셔너리로 변환 바로!
dict3=df_dict.to_dict('list')
print('\n df_dict.to_dict() 타입:', type(dict3))
print(dict3)

#기존 칼럼 Series의 데이터를 이용해 새로운 칼럼 Series 만들기
titanic_df['Age_by_10']=titanic_df['Age']*10
titanic_df['Family_No']=titanic_df['SibSp']+titanic_df['Parch']+1
titanic_df.head(3)

#새롭게 추가한 'Age_by_10' 칼럼 값을 일괄적으로 기존 값+100으로 업데이트해보기
titanic_df['Age_by_10']=titanic_df['Age_by_10']+100
titanic_df.head(3)

#예제에서 새롭게 Titanic DataFrame에 추가된 'Age_0' 칼럼을 삭제
titanic_drop_df=titanic_df.drop('Age_0', axis=1)
titanic_drop_df.head(3)

#리스트 형태로 삭제하고자 하는 칼럼명을 입력해 labels 파라미터로 입력
#titanic_df의 'Age_0', 'Age_by_10', 'Family_No' 칼럼 모두 삭제
drop_result=titanic_df.drop(['Age_0', 'Age_by_10', 'Family_No'], axis=1, inplace=True)
titanic_df.head(3)

#axis=0으로 설정해 index 0,1,2(맨 앞 3개 데이터) 로우를 삭제
pd.set_option('display.width', 1000)
pd.ser_option('display.max_colwidth', 15)
print('#### before axis 0 drop ####')
print(titanic_df.head(3))

titanic_df.drop([0,1,2], axis=0, inplace=True)

print('#### after axis 0 drop ####')
print(titanic_df.head(3))

#원본 파일 다시 로딩
titanic_df=pd.read_csv('titanic_train.csv')
#Index 객체 추출
indexes=titanic_df.index
print(indexes)
#Index 객체를 실제 값 array로 변환
print('Index 객체 array값:\n', indexes.values)

#index 객체는 식별성 데이터를 1차원 array로 갖고 있어 ndarray처럼 단일 값 반환 및 슬라이싱이 가능
print(type(indexes.values))
print(indexes.values.shape)
print(indexes[:5].values)
print(indexes.values[:5])
print(indexes[6])
#첫 번째 index 객체의 값을 5로 변경하기?
indexes[0]=5
#이 경우, TypeError 발생!! 왜냐하면 Series 객체는 Index 객체를 포함하지만 Series 객체에서 연산함수 적용시 Index는 연산에서 제외되기 때문
#Index는 오직 식별용으로만!
series_dair=titanic_df['Fare']
print('Fair Series max 값:', series_fair.max())
print('Fair Series sum 값:', series_fair.sum())
print('sum() Fair Series:', sum(series_fair))
print('Fair Series+3:\n', (series_fair+3).head(3))

#DataFrame 및 Series에 reset_index() 메서드를 수행하면 새롭게 인덱스를 연속 숫자 형으로 할당해 기존 인덱스는 'index'랄는 새로운 칼럼명으로 추가
titanic_reset_df=titanic_df.reset_index(inplace=False)
titanic_reset_df.head(3)

#Series에 reset_index()를 적용하면 Series가 아닌 DataFrame이 반환되니 유의
#기존 인덱스가 칼럼으로 추가돼 칼럼이 2개가 되므로 Series가 아닌 DataFrame이 반환
print('### before reset_index ###')
value_counts=titanic_df['Pclass'].value_counts()
print(value_counts)
print('value_counts 객체 변수 타입:', type(value_counts))
new_value_counts=value_counts.reset_index(inplace=False)
print('### After reset_index ###')
print(new_value_counts)
print('new_value_counts 객체 변수 타입:', type(new_value_counts))
#Pclass 내림차순 정렬로 새로운 index 부여

#titanic_df[0] 같은 표현식은 오류. 왜냐하면 DataFrame 뒤의 []에는 칼럼명을 지정해야 하는데, 0이 칼럼명이 아니기 때문
print('단일 칼럼 데이터 추출:\n', titanic_df['Pclass'].head(3))
print('\n여러 칼럼의 데이터 추출:\n', titanic_df[['Survived','Pclass']].head(3))
print('[] 안에 숫자 index는 KeyError 오류 발생:\n', titanic_df[0])
#오류!
#titanic_df[0:2] 같이 슬라이싱을 이용하면 인덱스로 변환 가능해 원하는 결과가 나온다

#불린 인덱싱 표현
titanic_df[titanic_df['Pclass']=3].head(3)

#승객 중 나이(Age)가 60세 이상인 데이터 추출
titanic_df=pd.read_csv('titanic_train.csv')
titanic_boolean=titanic_df[titanic_df['Age']>60]
print(type(titnaic_boolean))
titanic_boolean

#60세 이상인 승객의 나이와 이름만 추출
titanic_df[titanic_df['Age']>60][['Name','Age']].head(3)

#loc[]를 이용해도 동일하게 적용 가능하나 ['Name','Age']는 칼럼 위치에 놓여야
titanic_df.loc[titanic_df['Age']>60, ['Name','Age']].head(3)

#개별 조건을 변수에 할당하고 변수를 결합해서 불린 인덱싱 수행
cond1=titanic_df['Age']>60
cond2=titanic_df['Pclass']=1
cond3=titanic_df['Sex']='female'
titanic_df[cond1&cond2&cond3]

#titanic_df Name 칼럼으로 오름차순 정렬해 반환하기
titanic_sorted=titanic_df.sort_values(by=['Name'])
titanic_sorted.head(3)

#Pclass와 Name를 내림차순으로 정렬한 결과 반환
titanic_sorted=titanic_df.sort_values(by=['Pclass','Name'], ascending=False)
titanic_sorted.head(3)

#min(), max(), sum(), count()와 같은 aggregation 함수를 적용하면 모든 칼럼에 해당 aggregation을 적용
#단 count()는 Null 값을 반영하지 않은 결과를 반환하여 Null 값이 있는 Age, Cabin, Embarked 칼럼은 count()의 결과값이 다름
titanic_df.count()

#따라서 특정 칼럼에 aggregation 함수를 적용하기 위해서는 DataFrame에 대상 칼럼들만 추출해 aggregation을 적용
titanic_df[['Age','Fare']].mean()

#DataFrame의 groupby()는 입력 파라미터 by에 칼럼을 입력하면 대상 칼럼으로 groupby
#DataFrame에 groupby() 호출하면 DataFrameGroupBy라는 또 다른 형태의 DataFrame 반환
titanic_groupby=titanic_df.groupby(by='Pclass')
print(type(titanic_groupby))

#DataFrame에 groupby() 호출 후 반환된 결과에 aggregation 함수를 호출하면 groupby() 대상 칼럼을 제외한 모든 칼럼에 해당 aggregation 함수를 적용
titanic_groupby=titanic_df.groupby('Pclass').count()
titanic_groupby

#PassengerID와 Survived 칼럼에만 count()를 수행
titanic_groupby=titanic_df.groupby('Pclass')[['PassengerID','Survived']].count()

#aggregation 함수 명을 DataFrameGroupBy 객체의 agg() 내에 인자로 입력해서 사용-객체 인자 내에 있는 함수명을 받는다
titanic_df.groupby('Pclass')['Age'].agg([max,min])

#DataFrame의 groupby()를 이용해 API 기반으로 처리하다 보니 SQL의 group by보다 유연성이 떨어짐
#agg() 내에 입력값으로 딕셔너리 형태로 aggregation이 적용될 칼럼들과 aggregation 함수 입력
agg_format={'Age':'max', 'SibSp':'sum', 'Fare':'mean'}
titanic_df.groupby('Pclass').agg(agg_format)

#결손 데이터 처리하기
#sum()을 호출 시 True는 내부적으로 숫자 1로, False는 숫자 0으로 변환
titanic_df.isna().sum()

#fillna()로 결손 데이터 대체하기
titanic_df['Cabin']=titanic_df['Cabin'].fillna('C000')
titanic_df.head(3)

#'Age' 칼럼의 NaN 값을 평균 나이로, 'Embarked' 칼럼의 NaN 값을 'S'로 대체해 모든 결손 데이터를 처리
titanic_df['Age']=titanic_df['Age'].fillna(titanic_df['Age'].mean())
titanic_df['Embarked']=titanic_df['Embarked'].fillna('S')
titanic_df.isna().sum()

#lambda 식을 이용 DataFrame의 apply에 lambda 식을 적용해 데이터 가공
#'Name' 칼럼의 문자열 개수를 별도의 칼럼인 'Name_len'에 생성
titanic_df['Name_len']=titanic_df['Name'].apply(lambda x : len(x))
titanic_df[['Name','Name_len']].head(3)

#lambda 식에서 if else 절을 사용해 조금 더 복잡한 가공
#나이가 15세 미만이면 'Child', 그렇지 않으면 'Adult'로 구분하는 새로운 칼럼 'Child_Adult'를 apply lambda를 이용해 만들기
titanic_df['Child_Adult']=titanic_df['Age'].apply(lambda x : 'Child' if x<+15 else 'Adult')
titanic_df[['Age','Child_Adult']].head(8)
#if 절의 경우 if 식보다 반환 값을 먼저 기술해야

#나이가 15세 이하이면 Child, 15~60세 사이는 Adult, 61세 이상은 Elderly로 분류하는 'Age_Cat' 칼럼 만들기
titanic_df['Age_cat']=titanic_df['Age'].apply(lambda x : 'Child' if x<=15 else ('Adult' if x<=60 else 'Elderly'))
titanic_df['Age_cat'].value_counts()

#나이에 따라 더 세분화된 분류
#5살 이하는 Baby, 12살 이하는 Child, 18살 이하는 Teenage, 25살 이하는 Student, 35살 이하는 Young Adult, 60세 이하는 Adult, 그리고 그 이상은 Elderly로 분류
def get_category(age):
  cat=''
  if age<=5 : cat='Baby'
  elif age<=12 : cat='Child'
  elif age<=18 : cat='Teenage'
  elif age<=25 : cat='Student'
  elif age<=35 : cat='Young Adult'
  elif age<=60 : cat='Adult'
  else : cat='Elderly'

  return cat

#lambda 식에 위에서 생성한 get_category() 함수를 반환값으로 지정
#get_category(X)는 입력값으로 'Age' 칼럼 값을 받아서 해당하는 cat 반환
titanic_df['Age_cat']=titanic_df['Age'].apply(lambda x : get_category(x))
titanic_df[['Age','Age_cat']].head()