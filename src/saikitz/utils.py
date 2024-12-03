from IPython.display import Markdown, display
from pathlib import Path

from PIL import Image
from io import BytesIO

import base64

__all__ = ["printmd","lastoflistdict","img_to_base64",
           "base64_to_img","baseURL_optimize"]

def printmd(string):
    """用于在Jupyter Notebook中打印Markdown格式的字符串"""
    display(Markdown(string))

def lastoflistdict(dict_list:list[dict], key:any, value:any) -> int :
    """
    用于获取固定字典组成的列表中满足要求的最后一个字典的索引。
    """
    max_index = -1
    n = len(dict_list)
    for i in range(n) :
        if key in dict_list[i].keys() :
            if dict_list[i][key] == value :
                max_index = i
    return max_index

def img_to_base64(img_path:str|Path,
                  return_type:str = "ollama") -> str :
    """将图片转换为base64编码"""
    with open(Path(img_path), "rb") as files:
        img = files.read()
    encoded_image = base64.b64encode(img).decode('utf-8')
    match return_type :
        case "ollama":
            return encoded_image
        case "openai":
            return "data:image/jpeg;base64," + encoded_image
        case _ :
            raise ValueError("Invalid return_type")

def base64_to_img(base64_str:str, save_path:str|Path) -> None :
    """将base64编码转换为图片"""
    if "data:image/jpeg;base64," in base64_str :
        txtimg = base64_str.split(",")[1]
    else :
        txtimg = base64_str
    file_like = BytesIO(base64.b64decode(txtimg))
    img = Image.open(file_like)
    img.save(save_path)

def baseURL_optimize(base_url:str|None) -> str :
    """连接匹配"""
    match base_url :
        case "kimi" :
            return "https://api.moonshot.cn/v1",base_url
        case "qwen" :
            return "https://dashscope.aliyuncs.com/compatible-mode/v1",base_url
        case "ollama" :
            return 'http://localhost:11434',base_url
        case None :
            return "https://api.moonshot.cn/v1","kimi"
        case _ :
            return base_url,"custom"

def create_images(prompt:str, model:str, 
                  base_url:str|None = None,
                  api_key:str|None = None, 
                  n:int = 1, size:str = "1024x1024",
                  save_path:str|Path|None = None) :
    pass