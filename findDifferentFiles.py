import os
import findDifferentLines 
pl = findDifferentLines.main

def main(path1, path2):
    'prints out all files which exist in both directory path1 and directory path2 with contents which are not equal'
    pathOneFiles = os.listdir(path1)
    pathTwoFiles = os.listdir(path2)
    filesInCommon = [fil for fil in pathOneFiles if fil in pathTwoFiles and '.' in fil and fil[0] != '.']
    conflicts = []
    for fil in filesInCommon:
        contents1 = open(os.path.join(path1, fil)).read()
        contents2 = open(os.path.join(path2, fil)).read()
        if contents1 != contents2:
            conflicts.append(fil)
    if conflicts:
        print('The following files are in both directories and their contents differ:')
        i = 0
        for conflict in sorted(conflicts):
            i += 1
            print(conflict)
            pl(os.path.join(path1, conflict), os.path.join(path2, conflict))
            if i < len(conflicts):
                print()
    else:
        print('No conflicts')
main('Python/Desktop', 'Python/Notebook')
