from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordSize = len(words[0])
        numWords = len(words)
        windowSize = wordSize * numWords
        n = len(s)
        result = []
        
        # Create a Counter for the target words
        wordCount = Counter(words)
        
        # Loop to check each starting index within the word size boundaries
        for i in range(wordSize):
            start = i
            currentCount = Counter()
            count = 0  # To track matched words
            
            # Slide a window of size `windowSize` over the string
            for j in range(i, n - wordSize + 1, wordSize):
                word = s[j:j + wordSize]
                
                # If the word is part of `words`, process it
                if word in wordCount:
                    currentCount[word] += 1
                    count += 1
                    
                    # If we exceed the desired count, move the start pointer
                    while currentCount[word] > wordCount[word]:
                        leftWord = s[start:start + wordSize]
                        currentCount[leftWord] -= 1
                        count -= 1
                        start += wordSize

                    # If all words are matched, record the starting index
                    if count == numWords:
                        result.append(start)
                
                # If the word is not in `words`, reset the counters
                else:
                    currentCount.clear()
                    count = 0
                    start = j + wordSize

        return result
