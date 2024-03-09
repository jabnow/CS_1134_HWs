def two_sum(srt_lst, target):
    """
    returns two indices in a tuple: ()
    so that the elements add up to the target
    otherwise return None
    should have a linear run time
    """
    #yeah I know the formatting is wrong here
    mid = len(srt_lst)//2
    temp = 0
    right = len(srt_lst)
    for i in range(mid):
        temp = target - srt_lst[i]
        for j in range(mid, right):
            if srt_lst[j] == temp:
                return (i, j)
    return None

    #TRY 2
    # l, r = 0, len(srt_lst)-1
    # while l < r:
    #     sumd = srt_lst[l] + srt_lst[r]
    #     if sumd == target:
    #         return (l,r)
    #     elif sumd > target:
    #         r -= 1
    #     else:
    #         l += 1
    # return None

def main():
    srt_lst = [-2, 7, 11, 15, 20, 21]
    target = 22
    print(two_sum(srt_lst, target))
