def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    n = len(s)
    if n == 0:
        return ""
    if n == 1:
        return s

    start = 0
    max_len = 1

    def expand(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1  

    for i in range(n):
        
        l1, r1 = expand(i, i)
        if r1 - l1 + 1 > max_len:
            start = l1
            max_len = r1 - l1 + 1

        
        l2, r2 = expand(i, i + 1)
        if r2 - l2 + 1 > max_len:
            start = l2
            max_len = r2 - l2 + 1

    return s[start:start + max_len]