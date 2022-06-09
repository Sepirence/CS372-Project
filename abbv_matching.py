from os import remove
from header import *

novel_title_set = set()
tagged_novel_dict = dict()

with open("crawled_novel_data.tsv", "r", encoding='utf-8') as f:
    for novel_data in csv.reader(f, delimiter="\t"):
        tagged_novel_dict[novel_data[0]] = tuple(novel_data[1:])
        novel_title_set.add(novel_data[0])    

with open("novel_titles.csv", "r", encoding='utf-8') as f:
    for novel_data in csv.reader(f):
        novel_title_set.add(novel_data[0])

def gen_abbv_title_dict(novels: list, title_set: set) -> dict:
    abbv_title_dict = defaultdict(set)
    
    for idx, novel in enumerate(novels):
        abbv_char_list = list(novel)
        for title in novel_title_set:
            target_abbv = abbv_char_list[:]
            target_title = list(title)

            while len(target_abbv) > 0:
                char = target_abbv.pop(0)
                if char not in target_title:
                    break
                target_title.remove(char)
            else:
                abbv_title_dict[''.join(abbv_char_list)].add(title)
        if len(list(abbv_title_dict[novel])) == 0:
            continue

    return abbv_title_dict

with open("filtered_freqdist.pkl", "rb") as f:
    freq = pickle.load(f)
novels = []
for word, num in freq.most_common()[:500]:
    novels.append(word)
'''
가설
0 모든 글자가 제목에 들어있다

매칭 
1. 모든 글자가 순서에 맞게 들어갔다
2. 단어의 첫글자가 제목의 첫글자일 것이다

줄임말이냐 아니냐
1. 단어 - 제목들, 제목들의 개수가 너무 많으면(>5) 줄임말이 아닐 것이다
2. 단어 - 제목들, 단어 자체가 제목안에 있는 경우 줄임말이 아닐 것이다

알고리즘
1. 매-1 줄-1 줄-2 매-2 
2. 매-1 줄-2 줄-1 매-2
3. 매-2 줄-1 줄-2 매-1
'''

def matching_1(abbv_title_match_dict: dict):
    '''
    모든 글자가 순서에 맞게 들어갔다.
    '''
    for key, values in abbv_title_match_dict.items():
        if len(values) == 1:
            continue
        
        abbv_list = list(key)
        remove_set = set()
        for title in values:
            target_abbv = abbv_list[:]
            target_title = title[:]

            while len(target_abbv) > 0:
                char = target_abbv.pop(0)
                index = target_title.find(char)
                if index == -1:
                    break
                target_title = target_title[index+1:]
            else:
                continue
            remove_set.add(title)
        abbv_title_match_dict[key] -= remove_set
    return abbv_title_match_dict

def matching_2(abbv_title_match_dict: dict):
    '''
    단어의 첫글자가 제목의 첫글자이다.
    '''
    
    for word, titles in abbv_title_match_dict.items():
        if len(titles) == 1:
            continue
        remove_set = set()
        for title in titles:
            if word[0] != title[0]:
                remove_set.add(title)
        abbv_title_match_dict[word] -= remove_set
            
    return abbv_title_match_dict


def abbv_1(abbv_title_match_dict: dict, threshold=5):
    '''
    단어 - 제목들, 제목들의 개수가 너무 많으면 줄임말이 아닐 것이다.
    '''
    remove_word_list = []
    for word, titles in abbv_title_match_dict.items():
        
        if len(titles) > threshold:
            remove_word_list.append(word)
    for word in remove_word_list:
        del abbv_title_match_dict[word]
    
    return abbv_title_match_dict


def abbv_2(abbv_title_match_dict: dict):
    '''
    단어 - 제목들, 단어 자체가 제목안에 있는 경우 줄임말이 아닐 것이다.
    '''

    for word, titles in abbv_title_match_dict.items():
        if len(titles) == 1:
            continue
        remove_set = set()
        for title in titles:
            if word in title:
                remove_set.add(title)
        
        abbv_title_match_dict[word] -= remove_set
    
    return abbv_title_match_dict

def final_processing(title_dict: dict) -> dict:
    # f = open("ccc.tsv", "r", encoding="utf-8") 
    word_title_pair = []
    for word, titles in title_dict.items():
        if len(titles) > 1:
            title_list = []
            for title in titles:
                if title in tagged_novel_dict:
                    title_list.append((title, number_resolution(tagged_novel_dict[title][1])))
                else:
                    title_list.append((title, 0))
            title_list.sort(key=lambda x: x[1])
            word_title_pair.append((word, title_list[-1][0]))
    
    for word, title in word_title_pair:
        title_dict[word] = set([title])
    
    return title_dict

def number_resolution(num_string):
    num_field = float(num_string[:-2])
    num_unit = num_string[-2]
    if num_unit == "K":
        return int(num_field * 1000)
    elif num_unit == "M":
        return int(num_field * 1000000)
    elif num_unit == "B":
        return int(num_field * 1000000000)
    else:
        print("resolution error", num_string)
        return 0

title_dict = gen_abbv_title_dict(novels, novel_title_set)
title_dict = final_processing(title_dict)
with open(f"results/abbv_parsing_result_none.tsv", "w", encoding= 'utf-8', newline='') as f:
    tw = csv.writer(f, delimiter="\t")
    word_title_pair = []
    for word, title_set in title_dict.items():
        if len(title_set) == 0:
            word_title_pair.append((word, "UNDEF"))
        else:
            word_title_pair.append((word, list(title_set)[0]))
    for pair in word_title_pair: 
        tw.writerow(pair)

algorithms = [abbv_1, abbv_2, matching_1, matching_2]
algorithms_names = ['abbv_1', 'abbv_2', 'matching_1', 'matching_2']

algorithms_pairs = list(zip(algorithms, algorithms_names))
algo_permutations = []
for i in range(1, len(algorithms_pairs)+1):
    algo_permutations.extend(list(itertools.permutations(algorithms_pairs, r = i)))

for algo_pair in algo_permutations:
    title_dict = gen_abbv_title_dict(novels, novel_title_set)
    name_list = []
    for algo_fx, name in algo_pair:
        title_dict = algo_fx(title_dict)
        name_list.append(name)
    title_dict = final_processing(title_dict)

    with open(f"results/abbv_parsing_result_{name_list}.tsv", "w", encoding= 'utf-8', newline='') as f:
        tw = csv.writer(f, delimiter="\t")
        word_title_pair = []
        for word, title_set in title_dict.items():
            if len(title_set) == 0:
                word_title_pair.append((word, "UNDEF"))
            else:
                word_title_pair.append((word, list(title_set)[0]))
        for pair in word_title_pair: 
            tw.writerow(pair)