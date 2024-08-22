class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res , line , width = [], [], 0

        for w in words: # for each word
            if width + len(w) + len(line) > maxWidth: # if no of words + len of word + len(line) > max width:
                for i in range(maxWidth - width): # for i in range(max - curr)
                    line[i% (len(line)-1 or 1)] += ' '
                res, line, width = res + ["".join(line)], [], 0
            line+=[w]
            width += len(w)

        return res + [" ".join(line).ljust(maxWidth)]