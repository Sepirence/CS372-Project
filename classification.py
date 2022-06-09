from header import *

hannanum = Hannanum()

with open("baseball_gallery_word_list.csv","r",encoding='utf-8') as f:
    # print(csv.reader(f))
    # bsg_rdr = [word[0] for word in list(csv.reader(f)) if isinstance(word, list) and len(word) > 0]
    bsg_words = set(word[0] for word in csv.reader(f))
    
with open("stop_words.csv", "r", encoding='utf-8') as f:
    # stop_words = [word[0] for word in list(csv.reader(f)) if isinstance(word, list)and len(word) > 0]
    stop_words = set(word[0] for word in csv.reader(f))

def filter_set_filtering(word, filter_set):
    return word in filter_set



def gen_noun_list(sent: list)->list:
    
    tagged_words_list = hannanum.pos(sent)
    noun_list = []
    for word, tag in tagged_words_list:
        if tag == 'N':
            noun_list.append(word)
    
    return noun_list

with open("genre_novel_crawling_57000_sents.csv", "r", encoding='utf-8') as f:
    # genre_words = [word[0] for word in csv.reader(f) if len(word) != 0]
    
    noun_words = []
    for idx, sent in enumerate(csv.reader(f)):
        if len(sent) == 0:
            continue
        sent = sent[0]
        noun_list = gen_noun_list(sent)
        for noun in noun_list:
            if filter_set_filtering(noun, bsg_words):
                continue
            if filter_set_filtering(noun, stop_words):
                continue
            noun_words.append(noun)    

        if idx % 1000 == 0 and idx != 0:
            print(f"{idx} sents are done")

# filtered_genre_words = list(filter(lambda t: bsg_filter(t, bsg_rdr) and stop_words_filter(t, stop_words), genre_words))

with open('noun_words_list.pkl', 'wb') as f:
    pickle.dump(noun_words, f)

freq = nltk.FreqDist(noun_words)
with open("freqdist.pkl","wb") as f:
    pickle.dump(freq, f)


print(freq.most_common()[:150])


