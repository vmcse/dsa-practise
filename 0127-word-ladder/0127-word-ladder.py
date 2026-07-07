from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set(wordList)
        wordset.add(beginWord)

        if endWord not in wordset:
            return 0
        
        q = deque([(beginWord, 1)])
        visited = {beginWord}

        while q:
            word, dist = q.popleft()

            if word == endWord:
                return dist
            
            for i in range(len(word)):
                alphabets = "abcdefghijklmnopqrstuvwxyz"
                for c in alphabets:
                    if c == word[i]:
                        continue

                    next_word = word[:i] + c + word[i+1:]

                    if next_word in wordset and next_word not in visited:
                        visited.add(next_word)
                        q.append((next_word, dist + 1))
        
        return 0

            

