class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        Start = 0
        End = len(s) - 1

        while Start < End:
            s[Start], s[End] = s[End], s[Start]
            Start += 1
            End -= 1