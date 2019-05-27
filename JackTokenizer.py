# Tokenizer da linguagem Jack

import re
from JackEnum import *

keywords = ['int','class','constructor','function','method','field','static','var',
            'char','boolean','void','true','false','null','this','let','do', 'if',
            'else','while','return']
            
symbols = ['\{', '\}', '\(', '\)', '\[', '\]', '\.', '\,', '\;', '\+', '\-', '\*',
           '\/', '\&', '\|', '\<', '\>', '\=', '\~']

intconst = r'[0-9]+'
stringconst = r'\".*\"'
identifier = r'[a-zA-Z][a-zA-Z0-9_]*'

tokens_combinados = "(%s|%s|%s|%s|%s)" %("|".join(keywords),"|".join(symbols),intconst,stringconst,identifier)

def removerComentarios(codigo):
    codigo = re.sub('(?m)\s*//.+$','',codigo)
    codigo = re.sub('(?ms)/\*.*?\*/','',codigo)
    return codigo

class JackTokenizer():

    def __init__(self, arquivo):
        self.arquivo = open(arquivo, 'r')
        self.tokenCorrente = None
        codigo = self.arquivo.read().strip()
        codigo = removerComentarios(codigo)
        reg = re.compile(tokens_combinados)
        self.lista_tokens = re.findall(reg, codigo)
        self.indice_tokens = len(self.lista_tokens)
        
    def hasMoreTokens(self):
        if(self.tokenCorrente == self.indice_tokens):
            x = False
        else:
            x = True
        return x

    def advance(self):
        if(self.hasMoreTokens()):
            if(self.tokenCorrente == None):
                self.tokenCorrente = 0
            else:
                self.tokenCorrente += 1

    def tokenType(self):
        token = self.lista_tokens[self.tokenCorrente]
        if(re.match("|".join(keywords),token)):
            return Token.tKEYWORD
        else:
            if(re.match("|".join(symbols),token)):
                return Token.tSYMBOL
            elif(re.match(intconst,token)):
                return Token.tINTCONST
            elif(re.match(stringconst,token)):
                return Token.tSTRINGCONST
            elif(re.match(identifier,token)):
                return Token.tIDENTIFIER

    def getToken(self):
        token = self.lista_tokens[self.tokenCorrente]
        if(self.tokenType() == Token.tSTRINGCONST):
            token = token[1:len(token)-1]
        return token

    def keyword(self):
        token = self.getToken()
        if(token == "class"):
            return Keyword.kCLASS
        if(token == "method"):
            return Keyword.kMETHOD
        if(token == "function"):
            return Keyword.kFUNCTION
        if(token == "constructor"):
            return Keyword.kCONSTRUCTOR
        if(token == "int"):
            return Keyword.kINT
        if(token == "boolean"):
            return Keyword.kBOOLEAN
        if(token == "char"):
            return Keyword.kCHAR
        if(token == "void"):
            return Keyword.kVOID
        if(token == "var"):
            return Keyword.kVAR
        if(token == "static"):
            return Keyword.kSTATIC
        if(token == "field"):
            return Keyword.kFIELD
        if(token == "let"):
            return Keyword.kLET
        if(token == "do"):
            return Keyword.kDO
        if(token == "if"):
            return Keyword.kIF
        if(token == "else"):
            return Keyword.kELSE
        if(token == "while"):
            return Keyword.kWHILE
        if(token == "return"):
            return Keyword.kRETURN
        if(token == "true"):
            return Keyword.kTRUE
        if(token == "while"):
            return Keyword.kWHILE
        if(token == "return"):
            return Keyword.kRETURN
        if(token == "false"):
            return Keyword.kFALSE
        if(token == "null"):
            return Keyword.kNULL
        return Keyword.kTHIS

    def tagToken(self):
        tokenTag = self.getToken()
        tag = None
        if(self.tokenType() == Token.tKEYWORD):
            tag = "<keyword>" + tokenTag + "</keyword>"
        if(self.tokenType() == Token.tIDENTIFIER):
            tag = "<identifier>" + tokenTag + "</identifier>"
        if(self.tokenType() == Token.tINTCONST):
            tag = "<integerConstant>" + tokenTag + "</integerConstant>"
        if(self.tokenType() == Token.tSTRINGCONST):
            tag = "<stringConstant>" + tokenTag + "</stringConstant>"
        if(self.tokenType() == Token.tSYMBOL):
            if(tokenTag == '<'):
                tag = "<symbol>&lt</symbol>"
            elif(tokenTag == '>'):
                tag = "<symbol>&gt</symbol>"
            elif(tokenTag == '\"'):
                tag = "<symbol>&quot</symbol>"
            elif(tokenTag == '&'):
                tag = "<symbol>&amp</symbol>"
            else:
                tag = "<symbol>" +tokenTag + "</symbol>"
        return tag