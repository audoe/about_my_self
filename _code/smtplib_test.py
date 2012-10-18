#coding:utf8
from email.Utils import COMMASPACE
from email import Charset
from email.MIMENonMultipart import MIMENonMultipart
from email.MIMEMultipart import MIMEMultipart
from email.Header import Header
import smtplib

UTF8 = Charset.Charset('utf-8')
class UTF8MIMEText(MIMENonMultipart):
    def __init__(self, _text, _subtype='plain'):
        MIMENonMultipart.__init__(self, 'text', _subtype, charset='utf-8')
        self.set_payload(_text, UTF8)


def gen_msg(email, name, to_list, subject, data):
    msg = MIMEMultipart()
    msg['Subject'] = Header(u'件粉红色的风景'.encode('utf8'), 'utf-8')
    msg['From'] = '%s\r'%email
    msg['To'] = '%s\n' % COMMASPACE.join(to_list)
    body = UTF8MIMEText(data)
    msg.attach(body)
    return msg


if __name__ == "__main__":
    data = u'开房间第三方的手机分解速度放缓的风景反击得手发抖'
    subject = u'将发挥第三方的房贷收紧房贷负担'
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-a", "--host", dest="host",
                              help="smtp adderss")
    parser.add_option("-p", "--port",
                               dest="port",
                                                help="port of smtp server")
    parser.add_option("-u", "--username", dest="username", help="you username")
    parser.add_option("-w", "--password", dest="password", help="password")
    (options, args) = parser.parse_args()
    args1 = ['whchen@qq.com','645921567@qq.com']
    body = gen_msg('whchen@qq.com', 'whchen', args1, subject, data)
    smtp = smtplib.SMTP(options.host, options.port)
    smtp.login(options.username, options.password)
    smtp.sendmail('whchen@qq.com', args1, body.as_string())
    smtp.quit()
