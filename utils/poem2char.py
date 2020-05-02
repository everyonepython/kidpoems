# coding = utf-8
# 把詩句變成文字及發音的列表，用於命名發音文件。
# 通過 https://hongkongvision.com/tool/cc_py_conv_zh 結果進行整理。
#
# 文本 -> ::str    '白日依山盡',
# 結果 -> ::list   ['白[baak6]',
#                  '日[jat6]',
#                  '依[ji1]',
#                  '山[saan1]',
#                  '盡[zeon6]']

import re
from pprint import pprint


pronunciation = input('把拼音翻譯結果黏貼到這裏：')

re_char = re.compile(r'[\u4e00-\u9fa5]\[[a-z0-9/]+\]')  # 注意多音字匹配。
results = re_char.findall(pronunciation)
# 結果報錯，以為又是中文問題，本想用下面方案解決，但不行。其實沒有這麼複雜，原來第一句沒有加上 coding = utf8
# results = re_char.findall(pronunciation.encode('utf8').decode('unicode-escape'))

pprint(results)
