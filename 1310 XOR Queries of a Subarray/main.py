class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        for query in queries:
            if query[0] == query[1]:
                answer.append(arr[query[0]])
            else:
                answer.append(arr[query[0]] ^ arr[query[1]])
        return answer
