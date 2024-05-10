def solution(my_string, overwrite_string, s):
    answer = my_string[:int(s):] + overwrite_string + my_string[len(overwrite_string)+int(s)::]
    return answer
