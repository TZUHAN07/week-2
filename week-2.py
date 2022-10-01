def calculate(min, max, step):
    sum = 0
    for n in range(min, max+1, step):
        sum += n
    print(sum)


calculate(1, 3, 1)  # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2)  # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2)  # 你的程式要能夠計算 -1+1，最後印出 0


def avg(data):
    # 請用你的程式補完這個函式的區塊
    num = len(data["employees"])
    member = data["employees"]
    count = 0
    total = 0

    for i in range(0, num):
        if member[i]["manager"] == False:
            count += 1
            total += member[i]["salary"]
    print(int(total/count))


avg({
    "employees": [
        {
            "name": "John",
            "salary": 30000,
            "manager": False
        },
        {
            "name": "Bob",
            "salary": 60000,
            "manager": True
        },
        {
            "name": "Jenny",
            "salary": 50000,
            "manager": False
        },
        {
            "name": "Tony",
            "salary": 40000,
            "manager": False
        }
    ]
})  # 呼叫 avg 函式


def func(a):
    # 請用你的程式補完這個函式的區塊\
    def func2(b, c):
        print(a+(b*c))
        return a+(b*c)
    return (func2)


func(2)(3, 4)  # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5)  # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9)  # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果


def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    new = []
    for i in range(len(nums)):  # 共有多少值
        for j in range(i+1, len(nums)):
            new.append(nums[i] * nums[j])

    n = len(new)-1  # 串列長度-1
    # for i in range(0,n):
    #  for j in range(0,n-i):
    #    if (new[n]<new[n+1]):# 由大到小排序
    #      new[j],new[j+1]=new[j+1],new[j] # 兩數互換
    #  print(new)

    for i in range(0, n):
        for j in range(i + 1, n):
            if new[i] < new[j]:  # 由大到小排序
                new[i], new[j] = new[j], new[i]  # 兩數互換
    print(new[0])


maxProduct([5, 20, 2, 6])  # 得到 120
maxProduct([10, -20, 0, 3])  # 得到 30
maxProduct([10, -20, 0, -3])  # 得到 60
maxProduct([-1, 2])  # 得到 -2
maxProduct([-1, 0, 2])  # 得到 0
maxProduct([5, -1, -2, 0])  # 得到 2
maxProduct([-5, -2])  # 得到 10


def twoSum(nums, target):
    # your code here
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


result = twoSum([2, 11, 7, 15], 9)
print(result)  # show [0, 2] because nums[0]+nums[2] is 9


def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    count = 0
    result = 0
    new = []
    for i in range(0, len(nums)):
        if nums[i] == 0:
            count += 1

        else:
            count = 0

        new.append(count)
    result = max(new)
    print(result)


maxZeros([0, 1, 0, 0])  # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])  # 得到 4
maxZeros([1, 1, 1, 1, 1])  # 得到 0
maxZeros([0, 0, 0, 1, 1])  # 得到 3
