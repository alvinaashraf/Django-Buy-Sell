from django.shortcuts import render ,get_object_or_404,redirect
from .models import Item,Category
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm,EditItemForm
#search multiple fields 
from django.db.models import Q
# Create your views here.


def Detail(request,pk):
    item=get_object_or_404(Item,pk=pk)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:3]
    return render(request,'item/detail.html',{'item':item,'related_items':related_items})


@login_required
def newItem(request):
    form=NewItemForm(request.POST,request.FILES)
    if request.method=='POST':
        
        
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('item:Detail',pk=item.id)
        else:
            form=NewItemForm()
    
    return render(request,'item/form.html',{'form':form,'title':'New Item'})



@login_required
def delete(request,pk):
    item=get_object_or_404(Item, pk=pk, created_by=request.user )
    item.delete()
    
    return redirect('dashboard:dashboard')





@login_required
def editItem(request,pk):
    item=get_object_or_404(Item, pk=pk, created_by=request.user )
    form=EditItemForm(request.POST,request.FILES,instance=item)
    

    if request.method=='POST':
        

        
        
        if form.is_valid():
           
            form.save()
            return redirect('item:Detail',pk=item.id)
        else:
            form=EditItemForm(instance=item)
    
    return render(request,'item/form.html',{'form':form,'title':'Edit Item'})


def browse(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)
    if category_id:
        items = items.filter(category_id=category_id)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
            
            
    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })