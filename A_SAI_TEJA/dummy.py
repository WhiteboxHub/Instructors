'''def find_runner_score(n,score):
    if n<2:
        return 'invalid input. there should be at least 2 participants'

    unique_score = sorted(set(score), reverse=True)


    if len(unique_score)>1:
        return unique_score[1]
    else:
        return 'there is a no runner up.all score are same'

if __name__ == '__main__':

    n=int(input('enter the number of perticipants'))
    score = list(map(int,input('enter the score separated by space: ').split()))

    runner_up_score = find_runner_score(n, score)
    print('the runnner up score is:', runner_up_score)'''

import calendar
print(calendar.calendar(2022))

