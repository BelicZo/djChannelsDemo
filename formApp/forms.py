# -*- coding: utf-8 -*-
# __author__ = "belic"
# __datetime__ = "2018/5/27 11:08"
from django import forms
from django.contrib.auth.models import User
from django.core import validators
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.hashers import make_password


class FormAppTestForm(forms.Form):
    mobile_validator = validators.RegexValidator(r'^[1][3,4,5,6,7,8,9][0-9]{9}$', message="手机号格式错误")  # 手机号验证
    username = forms.CharField(min_length=10, max_length=32, validators=[UnicodeUsernameValidator()], error_messages={
        'unique': "用户名已经存在",
        'required': "请输入用户名",  # 默认都是True
        "min_length": "用户名至少10个字符",
        "max_length": "用户名最多32个字符"
    })
    password = forms.CharField(min_length=6, max_length=32, widget=forms.PasswordInput)
    email = forms.EmailField()
    mobile = forms.CharField(required=False, validators=[mobile_validator], label="手机号", label_suffix="==>")  # 用django-bootstrap label_suffix无用

    def clean_password(self):
        password = self.cleaned_data.get('password')
        try:
            validators.RegexValidator(r'^\d+$', message="密码不能全为数字", inverse_match=True)(password)
        except validators.ValidationError as e:
            self.add_error('password', e)
        return password

    def clean(self):
        cleaned_data = super(FormAppTestForm, self).clean()

        username = cleaned_data["username"]
        try:
            # UnicodeUsernameValidator()(username)  # r'^[\w.@+-]+$'
            UnicodeUsernameValidator(regex=r'^[a-zA-Z]\w+$')(username)  # 字母开头
        except forms.ValidationError as e:
            raise self.add_error('username', "用户名格式不正确")

        password = cleaned_data["password"]
        cleaned_data["password"] = make_password(password)  # 密码加密
        return cleaned_data
