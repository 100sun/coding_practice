# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
import time
from collections import Counter


def twoStrings_2(s1, s2):
    print(Counter(list(s1)) - Counter(list(s2)))
    return "YES" if Counter(list(s1)) - Counter(list(s2)) != Counter(list(s1)) else "NO"


def twoStrings(s1, s2):
    return "YES" if set(s1) & set(s2) else "NO"


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        start_time = time.time()
        twoStrings(s1, s2)
        print("--- %s seconds ---" % (time.time() - start_time))
