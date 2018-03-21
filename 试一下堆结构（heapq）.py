# 堆是一种很重要的数据结构（就是我看不懂）

import heapq
import random

data = random.sample(range(1000),10)        # 生成随机测试数据
heapq._heapify(data)                        # 堆化随机测试数据

heapq.heappush(data, 30)                   # 新元素入堆，自动调整堆结构
heapq.heappop(data)                        # 返回并删除最小的元素，自动调整堆结构
heapq.heappop(data)
heapq.heappop(data)                        # 删它三次试下

heapq.heappushpop(data, 1000)              # 弹出最小元素，同时新元素入堆
heapq.heapreplace(data, 500)               # 作用同上

heapq.nlargest(3, data)                    # 返回最大的前3个元素
heapq.nsmallest(2, data, key = str )       # 返回指定排序规则下最小的3个元素