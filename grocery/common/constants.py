IMAGE_TYPES = ["image/bmp", "image/gif", "image/vnd.microsoft.icon",
               "image/jpeg", "image/png", "image/svg+xml", "image/tiff",
               "image/webp"]
MAX_IMAGE_SIZE = 5

MAX_360_IMAGE_SIZE = 50

TMP_PATH = 'tmp'

EMAIL_REGEX = r"^([\w\.\+\-]+\@[a-zA-Z0-9\.\_]+\.[a-zA-z]{2,4})$"

MOBILE_REGEX = r"@[a-zA-Z0-9\.\_]"

#USER_REGEX = r"^[a-zA-Z0-9_.-]+$"
USERNAME_REGEX = r"^[a-zA-Z0-9_.-]+$" # r"^(?=.{4,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$"

MOBILE_REGEX = r"^[\d]{10}$"

RATING_RANGE = list(range(1, 11))