import zipfile,os

def compress(get_files_path, set_files_path,pwd):


    print("正在压缩....")
    f = zipfile.ZipFile(set_files_path, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(get_files_path):
        fpath = dirpath.replace(get_files_path,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            f.write(os.path.join(dirpath,filename), fpath+filename)
    f.close()
    if pwd=="ang":
     print('\n'.join([''.join([('ang'[(x-y) % len('ang')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
     print("        forever on-line")
    else:
     print("压缩完成")

    input("Prease <enter>")


def checkfile(get_files_path):
    if os.path.exists(get_files_path)==False:
        print("路径输入错误")
        get_files_path = input("重新输入需要压缩的文件路径：")#需要压缩的文件夹
        checkfile(get_files_path)
    else:
        # 存放的压缩文件地址(注意:不能与上述压缩文件夹一样)
        set_files_path = get_files_path+".zip"
        compress(get_files_path, set_files_path,pwd)


if __name__=='__main__':
    pwd = input("使用者密码：")#需要压缩的文件夹
    get_files_path = input("需要压缩的文件路径：")#需要压缩的文件夹
    checkfile(get_files_path)



