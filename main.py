  
import bimpy as bp
from bimpy.utils import help_marker
import easygui
import requests
from discord import Webhook, RequestsWebhookAdapter
from PIL import Image
import io
import threading
def download_image(url):
    r = requests.get(url, timeout=4.0)
    if r.status_code != requests.codes.ok:
        assert False, 'Status code error: {}.'.format(r.status_code)
    data = io.BytesIO(r.content)
    return Image.open(data)
ctx = bp.Context()
ctx.init(600, 600, "[>] Webhook Spammer [-] pika ._.#1888 [<]")
bp.load_fonts(latin_ext=True,cyrillic=True)
im = bp.Image(download_image("https://media-exp1.licdn.com/dms/image/C560BAQF4M0IT6_BcsA/company-logo_200_200/0/1620918122423?e=2159024400&v=beta&t=bS2Zs3ue9dfCics0Y1vaBxJJUKQJa_TudRCBf9zNfMY"))
webhookurlsi=bp.String()
mesajsayisi=bp.Int()
mesaj=bp.String()
pfp=bp.String()
username=bp.String()
clicked=None
style = bp.get_style()
mesajerror=None
webhookurlsierror=None
webhookurlsierror1=None
webhookurlsierrors=None
mesajsayisi.value=1
file_name=None
spambitti=None
dosya=None
while not ctx.should_close():
    with ctx:
        bp.indent()
        bp.indent()
        bp.indent()
        bp.indent()
        bp.indent()
        bp.indent()
        bp.image(im)
        bp.separator()
        bp.unindent()
        bp.unindent()
        bp.unindent()
        bp.unindent()
        bp.unindent()
        bp.unindent()
        if bp.collapsing_header("Tek Webhook Spammer"):
            bp.separator()
            bp.input_text('Webhook URL', webhookurlsi, 121)
            if webhookurlsierror==True:
                bp.same_line()
                bp.text_colored(bp.Vec4(1.0,0.0,1.0,1.0),"Herhangi bir webhook urlsi belirtilmemiş!")
            if webhookurlsierror1==True:
                bp.same_line()
                bp.text_colored(bp.Vec4(1.0,0.0,1.0,1.0),"Lütfen geçerli bir webhook urlsi belirtiniz!")
            bp.separator()
            bp.input_text('Webhook İsmi', username, 2001)
            bp.same_line()
            bp.text_colored(bp.Vec4(1.0,1.0,0.0,1.0),"İsteğe Bağlı")
            bp.separator()
            bp.input_text("Webhook Profil Fotoğrafı (URL)", pfp,2001)
            bp.same_line()
            bp.text_colored(bp.Vec4(1.0,1.0,0.0,1.0),"İsteğe Bağlı")
            bp.separator()
            bp.input_text('Mesaj', mesaj, 2001)
            if mesajerror==True:
                bp.same_line()
                bp.text_colored(bp.Vec4(1.0,0.0,1.0,1.0),"Herhangi bir mesaj yazılmamış!")
            bp.separator()
            bp.slider_int("Mesaj Sayısı", mesajsayisi, 1, 500)
            bp.separator()
            bp.indent()
            bp.indent()
            bp.indent()
            bp.indent()
            bp.indent()
            bp.indent()
            bp.indent()
            bp.indent()
            if bp.button("Spamı Başlat"):
                spambitti=False
                if(mesaj.value==""):
                    mesajerror=True
                else:
                    mesajerror=False
                if(webhookurlsi.value==""):
                    webhookurlsierror=True
                else:
                    webhookurlsierror=False
                if(len(webhookurlsi.value)!=120):
                    webhookurlsierror1=True
                else:
                    webhookurlsierror1=False
                    if(mesajerror==False and webhookurlsierror==False and webhookurlsierror1==False):
                        webhookurl=webhookurlsi.value.split("/")
                        mesajsayisi1=0
                        mesajsayisi2=mesajsayisi.value
                        while int(mesajsayisi2)!=mesajsayisi1:
                            webhook = Webhook.partial(str(webhookurl[5]), webhookurl[6], adapter=RequestsWebhookAdapter())
                            webhook.send(mesaj.value, username=username.value,avatar_url=pfp.value)
                            mesajsayisi1+=1
                            mesajsayisi.value-=1
                            if mesajsayisi.value<=0:
                                spambitti=True
            if spambitti==True:
                bp.same_line()
                bp.text("Spam Bitti!")
            bp.unindent()
            bp.unindent()
            bp.unindent()
            bp.unindent()
            bp.unindent()
            bp.unindent()
            bp.unindent()
            bp.unindent()
        bp.separator()
        if bp.collapsing_header("Multi Webhook Spammer"):
            bp.separator()
            if bp.button("Webhookları aktar"):
                file_name=easygui.fileopenbox(title="Discord Webhook Spammer",msg="Lütfen Webhookları Seçiniz",default="./data/*.txt",multiple=False)
                if file_name==None:
                    webhookurlsierrors=True
                else:
                    webhookurlsierrors=False
            if webhookurlsierrors==True:
                bp.same_line()
                bp.text_colored(bp.Vec4(1.0,0.0,1.0,1.0),"Herhangi bir metin dosyası seçilmedi!")
            elif webhookurlsierrors==False:
                bp.same_line()
                bp.text_colored(bp.Vec4(1.0,1.0,0.0,1.0),"Dosya seçildi! ({})".format(file_name))
                dosya=open(file_name,"r")
            bp.separator()
            bp.input_text('Webhook İsmi', username, 2001)
            bp.same_line()
            bp.text_colored(bp.Vec4(1.0,1.0,0.0,1.0),"İsteğe Bağlı")
            bp.separator()
            bp.input_text("Webhook Profil Fotoğrafı (URL)", pfp,2001)
            bp.same_line()
            bp.text_colored(bp.Vec4(1.0,1.0,0.0,1.0),"İsteğe Bağlı")
            bp.separator()
            bp.input_text('Mesaj', mesaj, 2001)
            if mesajerror==True:
                bp.same_line()
                bp.text_colored(bp.Vec4(1.0,0.0,1.0,1.0),"Herhangi bir mesaj yazılmamış!")
            bp.separator()
            bp.slider_int("Mesaj Sayısı", mesajsayisi, 1, 500)
            bp.separator()
            bp.indent()
            bp.indent()
            bp.indent()
            bp.indent()
            bp.indent()
            bp.indent()
            bp.indent()
            bp.indent()
            if bp.button("Spamı Başlat"):
                spambitti=False
                if(mesaj.value==""):
                    mesajerror=True
                else:
                    mesajerror=False
                    if(mesajerror==False):
                        webhookurl=webhookurlsi.value.split("/")
                        def spam(self,webhookurl6):
                            mesajsayisi1=0
                            mesajsayisi2=mesajsayisi.value
                            while int(mesajsayisi2)!=mesajsayisi1:
                                webhook = Webhook.partial(str(webhookurl6[5]), webhookurl6[6], adapter=RequestsWebhookAdapter())
                                webhook.send(mesaj.value, username=username.value,avatar_url=pfp.value)
                                mesajsayisi1+=1
                                if mesajsayisi.value<=0:
                                    spambitti=True
                        for webhookurl5 in dosya:
                            webhookurl7=webhookurl5.replace("\n","")
                            webhookurl6=webhookurl7.split("/")
                            t1 = threading.Thread(target=spam, args = ("thread-1",webhookurl6))
                            t1.start()
                            if spambitti==True:
                                bp.same_line()
                                bp.text("Spam Bitti!")
                                mesajsayisi.value=1
            bp.unindent()
            bp.unindent()
            bp.unindent()
            bp.unindent()
            bp.unindent()
            bp.unindent()
            bp.unindent()
            bp.unindent()
        bp.separator()