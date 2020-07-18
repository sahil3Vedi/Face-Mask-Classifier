from django import forms
from . models import CCTV_Img


class CCTVImgForm(forms.ModelForm):

    class Meta:
        model = CCTV_Img
        fields = ['name', 'CCTV_Main_Img']
