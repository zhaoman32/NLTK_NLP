import nltk

from nltk.book import *


# 查找特定词及其上下文
text1.concordance("monstrous")
# 出现在和monstrous相似的上下文中
text1.similar("monstrous")
# 共用两个或两个以上词汇的上下文
text2.common_contexts(["monstrous", "very"])
# 语料中的单词离散图
text4.dispersion_plot(["citizens", "America", "freedom"])
# 根据text3的风格生成随机文本
text3.generate()
# 对文本词汇排序
sorted(set(text3))
# 对词汇丰富度测量，每个词平均使用了16次
len(text3) / len(set(text3))
# 特定词在文中占百分比
text4.count("a") / len(text4)
# sent1 和 text 是以链表形式储存
print(sent1)
# 创建给定样本的频率分布
fdist = FreqDist(text4)
# 给定样本的频率
fdist.freq("monstrous")
# 以递减的顺序排序
fdist.keys()
# 绘制频率分布表，分布图
fdist.tabulate()
fdist.plot()