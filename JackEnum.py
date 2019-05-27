from enum import Enum

class Token(Enum):
    tKEYWORD = 0
    tSYMBOL = 1
    tINTCONST = 2
    tSTRINGCONST = 3
    tIDENTIFIER = 4
    tUNKNOWN = 5

class Keyword(Enum):
    kCLASS = 0
    kMETHOD = 1
    kFUNCTION = 2
    kCONSTRUCTOR = 3
    kINT = 4
    kBOOLEAN = 5
    kCHAR = 6
    kVOID = 7
    kVAR = 8
    kSTATIC = 9
    kFIELD = 11
    kLET = 12
    kDO = 13
    kIF = 14
    kELSE = 15
    kWHILE = 16
    kRETURN = 17
    kTRUE = 18
    kFALSE = 19
    kNULL = 20
    kTHIS = 21
    kUNKNOWN = 22