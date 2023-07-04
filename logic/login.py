from dataBaseControl.DataStudent import *


def login(id, password):
    """
    :param id: 学号或工号
    :param password: 密码
    :return:  list 账户存在则为[True,id],否则为[Flase,0]
    """
    return quiryaccount(id, password)
