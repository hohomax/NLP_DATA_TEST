from konlpy.tag import Komoran
komoran = Komoran()
print(komoran.morphs('우왕 한글을 분석해보자 어떻게 분석하는거지'))
print(komoran.nouns(u'한글이 섞여있어도 가능한건가 this is english'))
print(komoran.pos(u'한글형태소분석기 코모란 테스트 중 입니다.'))


#['우왕', '코', '모란', '도', '오픈소스', '가', '되', '었', '어요']
#['오픈소스', '관심', '개발자']
#[('한글', 'NNG'), ('형태소', 'NNP'), ('분석기', 'NNG'), ('코모', 'NNP'), ('란', 'JX'), ('테스트', 'NNG'), ('중', 'NNB'), ('이', 'VCP'), ('ㅂ니다', 'EF'), ('.', 'SF')]
