# -*- coding: utf-8 -*-

#テストケース
#(進めるマス数N, すごろくコース)
#すごろくコースの「-」は地面、「*」は落とし穴、「G」はゴールを意味する。
testcase1 = (2, '--*-*---**--G') #False
testcase2 = (3, '--*-*---**--G') #True
testcase3 = (4, '-***-***-***G') #True
testcase4 = (5, '--***-**--*G') #False
testcase5 = (5, '--***-**----*G') #True


#この関数を完成させてください。
#引数は適宜追加すること
def find_path(jump, course, current):
    if len(course)-1 < current: return True
    if course[current] == '*':
        return False
    elif course[current] == 'G':
        return True
    else:
        if find_path(jump, course, current+1):
            return True
        elif find_path(jump, course, current+jump):
            return True
        else:
            return False


print find_path(testcase1[0], testcase1[1], 0);
print find_path(testcase2[0], testcase2[1], 0);
print find_path(testcase3[0], testcase3[1], 0);
print find_path(testcase4[0], testcase4[1], 0);
print find_path(testcase5[0], testcase5[1], 0);

