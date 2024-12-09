import sqlite3

import sqlite3


def fetch_files(file_name):
    """检索文件,如果已存在那么返回False"""
    conn = sqlite3.connect('file.db')
    c = conn.cursor()
    c.execute('SELECT FILE_NAME FROM ALL_FILE WHERE FILE_NAME =?', (file_name,))
    files = c.fetchall()
    conn.close()
    if files:
        return False
    return True


def insert_files(file_id, file_name, file_type, share_link):
    """插入文件"""
    conn = sqlite3.connect('file.db')
    c = conn.cursor()
    c.execute("INSERT INTO ALL_FILE (file_id,file_name,file_type,url) VALUES (?,?,?,?)", (file_id, file_name, file_type, share_link))
    conn.commit()
    conn.close()


def update_files(file_id, file_name):
    conn = sqlite3.connect('file.db')
    c = conn.cursor()
    c.execute("UPDATE ALL_FILE SET FILE_ID=? WHERE FILE_NAME=?", (file_id, file_name))
    conn.commit()
    conn.close()


#fetch_files("莫里斯.Maurice.1987.1080p.冰冰字幕组.V2.mp4")
#print("INSERT INTO ALL_FILE VALUES (?,?,?,?)", ("958cd7ebcde649338ddb111e83d380cf","23-死后我断情绝爱（40集）白雪茹",0,"https://pan.quark.cn/s/699ff0cf6942"))
#insert_files("958cd7ebcde6498ddb111e83d380cf","23-死断情绝爱（40集）白雪茹",0,"https://pan.quark.cn/s/699ff0cf6942")
#print(fetch_files("23-死后我断情绝爱（40集）白雪茹"))
