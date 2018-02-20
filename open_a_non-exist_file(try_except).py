try:
    f=open('non_exist.txt')
    print('file opened!')
    f.close()
except:
    print('file not exists.')
    print('done')
