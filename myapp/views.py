from cgitb import html
from django.shortcuts import render
import requests
import time
from . import models
from importlib.resources import path
# Create your views here.


def index(request):
    return render(request,'myapp/index.html')

'''
def move_to_result(request):
    return render(request,'myapp/result.html')
'''


class GetImageClassView:
    def __init__(self,path) -> None:
        self.image_path = path
    
    
    def get(self):
        
        response = requests.post(
            url = "http://example.com/",
            payload=self.image_path
        )
        
        return response.json().get("data",[])

def regist(request):
    
    #image_pathは一旦決め打ちで変数に登録。画面のformで入力してもらうなど?
    path = "/image/test.jpg"

    #api叩いてレスポンスを受け取る。timestampを生成(UNIX時間)
    get_image_class = GetImageClassView(path)
    req_timestamp = int(time.time())
    response_data = get_image_class.get()
    res_timestamp = int(time.time())
    
    #リクエストの成功と失敗で分岐
    result = response_data[0].get("success")

    #リクエスト成功
    if result:
        image_path = path
        success = str(result)
        message = response_data[0].get("message")
        classes = response_data[0].get("estimated_data").get("class")
        confidence = response_data[0].get("estimated_data").get("confidence")
        request_timestamp = req_timestamp
        response_timestamp = res_timestamp

        ai_analysis_log = models.AIAnalysisLog(image_path=image_path, success=success, message=message, 
                                                classes=classes, confidence=confidence, request_timestamp=request_timestamp, response_timestamp=response_timestamp)
        ai_analysis_log.save()

    #リクエスト失敗
    else:
        image_path = path
        success = str(result)
        message = response_data[0].get("message")

        ai_analysis_log = models.AIAnalysisLog(image_path=image_path, success=success, message=message)
        ai_analysis_log.save()


