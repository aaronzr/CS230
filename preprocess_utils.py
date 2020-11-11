import pandas as pd
import re
from bs4 import BeautifulSoup
from langdetect import detect
import pdb
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize

def csvtonumpy(csv_path):
    pandas_frame = pd.read_csv(csv_path, encoding = 'utf-8')
    numpy_data = pandas_frame.to_numpy()
    return numpy_data

def get_important_info(numpy_data):
    num_datapoints, num_cols = numpy_data.shape
    important_data = numpy_data[:, [3, 5, 8, num_cols - 1]]
    return important_data

def replace1(matchobj):
    match_string = matchobj.group(0)
    new_string = match_string[0] + ' '
    return new_string

def replace2(matchobj):
    match_string = matchobj.group(0)
    new_string = match_string[:2] + ' ' + match_string[2]
    return new_string

def clean(numpy_data):
    num_datapoints, num_features = numpy_data.shape
    cleaned_data = numpy_data.copy()
    toremove = dict.fromkeys((ord(c) for c in u'\xa0\n\t'))
    pattern1 = "[!\.\?\),;:]  +"
    pattern2 = "[a-z0-9'\"\.][!\.\?\),;:][A-Z]"

    for i in range(num_datapoints):
        raw_question = numpy_data[i, 0]
        raw_answer = numpy_data[i, 2]

        # remove weird characters that html parser doesn't get
        cleaned_question = raw_question.translate(toremove)
        cleaned_answer = raw_answer.translate(toremove)

        # remove html stuff
        qsoup = BeautifulSoup(cleaned_question, 'html.parser')
        asoup = BeautifulSoup(cleaned_answer, 'html.parser')
        cleaned_question = qsoup.get_text()
        cleaned_answer = asoup.get_text()

        # remove superfluous spaces after punctuation
        cleaned_question = re.sub(pattern1, replace1, cleaned_question)
        cleaned_answer = re.sub(pattern1, replace1, cleaned_answer)

        # make sure sentences are separated by spaces
        cleaned_question = re.sub(pattern2, replace2, cleaned_question)
        cleaned_answer = re.sub(pattern2, replace2, cleaned_answer)

        cleaned_data[i, 0] = cleaned_question
        cleaned_data[i, 2] = cleaned_answer

        del asoup
        del qsoup

    return cleaned_data

def remove_foreign_sentences(numpy_data):
    num_datapoints = numpy_data.shape[0]
    mask = []
    for i in range(num_datapoints):
        clean_question = numpy_data[i, 0]
        clean_answer = numpy_data[i, 2]
        q_lang = detect(clean_question)
        a_lang = detect(clean_answer)
        if q_lang != 'en' or a_lang != 'en':
          mask.append(False)
        else:
          mask.append(True)
    return numpy_data[mask]

def split_data(numpy_data):
    train_mask = (numpy_data[:, 3] == 'train')
    val_mask = (numpy_data[:, 3] == 'val')
    test_mask = (numpy_data[:, 3] == 'test')

    train = numpy_data[train_mask][:, :3]
    val = numpy_data[val_mask][:, :3]
    test = numpy_data[test_mask][:, :3]
    return train, val, test

def split_sentences(data):
    num_answers = data.shape[0]
    tokenized_sentences = []
    for i in range(num_answers):
        answer = data[i]
        sentences = sent_tokenize(answer)
        tokenized_sentences.append(sentences)
    return tokenized_sentences
