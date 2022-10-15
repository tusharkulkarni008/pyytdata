import os
import json

from matplotlib.font_manager import json_load 
from apiclient.discovery import build

from .info import Info


class VideoQuerier(Info):

    def __init__(
            self,
            keyword: str,
            maxLen: int,
            order: str = "relevance",
            video_type: str = "video",
            video_category_id: int = 27,
            video_id: str = None,
    ):
        super().__init__(order="relevance", type="video")
        self.keyword = keyword
        self.maxLen = maxLen
        self.order = order
        self.type = video_type
        self.video_id = video_id
        self.video_category_id = video_category_id
        self.result = self.fetch()

    def fetch(self):
        req = self.query_youtube()
        if self.id not in json_load("api_json.json").keys():
            req.execute()
        else:
            cache = self.make_JSON()
        return req.execute()

    def get_result(self):
        return self.result

    def query_youtube(self):
        if self.keyword:
            req = self.youtube.search().list(
                q=self.keyword,
                part="snippet",
                maxResults=self.maxLen,
                type=self.type,
                order=self.order,
                videoCategoryId=self.video_category_id,
            )
        else:
            req = self.youtube.videos().list(part="snippet", id=self.id)

        self.result = req.execute()
    
    def make_JSON(self,):
        if os.path.exists("api_json.json") == False:
            with open("api_json.json" ,"a"):
                print("json created successfully")
        else:
            print("json already exists")
        f = json.load("api_json.json")
        api_dict ={}
        api_dict.update({self.id:self.result})
        json.dumps(api_dict)
        return f"cache updated  with{self.id}" 

    def get_result(self):
        return self.result


class VideoCommentQuerier:
    def __init__(self, idVideoComment):
        try:
            self.__API_KEY = os.environ.get(
                "API_KEY"
            )  # link to get the api key is in readme file
        except Exception:
            raise TypeError("You must have API_KEY set as an environment variable")
        youtube = build("youtube", "v3", developerKey=self.__API_KEY)
        self.youtube = youtube
        self.__id = idVideoComment

        request = youtube.commentThreads().list(part="snippet", videoId=self.__id)
        self.result = request.execute()

    def get_result(self):
        return self.result
