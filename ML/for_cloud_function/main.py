import tensorflow as tf
import pickle
import re

from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def preprocess(sents, max_len=58):
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


def predict(sents):
  preprocessed = preprocess(sents)
  preds = model.predict(preprocessed)
  return preds

with open('tokenizer_stem.pickle', 'rb') as handle:
  tokenizer = pickle.load(handle)
model = tf.keras.models.load_model('binary_repo_83_41.h5')
stemmer = None

# Comment lines below if you don't want to use stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

def run(request):
  try:
    request_json = request.get_json()
    sents = request_json['inputs']
    predictions = predict(sents)

    request_json['pred_vals'] = predictions.tolist()
    request_json['pred_flags'] = [False if p < 0.5 else True for p in predictions]
  except Exception as e:
    request_json['error'] = str(e)

  return request_json