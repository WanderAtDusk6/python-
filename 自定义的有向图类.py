# 自定义有向图类(模拟有向图创建与数据搜索)

class DirectedGraph(object):
    def __init__(self, d):
        if isinstance(d, dict):
            self.__graph = d
        else:
            self.__graph = dict()
            print("Sth error")

    def __generatePath(self, graph, path, end, results):
        current = path[-1]         # 见下面的[start]
        print('  内部2',path)
        if current == end:         # 与给出的end相同，就将它（这条path）放入result（这个方法的形参，实际是外面的21处的self.__result = []）
            results.append(path)
            print('  内部2的结束')
        else:
            for n in graph[current]:     # 找到那条路的末尾，查出末尾能通向的路
                if n not in path:        # 防止无限循环
                    print('    内部3开始，选中的是',n)
                    self.__generatePath(graph, path+[n], end, results)
                    print('    内部3结束')

    def searchPath(self, start, end):
        self.__results = []                                             # 一个在init外的实例属性，空列表，在下1,2句调用,用作保存path
        print('外部1-1启动')
        self.__generatePath(self.__graph, [start], end, self.__results )    # 这个中括号里的start是什么鬼,,,,没见过这样的形参啊？？
        print('外部1-2 结束')
        self.__results.sort(key = lambda x: len(x))                         # 排序
        print("The part from ",self.__results[0][0], ' to ', self.__results[0][-1], " is:")     # 传入的d里就有列表所以[][],但为什么只有一个[0]和[-1]中间的呢
        for path in self.__results:
            print(path)                         # path 来自self.__results的遍历


d = {'A':['B','C','D'],
     'B':['E'],
     'C':['D','F'],
     'D':['B','E','G'],
     'E':['D'],
     'F':['D','G'],
     'G':['E']}
g = DirectedGraph(d)
# g.searchPath('A','D')
g.searchPath('A','E')