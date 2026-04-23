class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ll = 0
        i = 0
        st = set()

        for j in range(len(s)):
            while(s[j] in st):
                st.remove(s[i])
                i+=1
            st.add(s[j])
            window_size = j - i +1     
            ll = max(ll, window_size)
        
        return ll
