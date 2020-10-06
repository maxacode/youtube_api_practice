ext = ['py','exe','ini','txt','zip']

ignoreExt = input("Which extenstion do you want to ignore? ('',' ',py,ini) - Press enter for default: ")
if ignoreExt == '':
    ignoreExt = ['',' ','py','ini']
else:
    ignoreExt = ignoreExt.split(',')

print(ignoreExt)

for x in ext:
    print(x)
    if x not in ignoreExt:
        print('+++++X is not in Ignore EXt {}'.format(x))
    else:
        print('----X in IgnoreEXt {}'.format(x))
        continue
print('Done')