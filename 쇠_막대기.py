
##stack을 사용함 (LIFO)

bar = list(input())
answer = 0
st = []

for i in range(len(bar)):
    if bar[i] == '(':
        st.append('(')

    else:                       # ')'가 나온다면 
        if bar[i-1] == '(':     # 한 조각이다
            st.pop()            # 마지막 )는 뺴고 세야하므로,
            answer += len(st)   # bar에 쌓인 ( 개수만큼 더한다.

        else: 
            st.pop()            # )와 짝을 이루는 (를 하나씩 빼줌  
            answer += 1 

    print(st)