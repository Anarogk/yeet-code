class Solution:
    def minLength(self, s: str) -> int:
        st = []

        for ch in s:
            if st and ch == 'B':
                if st[-1] == 'A':
                    st.pop()
                    continue
            
            if st and ch == 'D':
                if st[-1] == 'C':
                    st.pop()
                    continue
            
            st.append(ch)
        
        return len(st)