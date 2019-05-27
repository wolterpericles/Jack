# Teste de JackTokenizer

from JackTokenizer import JackTokenizer

tknz = JackTokenizer('Main.jack')
tknz.advance()
print("<tokens>")
while(tknz.hasMoreTokens()):
    classeToken = tknz.tagToken()
    print(classeToken)
    tknz.advance()
print("</tokens>")