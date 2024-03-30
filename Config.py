import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "20651882"))
    API_HASH = os.environ.get("API_HASH", "b79a9d643e52554decdd8d34ae4fb158")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7161504979:AAFWG_NDUBZKbs8P-uy9aGshB3UDjx1JXDw")
    STRING_SESSION = os.environ.get("1BVtsOL8Buy9Sko67baHXVUFNvEiKx8XDbhIUCbMe3JmmfXDnDmozLvWc0RePl4hN4DrKxr8PzGLeurc774Pq7AMcA_jj05yfbL7ucp2Oc0myli5d-uYUyTR9iPyIlekpJwtWc90ooXGYWvEzW6JO4H3qZLNDs_1xe8hH0zknXDTXfFhgbGyP5rR_rqWYAeSof3vXM8IgopWvq7CtQtIwTRCTQ_ZYVlMAHt3FDlKG7xhGKtA9F2U7AFJqa2g7vvQEhV05ZDMcGA68gUHBH_7xoiHIGeDv3cglVKf_MMAEJe4mINER6K2EU3Ko8nYIbCHlk_gL3ELI258K4_PxbBzSjbWfxLaQH1o=", "")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
