class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max = 0
        for sentence in sentences:
            if len(sentence.split()) > max:
                max = len(sentence.split())
        
        return max