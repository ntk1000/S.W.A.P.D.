# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from ums.forms import DemoUserForm
from ums.models import DemoUser

def demouser_edit(request):
	demouser = DemoUser()

	form = DemoUserForm(request.POST, instance=demouser)

	if form.is_valid():
		demouser = form.save(commit=True)
		demouser.save()
		return redirect('ums:demouser_commit',demouser.id)

	return render_to_response('ums/demouser_edit.html',dict(form=form),context_instance=RequestContext(request))

def demouser_commit(request, demouser_id):
	demouser = get_object_or_404(DemoUser, pk=demouser_id)

	if request.method == 'POST':
		form = DemoUserForm(request.POST, instance=demouser)
		if form.is_valid():
			demouser = form.save(commit=True)
			demouser.save()
			return redirect('ums:demouser_fin',demouser.id)
	else:
		form = DemoUserForm(instance=demouser)

	return render_to_response('ums/demouser_commit.html',dict(form=form,demouser_id=demouser_id),context_instance=RequestContext(request))

def demouser_fin(request, demouser_id):
	demouser = get_object_or_404(DemoUser, pk=demouser_id)
	return render_to_response('ums/demouser_fin.html',{'demouser': demouser},context_instance=RequestContext(request))