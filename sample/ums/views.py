# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from ums.forms import DemoUserForm
from ums.models import DemoUser

def demouser_list(request):
    demousers = DemoUser.objects.all().order_by('id')
    return render_to_response('ums/demouser_list.html',{'demousers': demousers},context_instance=RequestContext(request))

def demouser_edit(request, demouser_id=None):
    if demouser_id: # 修正
        demouser = get_object_or_404(DemoUser, pk=demouser_id)
    else: # 追加
        demouser = DemoUser()

    if request.method == 'POST':
        form = DemoUserForm(request.POST, instance=demouser)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            demouser = form.save(commit=False)
            demouser.save()
            return redirect('ums:demouser_list')
    else:    # GET の時
        form = DemoUserForm(instance=demouser)  # インスタンスからフォームを作成

    return render_to_response('ums/demouser_edit.html',
                              dict(form=form, demouser_id=demouser_id),
                              context_instance=RequestContext(request))

def demouser_del(request, demouser_id):
    demouser = get_object_or_404(DemoUser, pk=demouser_id)
    demouser.delete()
    return redirect('ums:demouser_list')