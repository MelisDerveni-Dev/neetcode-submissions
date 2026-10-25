class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = []
        for char in s:
            if char.isalnum():
                alphanumeric.append(char.lower())
        print(alphanumeric)
        firstPointer = 0
        lastPointer = len(alphanumeric) - 1
        while firstPointer < lastPointer:
            if alphanumeric[firstPointer] != alphanumeric[lastPointer]:
                return False
            firstPointer += 1
            lastPointer -= 1
        return True
