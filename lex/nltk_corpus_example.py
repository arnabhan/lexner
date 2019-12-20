from lexner import get_named_entities, get_processed_text
import nltk
from tqdm import tqdm
from nltk.corpus import reuters

doc_ids = reuters.fileids()
for i in tqdm(range(len(doc_ids))):    
    text = reuters.raw(doc_ids[i]).lower()
    sents = text.split('\n')
    for sent in sents:
        sent = sent.strip()
        if len(sent) < 1: continue
        annotations = get_named_entities(sent)
        processed_text = get_processed_text(annotations)
        print("Original Text:" + sent )
        print("LexNer_Porcessed:" + processed_text)