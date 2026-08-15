
class Solution:

    def encode(self, strs: List[str]) -> str:
        # for i in range(len(strs)):
            # enco = ("#",strs[i])
        result = ""
        for i in strs:
            result += str(len(i)) + "#" + i
        return result

    def decode(self, s: str) -> List[str]:
        # for i in range(len(enco)):
        # return enco.split("#")
        
        result = []

        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            L = int(s[i:j])
            word = s[(j+1) : (j+L+1)]

            result.append(word)

            i = j + 1 + L
        return result 

