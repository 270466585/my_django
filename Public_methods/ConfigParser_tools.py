# coding:utf-8

from configparser import ConfigParser
from Public_methods import Custom_exception
from Public_methods.file_path import crg_path
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
'''
读写配置文件，用ConfigParser库

'''


class Config_tools(object):

    def __init__(self,file):
        self.file=file
        self.fp=ConfigParser()
        try:
            try:
                self.fp.read(self.file)
            except:
                self.fp.read(self.file,encoding='utf-8-sig')
        except Exception as e:
            raise Custom_exception.ReadConfigError(Reason=e)

    def crg_section(self):#获取所有的section
        return self.fp.sections()
    def crg_option(self,st):#获取section的所有的key
        return self.fp.options(st)

    def crg_itme(self,st):#获取section中option的key和value
        return dict(self.fp.items(st))

    def crg_value(self,st,key):#获取option中的value
        return self.fp.get(st,key)

    def crg_dumps(self):#获取所有的section中option的key和value
        op=self.fp.sections()
        KV=[]
        for i in op:
            kv=self.fp.items(i)
            KV.append(kv)
        return KV
        # '''获取配置文件的所有sections和options和value,并以字典形式展示'''
        # # 获取config配置文件的所有sections
        # all_sections = self.fp.sections()
        # dumps_dict = {}
        # for i in all_sections:
        #     # 将每个section下的option和value以字典形式获取
        #     items = dict(self.fp.items(i))
        #     # 组合成字典：格式为{section:{option:value}}
        #     dumps_dict[i] = items
        # return dumps_dict

    def delete_itme(self,st,key):#在 section 中删除一个 item
        self.fp.remove_option(st,key)

    def delete_section(self,st):#删除一个 section
        self.fp.remove_section(st)

    def add_section(self,st):#添加一个 section
        self.fp.add_section(st)

    def set_itme(self,st,key,value):#往 section 中 添加一个 item（一个item由key和value构成）
        self.fp.set(st,key,value)

    def save(self):#在内存中修改的内容写回文件中，相当于保存
        with open(self.file,'w') as FP:
            self.fp.write(FP)

    def has_sections(self,st):  #检查section是否存在，True/False
        return self.fp.has_section(st)

    def has_option(self,st,key):    #检查option是否存在，True/False
        return self.fp.has_option(st,key)

if __name__=='__main__':
    crg_info=Config_tools(crg_path())
    crg_info.set_itme('API','number','122')
    crg_info.save()


