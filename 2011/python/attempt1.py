class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        inc = operations.count("++X") + operations.count("X++")
        dec = operations.count("--X") + operations.count("X--")
        return inc - dec