class solution:
    def encode(self, s:str) -> str:
        builder = []
        for word in s:
            length = len(word)
            builder.append(str(length) + "#" + word)
        return "".join(builder)

    def decode(self, s:str) -> str:
        res = []
        i = 0
        j = 0
        while i < len(s):
            if j == '#':
                length = int(s[i:j])
                j += 1
                chunk = s[j:j+length]
                res.append(chunk)
                i = j + length
                j = i
            else:
                j += 1
        return res
            