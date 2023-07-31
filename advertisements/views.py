from django.shortcuts import render
from django.http import HttpResponse

def advertisement_list(requset, *args, **kwargs):
    return HttpResponse('<ul>'''
                            '<li>Мастер на час</li>'
                            '<li>Ремонт компьютера</li>'
                            '<li>Услуги сантехника</li>'
                        '</ul>')


def advertisement_detail(requset, *args, **kwargs):
    return HttpResponse('<ol>'''
                            '<li>Мастер на час</li>'
                            '<li>Ремонт компьютера</li>'
                            '<li>Услуги сантехника</li>'
                        '</ol>')