
# System libraries & Helper Functions
from pprint import pformat

# PythonSDK
from PythonSDK.facepp import API,File

# Image Processing Class
import PythonSDK.ImagePro

# 以下四项是dmeo中用到的图片资源，可根据需要替换
detech_img_url = 'http://bj-mc-prod-asset.oss-cn-beijing.aliyuncs.com/mc-official/images/face/demo-pic11.jpg'
faceSet_img = './imgResource/demo.jpeg'       # 用于创建faceSet
face_search_img = './imgResource/search.png'  # 用于人脸搜索
segment_img = './imgResource/segment.jpg'     # 用于人体抠像
merge_img = './imgResource/merge.jpg'         # 用于人脸融合
wrinkles = './imgResource/wrinkles.jpg'
zombie = './imgResource/zombie.jpg'
zombie_2 = './imgResource/zombie_2.jpg'
baby = './imgResource/baby.jpg'
donald_trump = './imgResource/Donald Trump.jpg'
snoop = './imgResource/Snoop.jpg'
santa = './imgResource/santa.jpg'

luke_bowsher = './KnightbookScraping/Grade-12/Male/Luke Bowsher_male_Grade-12.png'
matt_phua = './KnightbookScraping/Grade-12/Male/Matthew Phua_male_Grade-12.png'
abby_doll = './KnightbookScraping/Grade-12/Female/Abigail Doll_female_Grade-12.png'
neha_tarkad = './KnightbookScraping/Grade-12/Female/Neha Tarakad Juneja_female_Grade-12.png'
max_dostart = './KnightbookScraping/Grade-12/Male/Max Dostart-Meers Dostart Meers_male_Grade-12.png'
paras_arora = './KnightbookScraping/Grade-12/Male/Paras Arora_male_Grade-12.png'
joseph_ma = './KnightbookScraping/Grade-12/Male/Joseph Ma Chou_male_Grade-12.png'

#此方法专用来打印api返回的信息
def print_result(hit, result):
    print(hit)
    print('\n'.join("  " + i for i in pformat(result, width=75).split('\n')))

def printFuctionTitle(title):
    return "\n"+"-"*60+title+"-"*60;

# 初始化对象，进行api的调用工作
api = API()

#人脸融合：https://console.faceplusplus.com.cn/documents/20813963
#template_rectangle参数中的数据要通过人脸检测api来获取
mergeFace_res = api.mergeface(template_file=File(matt_phua), merge_file=File(santa))
print_result("mergeFace", mergeFace_res)

# Start Fusion 
PythonSDK.ImagePro.ImageProCls.getMergeImg(mergeFace_res["result"])
