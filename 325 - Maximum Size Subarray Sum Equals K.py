def getLongestSubarray(a,k):
    
    n = len(a)
    prevSum = {0:1}
    total = 0
    res = 0
    for r in range(n):
        total += a[r]
        
        if total == k:
            res = max(res , r + 1)
        
        rem  = total - k
        if rem in prevSum:
            res = max(res, r - prevSum[rem])
        if total not in prevSum:
            prevSum[total] = r
    return res
            
        
if __name__ == "__main__":
  a = [-1, 1, 1]
  k = 2
  
  length = getLongestSubarray(a, k)
  print(f"The length of the longest subarray is: {length}")



