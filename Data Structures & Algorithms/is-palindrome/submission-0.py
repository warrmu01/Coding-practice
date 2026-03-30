class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove non-alphanumeric characters and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        Start = 0
        End = len(s) - 1

        # Compare characters from both ends
        while Start < End:
            if s[Start] != s[End]:  # If mismatch found
                return False
            Start += 1  # Move Start pointer forward
            End -= 1    # Move End pointer backward

        return True  # Return True if no mismatch found    