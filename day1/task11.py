path = './dataset/data.txt'

with open(path, encoding="shift_jis") as f:
    for s_line in f:
        s_line = s_line.strip()
        print(s_line)
