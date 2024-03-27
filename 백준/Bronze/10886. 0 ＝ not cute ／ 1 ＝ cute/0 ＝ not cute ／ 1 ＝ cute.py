n = int(input())
survey = []
for i in range(n):
    survey.append(int(input()))
if survey.count(0) < survey.count(1):
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")