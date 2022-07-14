def solution(progresses, speeds):
    p_list = []
    count, index = 0, 0

    while(True):
        if(index == len(speeds)) : break
        if(progresses[index] <= 100):
            progresses[index] += speeds[index]
            count += 1
        else:
            if((progresses[index] - speeds[index]) == 100) : count -= 1
            p_list.append(count)
            index += 1
            count = 0

    count, index = 1, 0
    answer = []
    for i in range(1, len(p_list)):
        if(p_list[index] >= p_list[i]):
            count += 1
        else:
            answer.append(count)
            index += count
            count = 1
        
    answer.append(count)
    return answer
