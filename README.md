# WhoCanConsider

> 这谁能想到？

本项目需要安装**tensorflow**、**spider**

## Usage

> 根据自己的anaconda环境配置start.bat

start.bat文件

```
CALL C:\Users\zengc\Miniconda2\Scripts\activate.bat C:\Users\zengc\Miniconda2\envs\im2txt

cd weiboComment
scrapy crawl weibo -o ../data/words.json

cd ../data
python showWords.py
render.html
del words.json

cd ../weiboComment
scrapy crawl wordcomment
```

`CALL C:\Users\zengc\Miniconda2\Scripts\activate.bat C:\Users\zengc\Miniconda2\envs\im2txt`这句话需要根据自己的环境配置，修改俩个`C:\Users\zengc`为你的用户目录，然后默认anaconda安装目录为`C:\Users\{USERNAME}\Miniconda2`，后面的环境路径配置为**你自己的环境路径**即可（此环境路径必须安装了一开始提到的俩个python库）。

- `run start.bat`

