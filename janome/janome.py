from janome.tokenizer import Tokenizer
t = Tokenizer()
for token in t.tokenize(u'すもももももももものうち'):
    print(token.decode('utf_8'))