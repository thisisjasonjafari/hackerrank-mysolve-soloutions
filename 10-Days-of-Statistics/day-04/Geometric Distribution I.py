def geometric_prob(r,p):
    print(round( ((1-p)**(r-1))*p,3))

a,b=map(int,input().split())
r=int(input())
p=a/b
geometric_prob(r,p)