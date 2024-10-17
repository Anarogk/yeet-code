class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert num to list of digits
        s = list(str(num))
        
        for i in range(len(s)):
            ind = i
            
            # Find max possible number to swap with
            for j in range(len(s) - 1, i, -1):
                if s[ind] < s[j]:
                    ind = j

            # If ind gets changed
            if ind != i and s[i] < s[ind]:
                # Swap and return the result
                s[i], s[ind] = s[ind], s[i]
                return int(''.join(s))

        return num