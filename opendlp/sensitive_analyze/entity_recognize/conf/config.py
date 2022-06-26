import os

# 资源文件路径
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SOURCE_ROOT = BASE_DIR + '/predefined_recognizer/rule_recognizer/resources/'
SOCIAL_CREDIT_CODE_FILE = SOURCE_ROOT+'social-credit-code.json'
POST_CODE_FILE = SOURCE_ROOT+'postcode-province.json'
TELEPHONE_CODE_FILE = SOURCE_ROOT+'telephone-code.json'
MOBILE_PHONE_FILE = SOURCE_ROOT+'mobile-phone-code.json'

# 每列最多取多少行数据进行识别
MAX_ROWS = 1000

# 内置支持识别的敏感数据类型
PERSON = 'PERSON'
COMPANY_NAME = 'COMPANY_NAME'
LOCATION = 'LOCATION'
ID_CARD = 'ID_CARD'
TELEPHONE = 'TELEPHONE'
MOBILE_PHONE = 'MOBILE_PHONE'
EMAIL = 'EMAIL'
LICENSE_PLATE = 'LICENSE_PLATE'
BANK_CARD = 'BANK_CARD'
PASSPORT = 'PASSPORT'
SOCIAL_CREDIT_CODE = 'SOCIAL_CREDIT_CODE'
POSTCODE = 'POSTCODE'
DATE = 'DATE'
IPV4 = 'IPV4'
IPV6 = 'IPV6'
MAC = 'MAC'
DOMAIN_NAME = 'DOMAIN_NAME'

OTHER = 'OTHER'


# 默认阈值
THRESHOLD_PREDEFINED = {
    PERSON: 0.8,
    COMPANY_NAME: 0.75,
    LOCATION: 0.8,
    ID_CARD: 0.8,
    TELEPHONE: 0.8,
    MOBILE_PHONE: 0.8,
    EMAIL: 0.8,
    LICENSE_PLATE: 0.8,
    BANK_CARD: 0.8,
    PASSPORT: 0.8,
    SOCIAL_CREDIT_CODE: 0.8,
    POSTCODE: 0.8,
    DATE: 0.8,
    IPV4: 0.8,
    IPV6: 0.8,
    MAC: 0.8,
    DOMAIN_NAME: 0.8
    }

THRESHOLD_USERDEFINED = 0.8