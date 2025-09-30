class Solution:
    def romanToInt(self, s: str) -> int:
      roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
      }
      result = 0
      n = len(s)

      for i in range(n):
        current_value = roman_map[s[i]]
        # Check for the next character and if it's a subtractive case
        if i + 1 < n and roman_map[s[i+1]] > current_value:
            result -= current_value
        else:
            result += current_value

      return result
          