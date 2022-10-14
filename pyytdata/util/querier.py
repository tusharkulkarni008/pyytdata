import os
import json 
from apiclient.discovery import build

from .info import Info


class VidQuerier(Info):
    def __init__(
        self,
        keyword: str,
        maxlen: int,
        order: str = "relevance",
        type: str = "video",
        videoCategoryId: int = 27,
        id: int = None,
    ):
        self.keyword = keyword
        self.maxlen = maxlen
        self.order = order
        self.type = type
        self.id = id
        super().__init__(order="relevance", type="video")
        if keyword:
            req = self.youtube.search().list(
                q=self.keyword,
                part="snippet",
                maxResults=self.maxlen,
                type=self.type,
                order=self.order,
                videoCategoryId=videoCategoryId,
            )
        else:
            req = self.youtube.videos().list(part="snippet", id=self.id)
        if os.path.exists(API_Cache.json) == False:
            with open(API_Cache.json, "rw") as f:
                print("API Cache created successfully")
                api_data = json.load(f)
                if self.id not in api_data.keys():
                    self.result = req.execute()
                    api_data.update({self.id , self.result})
                else:
                    self.result = api_data{self.id}
       
        

    def get_result(self):
        return self.result


class VidCmntQuerier:
    def __init__(self, id):
        try:
            self.__API_KEY = os.environ.get(
                "API_KEY"
            )  # link to get the api key is in readme file
        except Exception:
            raise TypeError("You must have API_KEY set as an environment variable")
        youtube = build("youtube", "v3", developerKey=self.__API_KEY)
        self.youtube = youtube
        self.__id = id

        request = youtube.commentThreads().list(part="snippet", videoId=self.__id)
        self.result = request.execute()

    def get_result(self):
        return self.result
