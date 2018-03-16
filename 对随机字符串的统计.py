# 对随机字符串的统计
import string
import random

# 1 遍历
x = string.ascii_letters + string.digits + string.punctuation
y = [random.choice(x) for i in range(1000)]
z =''.join(y)


d = dict()
for ch in z :
    d[ch] = d.get(ch, 0) +1


# 2 collections 的defaultdict类
from collections import defaultdict

frequences = defaultdict(int)
for item in z :
    frequences[item] +=1
    
# 3 collections 的counter类
from collections import Counter

frequences = Counter(z)
# >>>frequences.items()
# >>>frequences.most_common(1)
# >>>frequences.most_common(2)
