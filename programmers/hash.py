# [(["leo", "kiki", "eden"], ["eden", "kiki"]),
#           (["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]),
#           (["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])]
def marathon_solution(participant, completion):
    from collections import Counter
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]


# [["113333", "115555", "345555", "555555", "345444"], ["1234", "1235", "567"], ["12", "13"], ["113", "44", "4544"],["119", "97674223", "1195524421"], ["123", "456", "789"], ["12", "123", "1235", "567", "88"]]
def phone_sorting_solution(phone_book):
    print(phone_book, end=" -> ")
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book) - 1):
        # print(f"{phone_book[i + 1]} starts with {phone_book[i]} ?? ")
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True


# [[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]],  # 5
#           [["yellowhat", "headgear"], ["bluesunglasses", "face"], ["green_turban", "eyewear"]],  # 7
#           [["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]]  # 2
def spy_prod_solution(clothes):
    import math
    ct_clothes = {}
    for clothe in clothes:
        if clothe[1] in ct_clothes.keys():
            ct_clothes[clothe[1]] += 1
        else:
            ct_clothes[clothe[1]] = 1
    return math.prod([x + 1 for x in ct_clothes.values()]) - 1


def solution(genres, plays):
    answer = []
    ct = {genre: [] for genre in set(genres)}
    [ct[genre].append((play, i)) for i, (genre, play) in enumerate(zip(genres, plays))]
    for genre in sorted(ct, key=lambda x: sum(i[0] for i in ct[x]), reverse=True):
        answer.extend(list(map(lambda x: x[1], sorted(ct[genre], key=lambda x: x[0], reverse=True)[0:2])))
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))  # [4, 1, 3, 0]
print(solution(["classic", "pop", "classic", "classic"], [500, 600, 150, 800]))  # [4, 1, 3, 0]
print(
    solution(["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))  # [0, 1, 2, 4]
