# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
import time
from collections import Counter
import itertools
from collections import Counter


def count_anagrams(string):
    buckets = {}
    for i in range(len(string)):
        for j in range(1, len(string) - i + 1):
            key = frozenset(Counter(string[i:i + j]).items())  # O(N) time key extract
            buckets[key] = buckets.get(key, 0) + 1
    count = 0
    for key in buckets:
        count += buckets[key] * (buckets[key] - 1) // 2
    return count


# [a,a], [b,b], [ab,ba], [abb,bba]
def sherlockAndAnagrams(s):
    pairs = set()
    n_pairs = 0
    for i in range(1, len(list(s))):
        all_pairs = list()
        for j in range(len(list(s))):
            k = j + 1
            while k + i - 1 <= len(list(s)):
                k += 1
                all_pairs.append(s[j] + s[k:k + i - 1])
        print(all_pairs)


def sherlockAndAnagrams_1(s):
    pairs = set()
    n_pairs = 0
    for i in range(1, len(list(s))):
        all_pairs = [''.join(sorted(i)) for i in list(itertools.combinations(list(s), i))]
        for k, v in Counter(all_pairs).items():
            if v % 2 == 0:
                print(k)
                n_pairs += 1
    return n_pairs


def isAnagrams(s1, s2):
    return sorted(s1) == sorted(s2)


if __name__ == '__main__':
    print(isAnagrams('aba', 'aba'))
    # q = int(input())

    for q_itr in range(1):
        # s = input()
        start_time = time.time()
        result = sherlockAndAnagrams('abba')
        print(result)
        print("--- %s seconds ---" % (time.time() - start_time))

        start_time = time.time()
        result = count_anagrams('abba')
        print(result)
        print("--- %s seconds ---" % (time.time() - start_time))
