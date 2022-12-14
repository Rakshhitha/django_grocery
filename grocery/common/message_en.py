INCORRECT_DATA = "Incorrect data were provided"
SOMETHING_WENT_WRONG = "Something went wrong"
INVALID_DATA = "Invalid data"
INVALID_CREDENTIAL = "Invalid credentials"
INVALID_FILE_TYPE = "Invalid file type"
INVALID_IMAGE_SIZE = "Invalid image size"
RATING_10_SUM_LIMIT = "Sum reached above 10"
DUPLICATE_RATING = "Rating already exist"
DUPLICATE_ASSET = "Asset already exist"

CLIENT_ID_REQUIRED = "Client id required"
PASSWORD_RESET_REQUEST = "Your request has taken. You will receive a link to reset the"
" password"
REQUIRED_NEW_PASSWORD = "Required new password"
INVALID_NEW_PASSWORD = "Invalid new password"
PASSWORD_LENGTH_VALIDATION = (
    "Password should be greater than 6 character and less than 16 character"
)
SAME_PASSWORD_VALIDATION = "New password should not be same as old password"

SUCCESS = "Success"
CREATED = "Created successfully"
UPDATED = "Updated successfully"
DELETED = "Deleted successfully"
FAILED = "Failed"
ALREADY_EXIST = "Data already exists"
DATA_FETCHED = "Data fetched successfully"
USER_LOGIN_SUCCESS = "User logged in successfully"
USER_LOGOUT_SUCCESS = "User logged out successfully"
REGISTRATION_SUCCESS = "Registration successful"
PASSWORD_RESET = "Password reset successfully"
TOKEN_FETCHED_SUCCESSFULLY = "Token fetched successfully"
PUBLISHED = "Published successfully"
OTP_NOT_MATCH = "Entered OTP didn't match"
OTP_SENT_SUCCESS = "OTP sent successfully and valid for 10 minutes"
OTP_SESSION_EXPIRED = "OTP has expired"
OTP_VERIFIED_SUCCESS = "OTP verified successfully"
EMAIL_REGISTERED = "Email already registered. Please pass different mail id"
MOBILE_REGISTERED = (
    "Mobile Number already registered. Please pass different mobile number "
)
EMAIL_VERIFICATION_SUCCESS = "Email verified successfully"
EMAIL_VERIFICATION_LINK_EXPIRED_INVALID = (
    "Email verification link either has expired or invalid token"
)
MOBILE_EMAIL_NOT_FOUND = "Neither mobile number nor email found"
PAYLOAD_INCORRECT = "Invalid Payload"
EMAIL_NOT_FOUND = "Email not found"


def requiredfield(field):
    return f"Required field - {field}"
