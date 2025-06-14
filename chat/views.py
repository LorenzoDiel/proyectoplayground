from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from .forms import MessageForm

@login_required
def inbox(request):
    messages_received = Message.objects.filter(recipient=request.user).order_by('-sent_at')
    messages_sent = Message.objects.filter(sender=request.user).order_by('-sent_at')
    return render(request, 'chat/inbox.html', {
        'messages_received': messages_received,
        'messages_sent': messages_sent,
    })

@login_required
def send_message(request):
    initial = {}
    # Si viene ?para=id en la URL, preselecciona ese usuario
    para_id = request.GET.get('para')
    if para_id:
        from django.contrib.auth.models import User
        try:
            destinatario = User.objects.get(id=para_id)
            initial['recipient'] = destinatario
        except User.DoesNotExist:
            pass

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('chat-inbox')
    else:
        form = MessageForm(initial=initial)
        # No permite enviarte mensaje a vos mismo
        form.fields['recipient'].queryset = form.fields['recipient'].queryset.exclude(pk=request.user.pk)
    return render(request, 'chat/send_message.html', {'form': form})


@login_required
def view_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if message.recipient != request.user and message.sender != request.user:
        return redirect('chat-inbox')
    if message.recipient == request.user and not message.is_read:
        message.is_read = True
        message.save()
    return render(request, 'chat/view_message.html', {'message': message})
