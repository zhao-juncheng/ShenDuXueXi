def linear_sum(S,n):
    '''
    元素序列的递归求和
    通过前 n-1 个整数的总和加上最后一个数，递归的计算序列的和
        如果 n=0 ，S中所有 n 个整数的总和为 0
        否则，序列 S 的和应为 S 中前 n-1 个整数的总和加上 S 中最后一个元素
    思考：
        这个也是求一个数列的前 n 项的和，使用递归的方法
    :param S:待求和的元素序列
    :param n:n=len(S)
    :return:序列元素的加和
    '''
    if n==0:
        return 0
    else:
        return linear_sum(S,n-1)+S[n-1]

S=[1,2,3,4,5,6,7,8,9,10]
print(linear_sum(S,len(S)))