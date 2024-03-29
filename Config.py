import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "20651882"))
    API_HASH = os.environ.get("API_HASH", "b79a9d643e52554decdd8d34ae4fb158")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7161504979:AAFWG_NDUBZKbs8P-uy9aGshB3UDjx1JXDw")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQE7H2oAfhN6TvawYEP6-KbYD7GXQvX8SGtBcan6SD-hEJdqv1kX_3QGca3SvjWAJou0OS9v9KoPct91gqWk-kb0Zbepl_30BVvat9O51JDuh6_CxbJ8E22VQTINIQVmcxMmPxJa85U5K7raDovg3jeEAhwrSkv1Yv1YpOxM2ioruWeMrhT5Z0BYbfIs27EWT_TqoPf1ksvykjwDfvfbWrpmdvLAnuNKbR7SkTxE7tawsjTsYcBlEHmDxC1b0p_pBxFTErsfofIbc1hjCE-IBLm48IzaTkl8awlue0UYCWg18g1qbqRqHqA1Fee6wFXPlDUkBhkiv3skCaUTxqJIhTXDipE46wAAAAGr5ry2AA")
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
