from header import *
from pprint import pprint

with open("noun_words_list.pkl", "rb") as f:
    data = pickle.load(f)

filtering_words = [
    '야설',
    '남녀역전',
    '자궁',
    '근친물',
    '좆좆좆',
    '개따먹',
    '남역',
    '떡신',
    '세따먹',
    '암컷타락',
    '다따먹',
    '떡타지',
    '암타',
]

filter_data = list(filter(lambda t : len(t) > 1 and t not in filtering_words, data))

freq = nltk.FreqDist(filter_data)

with open("filtered_freqdist.pkl", "wb") as f:
    pickle.dump(freq, f)

pprint(freq.most_common()[:500])