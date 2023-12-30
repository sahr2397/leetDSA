fout = open('user.out', 'w')

for nums in map(loads, sys.stdin):
    N = len(nums)
    rv = [_ for _ in nums if _ != 0]
    rv.extend(
        [0] * (N - len(rv))
    )
    print(
        dumps(rv).replace(' ', ''), 
        file=fout
    )

fout.close()
exit()