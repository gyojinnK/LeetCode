class Solution:
    # 애너그램: 각기 다른 단어지만 사용되는 문자가 같은 단어
    # 1. 정렬
    # 2. 정렬된 값을 키로 갖는 딕셔너리 생성
    # 3. 해당 키에 단어들을 대입
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())
