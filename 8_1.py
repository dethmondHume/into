class CombStr:
    string = None
    
    def __init__(self, string):
        self.string = string

    def count_substrings(self, length):
        result = 0
        list_result = []
        for i in range(len(self.string) - length + 1):
            if length == 0:
                break
            tmp = ''
            for j in range(i, length + i):
                tmp = tmp + self.string[j]
            if list_result == []:
                list_result.append(tmp)
            else:
                flag = False
                for k in range(len(list_result)):
                    if tmp == list_result[k]:
                        flag = True
                if flag == False:
                    list_result.append(tmp)
        result = len(list_result)        
        return result
    
s0 = CombStr('qqqqqqweqqq%')
print s0.count_substrings(0) # 0
print s0.count_substrings(1) # 4
print s0.count_substrings(2) # 5
print s0.count_substrings(5) # 7
print s0.count_substrings(15) # 0
