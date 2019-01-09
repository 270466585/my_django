# coding:utf-8
import os,re
'''
所有文件路径创建
'''

#获取根路径
def Root_path():
    file_address=os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')
    root_Path=re.search(r'(.*)Public_methods',file_address)
    return root_Path.group(1)

#confing路径
def crg_path():
    crg_file=os.path.join(Root_path(),'Public_methods/crg_file/')
    if not os.path.exists(crg_file):os.makedirs(crg_file)
    ini_file=crg_file+'crg_file.ini'
    return ini_file



if __name__=='__main__':
    print(crg_path())
