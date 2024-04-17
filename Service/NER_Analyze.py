from konlpy.tag import Okt
from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch

# KoNLPy 형태소 분석기 초기화
okt = Okt()

# 입력 텍스트
text = "수원시 율현중학교 학생들이 항상 즐겁고 올바른 길로 성장할 수 있도록 도움이 되주고 선생님들께서 항상 타의 모범이 되어주시고 자라나는 새싹들의 의견을 잘 수렴해주시어 학생들이 중심이되는 21세기 참교육의 본보기가 될수있는 참된 학교입니다. 이런 자라나는 새싹들에게 비료가 되어줄 수 있는 짜장면이 저희에게 기부된다면 정말 꿈을 이룬듯 행복하며 기뻐할 것입니다. 이렇게 척박하고 갑갑한 세상에서 배달의 민족과 율현중학교의 콜라보레이션으로 따른 중학교들에게 희망과 행복을 나누어주며 항상 학업으로 인해 스트레스와 핍박을 받던 학생들에게 자유롭고 행복한 시간을 주시면 정말 사랑하고 또 사랑하겠습니다. 저희 율현중학교 학생들이 배달의 민족을 항상 유용하게 사용하고 있는 것은 아실것입니다. 사랑과행복이 넘쳐나고 더불어 살아가는 세상에 본보기가 되는 우리 율현중학교에 희망과 사랑이 되어주시기바랍니다❤"

# 형태소 분석 수행
tokens = okt.morphs(text)

model_name = "monologg/koelectra-small-finetuned-naver-ner"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# 토큰화 및 NER 태그 예측
inputs = tokenizer(tokens, return_tensors="pt", is_split_into_words=True)
outputs = model(**inputs)

predictions = torch.argmax(outputs.logits, dim=2)
ner_results = [model.config.id2label[p.item()] for p in predictions[0]]

# 결과 출력
print("Tokens:", tokens)
print("NER Tags:", ner_results)