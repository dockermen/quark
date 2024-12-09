import requests
import re
import time
import random
import logging
<<<<<<< HEAD
import pandas as pd
import os,datetime
from urllib import parse

from sqlite import insert_files
from sqlite import fetch_files

if not os.path.exists("logs"):
	os.mkdir("logs")
log_file_name = datetime.datetime.now().strftime("%Y-%m-%d")+".log"
log_formatter = logging.Formatter(fmt='%(levelname)s %(funcName)s %(asctime)s %(message)s',datefmt='%Y/%m/%d %I:%M:%S %p')
log = logging.getLogger()

log_filename = "logs/"+log_file_name
file_handler = logging.FileHandler(log_filename,encoding="utf-8", mode='w')
file_handler.setFormatter(log_formatter)

log.setLevel(logging.INFO)
log.addHandler(file_handler)


def get_id_from_url(url):
=======

logging.getLogger().setLevel(logging.INFO)


def get_id_from_url(url) -> str:
    """pwd_id"""
>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
    pattern = r"/s/(\w+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
<<<<<<< HEAD
    return None


    

=======
    return ""


>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
def generate_timestamp(length):
    timestamps = str(time.time() * 1000)
    return int(timestamps[0:length])

<<<<<<< HEAD
class Quark:
    ad_pwd_id = "92e708f45ca6"

    def __init__(self, cookie: str):
=======

class Quark:
    ad_pwd_id = "0df525db2bd0"

    def __init__(self, cookie: str) -> None:
>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
        self.headers = {
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            'accept': 'application/json, text/plain, */*',
            'content-type': 'application/json',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://pan.quark.cn',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://pan.quark.cn/',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cookie': cookie}

    def store(self, url: str):
        pwd_id = get_id_from_url(url)
<<<<<<< HEAD
        
        stoken = self.get_stoken(pwd_id)
        
        #print(stoken,pwd_id)
        detail = self.detail(pwd_id, stoken)

        file_name = detail.get('title')
=======
        stoken = self.get_stoken(pwd_id)
        detail = self.detail(pwd_id, stoken)
        file_name = detail.get('title')
        from sqlite import fetch_files
>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
        if fetch_files(file_name):
            first_id, share_fid_token, file_type = detail.get("fid"), detail.get("share_fid_token"), detail.get(
                "file_type")
            task = self.save_task_id(pwd_id, stoken, first_id, share_fid_token)
            data = self.task(task)
<<<<<<< HEAD
            print(task,data)
            #print(data.get("data").get("save_as"))
            file_id = data.get("data").get("save_as").get("save_as_top_fids")[0]

            if not file_type:
                dir_file_list = self.get_dir_file(file_id)
                self.del_ad_file(dir_file_list)
                #self.add_ad(file_id)
            share_task_id = self.share_task_id(file_id, file_name)
            retry = 0
            while retry < 5:
                try:
                    share_id = self.task(share_task_id).get("data").get("share_id")
                    share_link = self.get_share_link(share_id)
                    print("-------------------------------------------------")
                    print(file_id, file_name, file_type, share_link)
                    insert_files(file_id, file_name, file_type, share_link)
                    break
                except Exception as e:
                    print("--------ERROR----------")
                    print(url,share_task_id,self.task(share_task_id),e)
                    time.sleep(3)
                    continue
                finally:
                    retry+=1
=======
            file_id = data.get("data").get("save_as").get("save_as_top_fids")[0]
            if not file_type:
                dir_file_list = self.get_dir_file(file_id)
                self.del_ad_file(dir_file_list)
                self.add_ad(file_id)
            share_task_id = self.share_task_id(file_id, file_name)
            share_id = self.task(share_task_id).get("data").get("share_id")
            share_link = self.get_share_link(share_id)
            from sqlite import insert_files
            insert_files(file_id, file_name, file_type, share_link)
>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da

    def get_stoken(self, pwd_id: str):
        url = f"https://drive-pc.quark.cn/1/clouddrive/share/sharepage/token?pr=ucpro&fr=pc&uc_param_str=&__dt=405&__t={generate_timestamp(13)}"
        payload = {"pwd_id": pwd_id, "passcode": ""}
        headers = self.headers
        response = requests.post(url, json=payload, headers=headers).json()
        if response.get("data"):
            return response["data"]["stoken"]
        else:
            return ""

    def detail(self, pwd_id, stoken):
<<<<<<< HEAD
        #stoken= parse.quote(stoken)
        print(parse.quote(stoken))
        url = f"https://drive-pc.quark.cn/1/clouddrive/share/sharepage/detail"
        headers = self.headers
        params = {
            "pr":"ucpro",
            "fr":"pc",
            "pwd_id": pwd_id,
            "stoken": stoken,
            "force":0,
=======
        url = f"https://drive-pc.quark.cn/1/clouddrive/share/sharepage/detail"
        headers = self.headers
        params = {
            "pwd_id": pwd_id,
            "stoken": stoken,
>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
            "pdir_fid": 0,
            "_page": 1,
            "_size": "50",
        }
<<<<<<< HEAD

        retry = 0
        while retry < 1:
            try:
                response = requests.request("GET", url=url, headers=headers, params=parse.urlencode(params))
                id_list = response.json().get("data").get("list")
                if id_list:
                    id_list = id_list[0]
                    data = {
                    "title": id_list.get("file_name"),
                    "file_type": id_list.get("file_type"),
                    "fid": id_list.get("fid"),
                    "pdir_fid": id_list.get("pdir_fid"),
                    "share_fid_token": id_list.get("share_fid_token")
                }
                return data 
            except Exception as e:
                print(response.json().get("data"))
            finally:
                retry+=1



    def save_task_id(self, pwd_id, stoken, first_id, share_fid_token, to_pdir_fid="ddc51a5bfb7c4ce69e7143f471b5cb51"):
        log.info("获取保存文件的TASKID")
=======
        response = requests.request("GET", url=url, headers=headers, params=params)
        id_list = response.json().get("data").get("list")[0]
        if id_list:
            data = {
                "title": id_list.get("file_name"),
                "file_type": id_list.get("file_type"),
                "fid": id_list.get("fid"),
                "pdir_fid": id_list.get("pdir_fid"),
                "share_fid_token": id_list.get("share_fid_token")
            }
            return data

    def save_task_id(self, pwd_id, stoken, first_id, share_fid_token, to_pdir_fid=0):
        logging.info("获取保存文件的TASKID")
>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
        url = "https://drive.quark.cn/1/clouddrive/share/sharepage/save"
        params = {
            "pr": "ucpro",
            "fr": "pc",
            "uc_param_str": "",
            "__dt": int(random.uniform(1, 5) * 60 * 1000),
            "__t": generate_timestamp(13),
        }
        data = {"fid_list": [first_id],
                "fid_token_list": [share_fid_token],
                "to_pdir_fid": to_pdir_fid, "pwd_id": pwd_id,
<<<<<<< HEAD
                "stoken": stoken, "pdir_fid": 0, "scene": "link"}
        response = requests.request("POST", url, json=data, headers=self.headers, params=params)
        log.info(response.json())
=======
                "stoken": stoken, "pdir_fid": "0", "scene": "link"}
        response = requests.request("POST", url, json=data, headers=self.headers, params=params)
        logging.info(response.json())
>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
        task_id = response.json().get('data').get('task_id')
        return task_id

    def task(self, task_id, trice=10):
        """根据task_id进行任务"""
<<<<<<< HEAD
        log.info("根据TASKID执行任务")
=======
        logging.info("根据TASKID执行任务")
>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
        trys = 0
        for i in range(trice):
            url = f"https://drive-pc.quark.cn/1/clouddrive/task?pr=ucpro&fr=pc&uc_param_str=&task_id={task_id}&retry_index={range}&__dt=21192&__t={generate_timestamp(13)}"
            trys += 1
            response = requests.get(url, headers=self.headers).json()
<<<<<<< HEAD
            log.info(response)
=======
            logging.info(response)
>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
            if response.get('data').get('status'):
                return response
        return False

    def share_task_id(self, file_id, file_name):
        """创建分享任务ID"""
        url = "https://drive-pc.quark.cn/1/clouddrive/share?pr=ucpro&fr=pc&uc_param_str="
        data = {"fid_list": [file_id],
                "title": file_name,
                "url_type": 1, "expired_type": 1}
        response = requests.request("POST", url=url, json=data, headers=self.headers)
        return response.json().get("data").get("task_id")

    def get_share_link(self, share_id):
        url = "https://drive-pc.quark.cn/1/clouddrive/share/password?pr=ucpro&fr=pc&uc_param_str="
        data = {"share_id": share_id}
        response = requests.post(url=url, json=data, headers=self.headers)
        return response.json().get("data").get("share_url")

    def get_all_file(self):
        """获取所有文件id"""
<<<<<<< HEAD
        log.info("正在获取所有文件")
=======
        logging.info("正在获取所有文件")
>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
        all_file = []
        url = "https://drive-pc.quark.cn/1/clouddrive/file/sort?pr=ucpro&fr=pc&uc_param_str=&pdir_fid=0&_page=1&_size=50&_fetch_total=1&_fetch_sub_dirs=0&_sort=file_type:asc,updated_at:desc"
        response = requests.get(url, headers=self.headers)
        files_list = response.json().get('data').get('list')
        for files in files_list:
            file_list = files.get("files")
            for i in file_list:
                all_file.append(i)
        return all_file

<<<<<<< HEAD
    def get_dir_file(self, dir_id):
        log.info("正在遍历父文件夹")
=======
    def get_dir_file(self, dir_id) -> list:
        logging.info("正在遍历父文件夹")
>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
        """获取指定文件夹的文件,后期可能会递归"""
        url = f"https://drive-pc.quark.cn/1/clouddrive/file/sort?pr=ucpro&fr=pc&uc_param_str=&pdir_fid={dir_id}&_page=1&_size=50&_fetch_total=1&_fetch_sub_dirs=0&_sort=updated_at:desc"
        response = requests.get(url=url, headers=self.headers)
        files_list = response.json().get('data').get('list')
        return files_list

    def del_file(self, file_id):
<<<<<<< HEAD
        log.info("正在删除文件")
=======
        logging.info("正在删除文件")
>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
        url = "https://drive-pc.quark.cn/1/clouddrive/file/delete?pr=ucpro&fr=pc&uc_param_str="
        data = {"action_type": 2, "filelist": [file_id], "exclude_fids": []}
        response = requests.post(url=url, json=data, headers=self.headers)
        if response.status_code == 200:
            return response.json().get("data").get("task_id")
        return False

    def del_ad_file(self, file_list):
<<<<<<< HEAD
        log.info("删除可能存在广告的文件")
=======
        logging.info("删除可能存在广告的文件")
>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
        for file in file_list:
            file_name = file.get("file_name")
            from ad_check import ad_check
            if ad_check(file_name):
                task_id = self.del_file(file.get("fid"))
                self.task(task_id)

    def add_ad(self, dir_id):
<<<<<<< HEAD
        log.info("添加个人自定义广告")
=======
        logging.info("添加个人自定义广告")
>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
        pwd_id = self.ad_pwd_id
        stoken = self.get_stoken(pwd_id)
        detail = self.detail(pwd_id, stoken)
        first_id, share_fid_token = detail.get("fid"), detail.get("share_fid_token")
<<<<<<< HEAD
        #print(pwd_id, stoken, first_id, share_fid_token, dir_id)
        task_id = self.save_task_id(pwd_id, stoken, first_id, share_fid_token, dir_id)
        self.task(task_id, 1)
        log.info("广告移植成功")

    def search_file(self, file_name):
        log.info("正在从网盘搜索文件🔍")
=======
        task_id = self.save_task_id(pwd_id, stoken, first_id, share_fid_token, dir_id)
        self.task(task_id, 1)
        logging.info("广告移植成功")

    def search_file(self, file_name):
        logging.info("正在从网盘搜索文件🔍")
>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
        url = "https://drive-pc.quark.cn/1/clouddrive/file/search?pr=ucpro&fr=pc&uc_param_str=&_page=1&_size=50&_fetch_total=1&_sort=file_type:desc,updated_at:desc&_is_hl=1"
        params = {"q": file_name}
        response = requests.get(url=url, headers=self.headers, params=params)
        return response.json().get('data').get('list')


if __name__ == '__main__':
<<<<<<< HEAD
    cookie = '_UP_A4A_11_=wb96914f9cd44da88aca1069d68cf27d; b-user-id=e4145741-a9ce-64bb-a183-7caebebb6c7b; _UP_D_=pc; xlly_s=1; __pus=5fb62a842d6efcc1d6a331ddee27ba9bAATkORlhnIJVtjCAZ532H/OxpWMaHfKRJw7Qdk3uclaHb2X7LhZXxUg6M1qdo1bUzId0WPlIxM7mC3L1xSU+ymEn; __kp=768e1110-b475-11ef-aec1-c9f4031e6bed; __kps=AARDFtwPcujezLpaTtnoSehy; __ktd=VidtWUbkC7czZYutWVQ+pA==; __uid=AARDFtwPcujezLpaTtnoSehy; tfstk=fxFSelDAh3x5neXPCeQqcN_K4XcQyk1ZwegLSydyJbh8JXZj04JPEvSQhkEq2QlJwDMQAVNUaaXkHmEKx0hUU0uLcyERr27uO-AQSyVPrX7oZzcn9GSN_6aurXqwxRe17mdxRrdppaygIshn9GS23BHl1XqME5Ku9rQj82tKykHKDmnm8LnLv0HvDVgi9XhLvmHxW2RJ2Lp-kxnmJXnLvXhwHsg1F2U5ulkz3499tSmX9CTiPYIY2pRkZSgSFWU-cwQLG4MSXxqeIhN80yFzZxXHLX44CkwLDsO7AzeTv0PAXBiUI2aK5fLwsratRAhKhedLlbnmpqGO6ng0HzyLZuTB94Vz_viihwdnLjFZBREW-N4xw2EnIWSMZ0ULS52Z16OxNvIrBCo132JBH1AIlc7flpvhh7wn6zeOg4k-o4qNlZtXKY3mlK7flprteq02LZ_XVcf..; isg=BMvLN_Q7KMft_3QJOsq1-cNaWm-1YN_i3ALNtD3Ar4phXOC-xTEPMkc0Mlyy_Dfa; __puus=67754f0399746794c1c89adf48349c88AAR9Fx83oY+/nn6PV0TVDLXxo7lxlinmSL3DXHJkCcwUC6+IBMBrLlPzzrNdu5j3jIZKAbEUSsoYOSujAO1eNJljuX7hVyzoLJsfWPydVnzYbsNK3zB1lxvuym2WNzFcpyththwubC9ORTgMiNSHmBs1ieCq++vfQQgxxS6RAbU5AbV7WexStDXWNgRFipiLjiEi9ar90Bbe9QGu/xMI0FP/'
    quark = Quark(cookie)
    df = pd.read_excel("./info.xlsx")
    df.columns = ["name","url","time"]
    for url in df["url"][618:]:
        quark.store(url)
    # a = quark.task("d22b9dcf661843629965b93a144542c9").get("data")
    # print(a)
    # share_task_id = quark.share_task_id("9630f4cb18fe4af2bfce3fb83eacae1c","02-登堂认母（60集）")
    # share_id = quark.task(share_task_id).get("data").get("share_id")
    # share_link = quark.get_share_link(share_id)
    # insert_files("9630f4cb18fe4af2bfce3fb83eacae1c", "02-登堂认母（60集）", 0, share_link)
    
=======
    cookie = ''
    quark = Quark(cookie)
    quark.store('https://pan.quark.cn/s/92e708f45ca6#/list/share')

>>>>>>> a809bc79fb404a98cf6865ab955902af3b0049da
