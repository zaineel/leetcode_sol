class solution:
    def firstUniqChar(self, s: str) -> int:
        freq_map = {}
        for char in s:
            if char in freq_map:
                freq_map[char] += 1
            else:
                freq_map[char] = 1
        for i in range(len(s)):
            if freq_map[s[i]] == 1:
                return i
        return -1

        # count = [0] * 26 'aabb'
        
        # for char in s:
        #     count[ord(char) - ord('a')] += 1 //[2,2,0,0,0,0,0,0,...]
        # for i, char in enumerate(s):
        #     if count[ord(char) - ord('a')] == 1: //[2,2,0,0,0,0,0,0,...]
        #         return i 
        # return -1
        
                