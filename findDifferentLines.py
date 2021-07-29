def main(file1, file2):
    i = 0
    lst1 = open(file1).readlines()
    lst2 = open(file2).readlines()
    while i < max(len(lst1), len(lst2)):
        i += 1
        try:
            line1 = lst1[i]
        except:
            line1 = ''
        try:
            line2 = lst2[i]
        except:
            line2 = ''
        if line1 != line2:
            print(f"({i})   {' '.join(line1[:-1].split())}   !=   {' '.join(line2[:-1].split())}")
