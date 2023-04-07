#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        # vowels = 'aeiou'
        # vowel_index = []
        # vowel_result = []
        # for i, char in enumerate(s):
        #     if char.lower() in vowels:
        #         vowel_index.append(i)
        #         vowel_result.append(char)

        # new_string = ''
        # n = len(s)
        # n_vowel = len(vowel_index)
        # for j in range(n):
        #     if j in vowel_index:
        #         index_j = vowel_index.index(j)
        #         new_string = new_string + vowel_result[n_vowel-1-index_j]
        #     else:
        #         new_string = new_string + s[j]
        # return new_string
        # a e i o u                                         #元音元素
        dic = {'a','e','i','o','u','A','E','I','O','U'}     #大小写元音元素集合作为判断依据
        pol = 0                                             #左指针
        por = len(s)-1                                      #右指针
        s_ = list(s)                                        #str类型数据无法直接查询in和not in，转换为list
        while pol < por:                                    #左右指针交错循环停止
            if s_[pol] in dic and s_[por] in dic:           #左右指针所指元素均在集合中
                s_[pol], s_[por] = s_[por], s_[pol]         #交换左右指针所指元素
                por -= 1                                    #右指针左移
                pol += 1                                    #左指针右移
            if s_[por] not in dic:                          #右指针所指元素不在集合中
                por -= 1                                    #右指针左移
            if s_[pol] not in dic:                          #左指针所指元素不在集合中
                pol += 1                                    #左指针右移
        return ''.join(s_)                                  #返回str格式数据


# @lc code=end
