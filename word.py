import wordcloud
import re
import jieba
r = '[’!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]+\\n'
w = wordcloud.WordCloud(width=1000,height=700,background_color='white')
with open('resume.txt') as f:
    str = f.read()
    str = re.sub(r, '', str)
    words = jieba.lcut(str)
    print(words)
    w.generate(str)
    w.to_file('word.png')