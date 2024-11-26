def solution(N, A):
    final = [0] * N
    max_array = max(A)
    current_max = 0
    for value in A:
        if value == max_array:
            for i in range(N):
                final[i] += current_max
        else:
            
            final[value-1] +=1 
            if final[value-1] > current_max:
                current_max = value

    return final


print(solution(5, [3,4,4,6,1,4,4]))
