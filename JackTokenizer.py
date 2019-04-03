import re
from enum import Enum

keywords = ['class','constructor','function','method','field','static','var',
            'char','boolean','void','true','false','null','this','let','do',
            'if','else','while','return']
            
symbols = ['\{', '\}', '\(', '\)', '\[', '\]', '\.', '\,', '\;', '\+', '\-',
           '\*', '\/', '\&', '\|', '\<', '\>', '\=', '\~']

intconst = r'[0-9]+'
stringconst = r'\".*\"'
identifier = r'[a-zA-Z]+'

tokens_combinados = "(%s|%s|%s|%s|%s)" %("|".join(keywords),"|".join(symbols),intconst,stringconst,identifier)

class Token(Enum):
    KEYWORD = 0
    SYMBOL = 1
    INTCONST = 2
    STRINGCONST = 3
    IDENTIFIER = 4

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
        tipo = None
        if(re.match("|".join(keywords),token)):
            tipo = "keyword"
        else:
            if(re.match("|".join(symbols),token)):
                tipo = "symbol"
            elif(re.match(intconst,token)):
                tipo = "intConst"
            elif(re.match(stringconst,token)):
                tipo = "stringConst"
            elif(re.match(identifier,token)):
                tipo = "identifier"
        return tipo

    def getToken(self):
        token = self.lista_tokens[self.tokenCorrente]
        if(self.tokenType() == "stringConst"):
            token = token[1:len(token)-1]
        return token

tknz = JackTokenizer('Main.jack')
tknz.advance()
print("<tokens>")
while(tknz.hasMoreTokens()):
    classeToken = tknz.tokenType()
    print("<%s>%s</%s>" %(classeToken,tknz.getToken(),classeToken))
    tknz.advance()
print("</tokens>")