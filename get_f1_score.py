from header import *


# print(parsed_word_abbv_pairs)
novel_abbv_pairs = [
('아카살',  "아카데미에서 살아남기"), 
('창작물',       "창작물 속으로"),
('전1시',       "전지적 1인칭 시점"),
('괴담동',      "괴담동아리"),
('미래편지',    "미래에서 온 연애편지"),  
('악살싶',      "악당은 살고 싶다"),  
('빌환',        "빌어먹을 환생"),    
('후회프듀',    "후회 안 하는 프로듀서"),
('검머외',       "이세계 검은 머리 외국인"),
('아카빵',       "아카데미 히로인 오른쪽 대각선 뒷자리"),
('마녀시티',     "마녀의 도시"),
('메나죽',       "메인 히로인들이 나를 죽이려 한다"),
('약관동의',     "약관 동의는 신중히"),
('아카쿠로',     "아카데미 검은머리 외국인"),
('종말갤',       "종말 후 외톨이 갤러리"),
('매도엘프',     "매도당하고 싶은 엘프님"),
('대마대',       "대마법사였던것은 다시 대마법사를 꿈꾼다"),
('타락성녀',     "절대 타락시키는 용사, 절대 타락하지 않는 성녀"),
('이블파티',     "나의 악당들"),
('악영싫',       "악역 영애가 되긴 싫어"),
('약관',         "약관 동의는 신중히"),
('무림서부',     "무림서부"),
('악영길',       "악당 영애 길들이기"),
('석화용사',     "15일뒤 석화에서 풀리는 용사"),
('약먹마',       "약먹는 천재마법사"),
('악신살',       "악신에게서 살아남기"),
('회맹성',       "회귀자와 맹인 성녀"),
('나혼소',       "나 혼자 소드 마스터"),
('아포사이비',   "아포칼립스 사이비 교주"),
('무노자',       "무림 속 외노자가 되었다"),
('주빌런',       "주인공이 빌런임"),
('히강악',       "히로인을 강탈한 악당이 되었다"),
('무림티비',     "잘 보이는 무림티비!"),
('석화',         "15일뒤 석화에서 풀리는 용사"),
('소엑',         "소설 속 엑스트라"),
('마녀도시',     "마녀의 도시"),
('용파때',       "용사 파티 때려치웁니다"),
('겜바바',       "게임 속 바바리안으로 살아남기"),
('히로히로',     "히어로 IN 히로인"),
('용파짐',       "용사파티의 짐꾼"),
('일편독심',     "일편독심"),
('드유',         "드래곤을 유괴하다"),
('아카편의점',   "아카데미 편의점으로 힐링 할게요"),
('얼굴천재',     "아카데미 얼굴천재가 되었다"),
('그살',         "그래도 살아간다"),
('ntr용사',      "15일뒤 석화에서 풀리는 용사"),
('매도깐프',     "매도당하고 싶은 엘프님"),
('데몬소드',     "데몬 소드"),
('마학간',       "마왕은 학원에 간다"),
('주술초월',     "주술사는 초월을 원한다"),
('마저씨',       "마법소녀 아저씨"),
('몰루빙의',     "모르는 만화에 빙의했다"),
('이불사',       "이세계 불법체류 사이비"),
('13회귀',       "회귀도 13번이면 지랄 맞다"),
('게이살',       "아카데미 플레이어를 죽였다"),
('예수천국',     "예수천국 불신지옥"),
('1525',         "6명이 25명이 될 때까지 못 나감"),
('세최딸',       "세계 최강 딸내미"),
('아카게이살',   "아카데미 플레이어를 죽였다"),
('이밀헌',       "이세계 밀프 헌터"),
('템빨',         "템빨"),
('걸소아',       "걸그룹 소설 아닌데요?"),
('아카방해',     "아카데미 주인공, 방해합니다."),
('마없세',       "마왕이 없는 세계"),
('이예르폴',     "오, 이예르! 이예르폴!"),
('아카매점',     "아카데미 최강의 매점아저씨"),
('마왕학원',     "마왕은 학원에 간다"),
('히집악',       "히어로가 집착하는 악당이 되었다"),
('눈마새',       "눈물을 마시는 새"),
('헌터여고',     "헌터 여고의 남선생"),
('해적영애',     "저주받은 해적선장과 빡대가리 해적영애"),
('메모라이즈',   "메모라이즈"),
('러스트',       "러스트"),
('소꿉천마',     "소꿉친구는 천재 마법사"),
('체육고',       "체육고 영재로 회귀했다"),
('전툴루',       "전생하고 보니 크툴루"),
('자븝미',       "자해하는 미친 븝미"),
('아카편',       "아카데미 편의점으로 힐링 할게요"),
('아카검머외',   "아카데미 검은머리 외국인"),
('무카살',       "무림에서 카드로 살아남기"),
('옥탑방',       "옥탑방 엘프"),
('전생마왕',     "전생마왕의 합리적인 생존전략"),
('감옥학원',     "감옥학원에서 나만 힐링할거다"), 
('반지하',       "반지하 오크"),
('창염',         "창염의 피닉스"),
('모스크바',     "모스크바의 여명"),
('아카경비',     "아카데미 경비원으로 빙의당했다"),
('암살영애',     "전직 암살자는 귀족영애가 됩니다"),
('반로환동전',   "21세기 반로환동전"),
('메슬',         "메이지 슬레이어"),
('수상남매',     "수상할 정도로 사이가 좋은 남매"),
('아카메디',     "아카메디 아카데미"),
('마약소꿉',     "마약 소꿉친구가 되었다"),
('회귀13',       "회귀도 13번이면 지랄 맞다"),
('경성훈타',     "경성의 헌터 아카데미"),
('탑매',         "탑 매니지먼트"),
('경성헌터',     "경성의 헌터 아카데미"),
('마최물',       "마법소녀 최면물"),
('탐재',         "탐식의 재림"),
('스자헌',       "SSS급 죽어야 사는 헌터"),
('회사설',       "회귀자 사용설명서"),
('히로보디',     "히어로 보디가드"),
('괴담',        "괴담 동아리"),
('괴물서커스',    "괴물서커스단의 단장이 되었다"),
('구진엑',       "구라 안치고 진짜 엑스트라"),
('귀축교사',      "귀축교사"),
('나작소감금',     "나작소 작가에게 감금당했다."),
('나혼렙',       "나 혼자만 레벨업"),
('납골당',       "납골당의 어린 왕자"),
('닉잘못',       "닉네임을 잘못 정했다"),
('달조',        "달빛조각사"),
('딥블랙시티',    "딥블랙시티"),
('레오네',       "부디, 레오네라 불러주시길"),
('망겜성',       "겜의 성기사"),
('맹인성녀',      "회귀자와 맹인 성녀"),
('묵향',        "묵향"),
('백야',        "백야"),
('별품소',       "별을 품은 소드마스터"),
('빡대용',       "빡대가리 용사파티의 용사가 되었다"),
('소꿉전여친',    "날 차버린 소꿉친구와 전 여친이 같은 반이라 곤란하다"),
('아찐네크',     "아싸 찐따 네크로맨서"),
('아카선비',     "아카데미 선비의 생활일지"),
('아카야겜',     "아카데미 야겜에 빙의했다."),
('악녀호위',     "로판 속 악녀의 호위기사가 되었다"),
('악역영애',     "악역 영애가 되긴 싫어"),
('어반흑막',     "어반판타지속 흑막이 되었다"),
('업키걸',      "업어 키운 걸그룹"),
('여소빙',      "여러 소설에 동시에 빙의당했다"),
('여왕죽',      "여왕을 죽여라"),
('오궁도화',     "오궁도화"),
('용키',        "용사 키우기"),
('우주괴물',     "진화하는 우주괴물이 되었다"),
('우주천마',     "우주천마 3077"),
('자해븝미',     "자해하는 미친 븝미"),
('제냥꾼',      "제국사냥꾼"),
('쥐뿔',       "쥐뿔도 없는 회귀"),
('천재흑마',    "천재 흑마법사"),
('천하소꿉',    "천하제일인의 소꿉친구"),
('친애언니',    "친애하는 언니께"),
('카드아카',    "카드 아카데미 1타강사"),
('판작살',     "판타지 세상에서 작가로 살아가는 법"),
('히로히',     "히어로 IN 히로인"),
]
#                 진짜                                       추정
# true positive:  히집악 - 히어로가 집착하는 악당이 되었다   히집악 - 히어로가 집착하는 악당이 되었다
# true negative:  히집악 - 히어로가 집착하는 악당이 되었다   히집악 - 히로히로가 집중하는 악동뮤지션
# false positive: 100화 - 없음                               100화 - 이세계에서 100년동안 화력발전했으니 사직합니다. 
# false negative: 100화 - 없음                               100화 - 없음

def determiner(parsed_word_abbv_pairs: list, genuine_word_abbv_dict: dict):
    confusion_list = []
    for pair in parsed_word_abbv_pairs:
        # false
        # pair = pair[0]
        parsed_word = pair[0]
        parsed_abbv = pair[1]
        if parsed_word not in genuine_word_abbv_dict:
            
            if parsed_abbv == "UNDEF":
                # true negative
                confusion_list.append('TN')
            else:
                # false positive
                confusion_list.append('FP')
            continue
        # true
        genuine_abbv = genuine_word_abbv_dict[parsed_word]
        if genuine_abbv == parsed_abbv:
            # true positive
            confusion_list.append('TP')
        else:
            # false negative
            confusion_list.append('FN')
    return confusion_list

def accuracy(confusion_list: list):
    TP_cnt = confusion_list.count('TP')
    TN_cnt = confusion_list.count("TN")
    return (TP_cnt + TN_cnt) / len(confusion_list)

def precision(confusion_list: list):
    TP_cnt = confusion_list.count('TP')
    FP_cnt = confusion_list.count("FP")

    return TP_cnt / (TP_cnt + FP_cnt)

def recall(confusion_list: list):
    TP_cnt = confusion_list.count('TP')
    FN_cnt = confusion_list.count("FN")

    return TP_cnt / (TP_cnt + FN_cnt)

def f1_score(confusion_list: list):
    p = precision(confusion_list)
    r = recall(confusion_list)
    return 2 / ((1/p) + (1/r))

genuine_word_abbv_dict = {word: title for word, title in novel_abbv_pairs}

# with open(f"results/abbv_parsing_result_[].tsv", "r", encoding='utf-8') as f:
#     parsed_word_abbv_pairs = []
#     for pair in csv.reader(f, delimiter='\t'):
#         parsed_word_abbv_pairs.append(pair)
#     confusion_list = determiner(parsed_word_abbv_pairs, genuine_word_abbv_dict)
#     print(f"results/abbv_parsing_result_none.tsv")
#     print(f'accuracy: {accuracy(confusion_list):.2f}\nprecision: {precision(confusion_list):.2f}\nrecall: {recall(confusion_list):.2f}\nf1 score: {f1_score(confusion_list) * 100:.2f}')

algorithms_names = ['abbv_1', 'abbv_2', 'matching_1', 'matching_2']
algo_permutations = []
for i in range(1, len(algorithms_names)+1):
    algo_permutations.extend(list(itertools.permutations(algorithms_names, r = i)))

df = pandas.DataFrame(columns= ['file name', 'Accuracy', 'Precision', 'Recall', 'F1 Score'])

for i, name_list in enumerate(algo_permutations):
    with open(f"results/abbv_parsing_result_{list(name_list)}.tsv", "r", encoding='utf-8') as f:
        parsed_word_abbv_pairs = []
        for pair in csv.reader(f, delimiter='\t'):
            parsed_word_abbv_pairs.append(pair)
    confusion_list = determiner(parsed_word_abbv_pairs, genuine_word_abbv_dict)

    df.loc[i] = [f"results/abbv_parsing_result_{list(name_list)}.tsv",
                accuracy(confusion_list) ,
                precision(confusion_list) ,
                recall(confusion_list) ,
                f1_score(confusion_list) * 100]

    print("=============================================")
    print(f"results/abbv_parsing_result_{list(name_list)}.tsv")
    print(f'accuracy: {accuracy(confusion_list):.2f}\nprecision: {precision(confusion_list):.2f}\nrecall: {recall(confusion_list):.2f}\nf1 score: {f1_score(confusion_list) * 100:.2f}')
df.to_csv('results/collection_of_result.tsv', sep= '\t', index= False)