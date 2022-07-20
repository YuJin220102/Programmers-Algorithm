def solution(numbers):
    numbers = list(map(str, numbers))
    # x * 3은 조건이 1000이하이기 때문에 
    # 303030, 333 을 비교하면 [0] : 3 = 3
    #                       [1] : 0 = 3을 통해 333이 앞에 정렬 되도록 함 
    # str 정렬은 [0]인덱스부터 차례대로 아스키 코드로 변환하여 비교함
    # int 정렬을 했다면 [10, 6, 2], str 정렬은 [6, 2, 10]
    numbers.sort(key = lambda x : x * 3, reverse = True)
    # str(int())는 00000...을 0으로 바꾸기 위해 사용
    return str(int(''.join(numbers)))
