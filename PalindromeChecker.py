from collections import deque

class PalindromeChecker:
    def __init__(self, word):
        self.stack = []
        self.queue = deque()


        self.cleaned = ''.join(char.lower() for char in word if char.isalnum())


        for char in self.cleaned:
            self.stack.append(char)
            self.queue.append(char)

    def is_palindrome(self):
        for _ in range(len(self.cleaned) // 2):
            if self.stack.pop() != self.queue.popleft():
                return False
        return True
