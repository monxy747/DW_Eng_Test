from xmlrpc.client import boolean
from myapp.views import GetImageClassView
from django.test import TestCase
from unittest.mock import patch
from django.urls import reverse

# Create your tests here.
#リクエスト成功のテスト
class GetImageClassMockSuccessResponse:
    def __init__(self) -> None:
        self.status_code = 200

    def json(self):
        return {
            "data":[
                {
                    "success": True,
                    "message": "success",
                    "estimated_data":{
                        "class":3,
                        "confidence":0.8683
                    }
                }
            ]
        } 
            

class GetImageClassViewSuccessTest(TestCase):
    @patch("requests.post", return_value=GetImageClassMockSuccessResponse())
    def test_1(self, mocked):
        '''
        APIの成功レスポンスを正常に取得できること
        '''
        service = GetImageClassView(path = "/image/test.jpg")
        response_data = service.get()
        self.assertEqual(True, len(response_data)>0)
        self.assertEqual(
            True,
            response_data[0].get("success")
        )
        self.assertEqual(
            "success",
            response_data[0].get("message")
        )
        self.assertEqual(
            3,
            response_data[0].get("estimated_data").get("class")
        )
        self.assertEqual(
            0.8683,
            response_data[0].get("estimated_data").get("confidence")
        )

#リクエスト失敗のテスト
class GetImageClassMockFailureResponse:
    def __init__(self) -> None:
        self.status_code = 200

    def json(self):
        return {
            "data":[
                {
                    "success": False,
                    "message": "Error:E50012",
                    "estimated_data":{}
                }
            ]
        } 
            

class GetImageClassViewFailureTest(TestCase):
    @patch("requests.post", return_value=GetImageClassMockFailureResponse())
    def test_1(self, mocked):
        '''
        APIの失敗レスポンスを正常に取得できること
        '''
        service = GetImageClassView(path = "/image/test.jpg")
        response_data = service.get()
        self.assertEqual(True, len(response_data)>0)
        self.assertEqual(
            False,
            response_data[0].get("success")
        )
        self.assertEqual(
            "Error:E50012",
            response_data[0].get("message")
        )
        