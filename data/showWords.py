# -*- coding: utf-8 -*-

import json

from pyecharts import options as opts
from pyecharts.charts import Bar

def bar_base(words, hot) -> Bar:
    c = (
        Bar(init_opts=opts.InitOpts(width="130%", height="900px"))
        .add_xaxis(words)
        .add_yaxis('微博热搜排名', hot)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="热搜前50名", subtitle=""),
            # datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
            datazoom_opts=opts.DataZoomOpts(type_='inside'),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-30)),
        )
    )
    return c


if __name__ == '__main__':
    bar = Bar()
    with open('./test.json', 'r', encoding='utf-8') as f:
        lists = json.load(f)

        words = []
        hot = []

        for list in lists:
            words.append(list['word'])
            hot.append(list['hot'])

        bar = bar_base(words, hot)
        bar.render()