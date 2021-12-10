def singleNumber(nums):
    one, two = 0, 0
    for x in nums:
        print("\n==========x=========")
        print(f"one:{one} two:{two}")
        one = one ^ x  # bitwise exclusive or
        print(f"one:{one} two:{two}")
        two = two | (one & x)  # bitwise or bitwise and
        print(f"one:{one} two:{two}")
        three = two & x  # bitwise and
        print(f"one:{one} two:{two} three:{three}")
        one = one & ~three  # bitwise and not
        print(f"one:{one} two:{two} three:{three}")
        two = two & ~three  # bitwise and not
        print(f"one:{one} two:{two} three:{three}")
    return one

print(singleNumber([2,2,3,2]))