CALL C:\Users\zengc\Miniconda2\Scripts\activate.bat C:\Users\zengc\Miniconda2\envs\im2txt

cd weiboComment
scrapy crawl weibo -o ../data/words.json

cd ../data
python showWords.py
render.html
del words.json

cd ../weiboComment
scrapy crawl wordcomment