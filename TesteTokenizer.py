from JackTokenizer import JackTokenizer

tknz = JackTokenizer('Main.jack')
tknz.advance()
print("<tokens>")
while(tknz.hasMoreTokens()):
    classeToken = tknz.tokenType()
    print("<%s>%s</%s>" %(classeToken,tknz.getToken(),classeToken))
    tknz.advance()
print("</tokens>")