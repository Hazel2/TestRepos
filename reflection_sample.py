# -*- coding: utf-8 -*-


#テストケース
#鏡の配置は「\」「/」で表される。
#それぞれ45度、135度の角度で鏡が取り付けられていることを意味する。
testcase1 = ['--\\-\\',
             '-----',
             '--\\-/']

testcase2 = ['--\\--',
             '-/--\\',
             '-\\/-\\']

testcase3 = [
        '------\\',
        '/-\\----',
        '--\\---/',
        '-------',
        '\\-----/']

#この関数を完成させてください。
#引数は適宜追加すること
def count_reflection(panel, colX, colY, dirX, dirY, count):
    if colX < 0 or colY < 0: return count
    try:
        if panel[colX][colY] == '-':
            return count_reflection(panel, colX+dirX, colY+dirY, dirX, dirY, count)
        elif panel[colX][colY] == '/':
            return count_reflection(panel, colX-dirY, colY-dirX, -dirY, -dirX, count+1)
        elif panel[colX][colY] == '\\':
            return count_reflection(panel, colX+dirY, colY+dirX, dirY, dirX, count+1)
    except IndexError:
        return count


print count_reflection(testcase1, 0,0, 0, 1, 0)  #5
print count_reflection(testcase2, 0,0, 0, 1, 0)  #6
print count_reflection(testcase3, 0,0, 0, 1, 0)  #8
