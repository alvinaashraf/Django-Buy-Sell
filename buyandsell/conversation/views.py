from django.shortcuts import render,get_object_or_404,redirect
from item.models import Item
from django.contrib.auth.decorators import login_required
from .models import Conversation
from .forms import ConversationMessageForm
# Create your views here.

@login_required
def newConversation(request,item_pk):
    item=get_object_or_404(Item,pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversation=Conversation.objects.filter(items=item).filter(members__in=[request.user.id])
    
    if conversation:
        return redirect('conversation:detail_inbox',pk=conversation.first().id)
    
    if request.method=='POST':
        form= ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation=Conversation.objects.create(items=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()
            
            return redirect('item:Detail',pk=item_pk)
        
    else:
        form=ConversationMessageForm()
        
    return render(request,'conversation/new.html',{'form':form})




@login_required
def inbox(request):
    conversation=Conversation.objects.filter(members__in=[request.user.id])
    
    return render(request,'conversation/inbox.html',{'conversation':conversation})
    
            
    
    
@login_required
def detail_inbox(request,pk):
    conversation=Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    
    if request.method == 'POST':
        form=ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()
            
            conversation.save()
            
            return redirect('conversation:detail_inbox',pk=pk)
        
    else:
        form=ConversationMessageForm()
    
    return render(request,'conversation/inbox_detail.html',{'conversation':conversation,'form':form})