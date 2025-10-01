from collections import Counter
from math import comb, factorial

MOD = 10**9 + 7

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        freq = Counter(map(int, num))
        n = len(num)
        even_slots = (n + 1) // 2
        odd_slots = n // 2
        
        # dp[diff][even_used][odd_used] = ways
        dp = {(0, 0, 0): 1}
        
        for d in range(10):
            if freq[d] == 0:
                continue
            
            new_dp = {}
            count = freq[d]
            
            for put_even in range(count + 1):
                put_odd = count - put_even
                for (diff, used_even, used_odd), ways in dp.items():
                    if used_even + put_even <= even_slots and used_odd + put_odd <= odd_slots:
                        ndiff = diff + d * (put_even - put_odd)
                        ne = used_even + put_even
                        no = used_odd + put_odd
                        
                        new_dp[(ndiff, ne, no)] = (new_dp.get((ndiff, ne, no), 0) + ways * comb(even_slots - used_even, put_even) * comb(odd_slots - used_odd, put_odd)) % MOD
            dp = new_dp
        
        ans = 0
        for (diff, used_even, used_odd), ways in dp.items():
            if diff == 0 and used_even == even_slots and used_odd == odd_slots:
                ans = (ans + ways) % MOD
        
        return ans
