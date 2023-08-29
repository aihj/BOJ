s=list(input())
tag=False
bag=''
result=''

# bag에 한글자씩 추가하고, 공백과 >을 만날때마다 bag을 result에 비워준다.
for i in s:
  if tag==False: #괄호밖일 때 
        if i=='<': #괄호 안으로 가! 
            tag=True
            bag=bag+i

        elif i==' ':
            bag=bag+i
            result=result+bag 
            bag='' ##bag 비움 

        else: #거꾸로 더하기
            bag=i+bag #bag에 남아있는 글자들은 괄호밖 뿐
            

  elif tag==True: #괄호안 글자일때, 차례대로 추가하다가 >를 만나면 비움
        bag=bag+i        
        if i=='>':
            tag=False
            result=result+bag
            bag='' ##bag 비움 

print(result+bag)
