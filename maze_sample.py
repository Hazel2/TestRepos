# -*- coding: utf-8 -*-


"""
問題：
以下のような迷路の地図が与えられたとき、STARTからGOAL
またはTREASUREが示す座標へのルートを計算する。
"""
MAZE=['**** * *     ',
      '*    * *** * ',
      '** * *     * ',
      '** * * *** * ',
      '** *       * ',
      '** ********* ',
      '**     *     ',
      '****** ******'
     ]
START = (0,6)
TREASURE = (6,8)
GOAL = (7,6)


def show_route(route):
    """
    与えられた座標の配列を地図上に表示する
    """
    for i,row in enumerate(MAZE):
        tmprow = ''
        for j,cell in enumerate(row):
            if (i,j) in route:
                tmprow+='@'
            else:
                tmprow+=cell
        print tmprow











class Player(object):
    def __init__(self, startX, startY):
        self.posX = startX
        self.posY = startY
        
        #地図データから座標同士の接続を表すグラフを作る
        mapping = {}
        for i,row in enumerate(MAZE):
            for j,cell in enumerate(row):
                if cell == '*':
                    continue
                if j+1 < len(row) and MAZE[i][j+1] == ' ':
                    mapping[(i,j,i,j+1)] = True
                if 0 <= j-1 and MAZE[i][j-1] == ' ':
                    mapping[(i,j,i,j-1)] = True
                if i+1 < len(MAZE) and MAZE[i+1][j] == ' ':
                    mapping[(i,j,i+1,j)] = True
                if 0 <= i-1 and MAZE[i-1][j] == ' ':
                    mapping[(i,j,i-1,j)] = True        
        self.map = mapping

    def move_to(self, desX, desY):
        self.posX = desX
        self.posY = desY

    def find_route(self, goalX, goalY):
        return self.__find_route([], self.posX, self.posY, goalX, goalY)

    def __find_route(self, passed_route, virX, virY, goalX, goalY):
        """
        @param passed_route それまでに通過した座標の配列
        @param virX, virY 探索対象の仮想座標
        @param goalX,goalY 目的地の座標
        """
        #print virX, virY, goalX, goalY
        tmp_route = passed_route[:]
        tmp_route.append((virX, virY))

        if (virX,virY) == (goalX,goalY):
            return tmp_route
        elif (virX, virY) in passed_route:
            return None
        
        reached_route = []
        if self.map.get((virX,virY,virX,virY+1)):
            route = self.__find_route(tmp_route, virX,virY+1,goalX, goalY)
            if route:
                reached_route.append(route)
        if self.map.get((virX,virY,virX,virY-1)):
            route = self.__find_route(tmp_route, virX,virY-1,goalX, goalY)
            if route:
                reached_route.append(route)
        if self.map.get((virX,virY,virX+1,virY)):
            route = self.__find_route(tmp_route, virX+1,virY,goalX, goalY)
            if route:
                reached_route.append(route)
        if self.map.get((virX,virY,virX-1,virY)):
            route = self.__find_route(tmp_route, virX-1,virY,goalX, goalY)
            if route:
                reached_route.append(route)

        if len(reached_route) > 0:
            minroute = None
            for route in reached_route:
                if not minroute:
                    minroute = route
                elif len(minroute) > len(route):
                    minroute = route
            return minroute
        else:
            return None

player = Player(*START)

print "Find route to TREASURE."
route2treasure = player.find_route(*TREASURE)
if route2treasure:
    show_route(route2treasure)

print "-------------------------"
print "Find route to GOAL."
route2goal = player.find_route(*GOAL)
if route2goal:
    show_route(route2goal)

print "-------------------------"
print "Find route from TREASURE to GOAL."
player.move_to(*TREASURE)
treasure2goal = player.find_route(*GOAL)
if treasure2goal:
    show_route(treasure2goal)
