class Global:
    '''需要定义全局变量的放在这里，最好定义一个初始值'''
    u_id= 0

# 对于每个全局变量，都需要定义get_value和set_value接口
def set_id(id):
    Global.u_id = id
def get_id():
    return Global.u_id
