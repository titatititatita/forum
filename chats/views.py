from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from .models import Thread


def index(request):
    thread_list = Thread.objects.filter(reply__isnull=True)
    template = loader.get_template('chats/index.html')
    context = {
        'thread_list': thread_list,
    }
    return HttpResponse(template.render(context, request))


def show_thread(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    reply_list = Thread.objects.filter(reply=thread_id)
    return render(request, 'chats/thread.html', {'thread': thread, 'reply_list': reply_list})


def create_thread(request):
    t = Thread(text=request.POST['text'])
    t.save()
    return HttpResponseRedirect(reverse('chats:show_thread', args=(t.id,)))


def create_reply(request, thread_id):
    t = Thread(text=request.POST['text'], reply_id=thread_id)
    t.save()
    return HttpResponseRedirect(reverse('chats:show_thread', args=(thread_id,)))
