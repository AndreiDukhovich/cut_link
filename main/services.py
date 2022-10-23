import qrcode
from random import choice
from string import ascii_letters
from .models import Users_link
from django.core.files import File

def create_qr_code(link, file_name):
    data = link
    filename = f"{file_name}.png"
    img = qrcode.make(data)
    img.save('static\\qr\\'+filename)
    return File(open('static\\qr\\'+filename, 'rb'))


def get_cut_link(request, link):
    cut_link = ''
    simbols = ascii_letters + '0123456789'
    cut_link_list = Users_link.objects.values_list('cut_link', flat=True)
    while True:
        for _ in range(6):
            cut_link += choice(simbols)
        if cut_link in cut_link_list:
            cut_link = ''
        else:
            break
    return 'http://' + request.get_host() + '/' + cut_link