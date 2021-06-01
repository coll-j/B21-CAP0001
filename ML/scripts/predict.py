import tensorflow as tf
import pickle
import numpy as np
import re
import argparse

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def load_kamus_alay():
  kamus_alay = pd.read_csv('new_kamusalay.csv', encoding="ISO-8859-1", header=None)
  kamus_alay_dict = {}
  for i, row in kamus_alay.iterrows():
    kamus_alay_dict[row[0]] = row[1]

def load_tokenizer(tokenizer_filename):
  with open(tokenizer_filename, 'rb') as handle:
    tokenizer = pickle.load(handle)
    return tokenizer

def preprocess(sents, tokenizer, stemmer=None, max_len=58):
  lower_sents = [s.lower() for s in sents]
  cleaned = lower_sents
  if stemmer is not None:
    cleaned = list(map(lambda s: stemmer.stem(s), cleaned)) # stemming
  query = r'[^a-zA-Z\d\s]' # ambil alphanumeric saja
  cleaned = list(map(lambda s: re.sub(query, ' ', s), cleaned))
  query = r'(?:^| )\w(?:$| )'
  cleaned = list(map(lambda s: re.sub(query, ' ', s), cleaned)) # hilangkan single letter
  query = r" +"
  cleaned = list(map(lambda s: re.sub(query, ' ', s.strip()), cleaned)) # hilangkan trailing spaces
  seq = tokenizer.texts_to_sequences(cleaned)
  seq = tf.keras.preprocessing.sequence.pad_sequences(seq, maxlen=max_len)

  return seq

def load_model(model_filename):
  model = tf.keras.models.load_model(model_filename)
  return model

def predict(sent):
  preprocessed = preprocess(sent, tokenizer)
  preds = model.predict(preprocessed)
  return preds

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-s', '--single', nargs='+', default=None)
  parser.add_argument('-t', '--text', default=None)
  parser.add_argument('-j', '--json', nargs='+', default=None)

  opts = parser.parse_args()
  sent = opts.single
  txt_path = opts.text
  print(sent, txt_path)

  if txt_path is not None:
    sent = []
    with open(txt_path, 'r') as txt_file:
      lines = txt_file.readlines()
      for line in lines:
        sent.append(line.strip())

  tokenizer = load_tokenizer('../tokenizer_stem.pickle')
  factory = StemmerFactory()
  stemmer = factory.create_stemmer()
  model_file = '../binary_repo_83_41.h5'
  model = load_model(model_file)

  # sent = ['test', '123']
  predictions = predict(sent)
  print(predictions)