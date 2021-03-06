import MeCab
import gensim
import sys
import re
from gensim.models import word2vec

sys.path.append("/.pyenv/versions/anaconda3-4.3.1/envs/word2vec/lib/python3.6/site-packages")
with open("newkashi.txt","w") as n:
    with open("kashi.txt","rb") as f:
        binarydata = f.read()
        text = binarydata.decode('utf_8')
        text = re.sub(r'<br/>', '  ', text)
        text = re.sub(r'<br>', '  ', text)
        text = re.sub(r'</br>', '  ', text)
        text = re.sub(r'</div>, <div id="kashi_area" itemprop="text">', '\n', text)
        text = re.sub(r'</div>]', '', text)
        text = re.sub(r'<div id="kashi_area" itemprop="text">', '', text)
        n.write(text)
    print(text)

m = MeCab.Tagger("-Owakati")

with open("wakachi.txt","w") as f:
    result = m.parse(text)
    print(result)
    f.write(result) # skip first \s

print(result[0])

#sentences = word2vec.LineSentence("wakachi.txt")
sentences = word2vec.Text8Corpus("wakachi.txt")
model = word2vec.Word2Vec(sentences, size=100, window=5, min_count=5, workers=4)
vector = model.wv["僕"]
word = model.most_similar( [ vector ], [], 5)
print(vector)
print(word)

#model = word2vec.Word2Vec(sentences,
 #                         sg=1,
  #                        size=100,
   #                       min_count=1,
    #                      window=7,
     #                     hs=1,
      #                    negative=0)

#print(model.most_similar("が"))
