cnt_ee = 0
cnt_eb = 0

string = input()

for i in range(len(string) - 1):
    if string[i:i+2] == 'ee':
        cnt_ee += 1
    if string[i:i+2] == 'eb':
        cnt_eb += 1

print(cnt_ee, cnt_eb)