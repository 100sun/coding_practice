from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        from itertools import groupby
        print(seats)

        # get the most edge idx btwn filled seats
        ans = seats.index(1)
        print(f"ans: {ans}")
        seats.reverse()
        ans = max(ans, seats.index(1))
        print(f"ans: {ans}")

        # For each group of K empty seats between two people, we can take into account the candidate answer (K+1) / 2.
        for seat, group in groupby(seats):
            if not seat:  # when empty seat group
                K = len(list(group))
                ans = max(ans, (K + 1) / 2)  # between the edge of the row and one other person
        return int(ans)

    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        print(f"n={n}, reservedSeats={reservedSeats}")
        from collections import defaultdict
        reserved_by_rows = defaultdict(set)
        for i, j in reservedSeats:
            if 2 <= j <= 9:  # not edges of the row
                reserved_by_rows[i].add(j)
        print("reserved_by_rows: ", reserved_by_rows)

        ret = 2 * n  # max n of groups = 2 groups by each row
        for i in reserved_by_rows.keys():  # By row
            reserved = reserved_by_rows[i]
            print("reserved seats in this row: ", reserved)
            # 부분집합 a & b
            if not {4, 5, 6, 7} & reserved and {2, 3, 8, 9} & reserved:
                print("\tnot part of {4, 5, 6, 7} && part of {2, 3, 8, 9}")
                ret -= 1
            elif {2, 3, 4, 5} & reserved:
                print("\tpart of {2, 3, 4, 5}")
                ret -= 1
            elif {6, 7, 8, 9} & reserved:
                print("\tpart of {6, 7, 8, 9}")
                ret -= 1
        return ret


if __name__ == '__main__':
    test = Solution()
    # print("=======================")
    # print(test.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]), 2)
    # print("=======================")
    # print(test.maxDistToClosest([1, 0, 0, 0]), 3)
    # print("=======================")
    # print(test.maxDistToClosest([0, 1]), 1)
    # print("=======================")
    # print(test.maxNumberOfFamilies(n=3, reservedSeats=[[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]), 4)
    # print("=======================")
    # print(test.maxNumberOfFamilies(n=2, reservedSeats=[[2, 1], [2, 6]]), 2)
    # print("=======================")
