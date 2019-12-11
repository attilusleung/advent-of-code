in1 = int(input())
in2 = int(input())

count = 0
skip = 0
lis = []

for i in range(in1, in2):
    double = False
    decrease = True
    s = str(i)
    for i in range(0, 5):
        if s[i] > s[i+1]:
            decrease = False
    if not decrease: continue

    i = 0
    while i < 5:
        if s[i] == s[i+1]:
            if i < 4 and s[i] == s[i+2]:
                print(f"{s}, {double}")
                j = i+1
                while j < 6 and s[i] == s[j]:
                    j += 1
                i = j
                continue
            double = True
        i += 1

    if double and decrease:
        count += 1
        lis.append(s)

print(lis)
print(count)







# for i in range(in1, in2+1):
#     s = str(i)
#     double = False
#     decrease = True
#     for i in range(0, 5):
#         if s[i+1] < s[i]:
#             decrease = False
#             break
#         if s[i] == s[i+1]:
#             if i < 4 and s[i] == s[i+1]:
#                 j = i+1
#                 while s[i] == j < 6 and s[j]:
#                     skip += 1
#                     j += 1
#                 continue
#             double = True
#
