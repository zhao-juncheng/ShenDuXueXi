'''
要是有不太懂得，可以再结合教材内容详细理解

凯撒密码
    主要规则：对于每一个英文字母，用在字母表中继该字母固定数目后的字母进行替换
    例如，固定数目为3， ABC->DEF
字符串和字符列表之间的转换：
    字符串转换成字符列表：
    在python中，一个字符串如 'bird' ，将其作为参数调用 list('bird')-->['b','i','r','d']
    字符列表转换成字符串：
    例如：对于一个字符列表['b','i','r','d']，通过空字符串 '' 将一个字符列表作为参数调用 .join(['b','i','r','d'])
        ''.join(['b','i','r','d'])-->'bird'
代码实现细节
    1 将26个英文字母作为参照表编码加密表
        使用算术式 (i+r) mod 26来实现，i代表该字母的码，+r代表用在字母表中继该字母 r 个数目之后的字母，用于加密替换
      确定规则数目后得到的相对应的一个字母表，作为解密表，
        使用算术式 (i-r) mod 26来实现，i代表该字母的码，-r代表用在字母表中继该字母 r 个数目之前的字母，用于解密替换

    2 对于一个待加密字符串，其每一个字母去加密表中得到其对应的加密后的字母
      对于一个带解密字符串，其每一个字母去解密表中得到其对应的解密后的字母

'''
class CaesarCipher:
    def __init__(self,shift):
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            # 用于得到 26 字母对应的加密表，用 shift 来确定加密格式。
            # 例如：shift = 3 ，则加密表为['D','E','F',...,'A','B','C']。解密表则相反
            # chr(int数值)，用于得到该数值在Unicode所对应的字符
            # ord(字符)，用于得到该字符在Unicode所对应的数值，方便于计算
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self,message):
        return self._transform(message,self._forward)

    def decrypt(self,secret):
        return self._transform(secret,self._backward)

    def _transform(self,original,code):
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k])-ord('A')
                msg[k] = code[j]
        return ''.join(msg)

if __name__ == '__main__':
    cipher = CaesarCipher(3)
    message = "THE EAGLE IS IN PLAY; MEET AT JOE'S."
    coded = cipher.encrypt(message)
    print('Secret: ',coded)
    answer = cipher.decrypt(coded)
    print('Message: ',answer)
