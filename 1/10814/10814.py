import sys

input = sys.stdin.readline()

n = int(input())

members = list()
for i in range(n):
    members.append(input().split())

members.sort(key=lambda member: int(member[0]))
for member in members:
    print(f'{member[0]} {member[1]}')
