#1.설치
# pip install langchain
# pip install langchain-openai

#2.모델 초기화
from google.colab import userdata
from langchain_openai import ChatOpenAI

api_key = userdata.get('OPENAI_API_KEY')
llm = ChatOpenAI(openai_api_key=api_key)

# 3.langchain 모델 기본 사용
output = llm.invoke("2024년 청년 지원 정책에 대하여 알려줘")

# 4.Template 기반 사용법
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system","너는 청년을 행복하게 하기 위한 정부정책 안내 컨설턴트야"),
    ("user","{input}")
])

chain = prompt | llm
#