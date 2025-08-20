from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddForm
from .models import Contact
from django.http import HttpResponseRedirect
from .forms import ContactForm

def show(request):
    """ 
    This function gets all the members in your Database through your Model
    Any further usage please refer to: https://docs.djangoproject.com/el/1.10/ref/models/querysets/
    """
    contact_list = Contact.objects.all()
    return render(request, 'mycontacts/show.html',{'contacts': contact_list})
    
def add(request):
    """ This function is called to add one contact member to your contact list in your Database """
    if request.method == 'POST':
        
        django_form = AddForm(request.POST)
        if django_form.is_valid():
           
            """ Assign data in Django Form to local variables """
            new_member_name = django_form.data.get("name")
            new_member_relation = django_form.data.get("relation")
            new_member_phone = django_form.data.get('phone')
            new_member_email = django_form.data.get('email')
            
            """ This is how your model connects to database and create a new member """
            Contact.objects.create(
                name =  new_member_name, 
                relation = new_member_relation,
                phone = new_member_phone,
                email = new_member_email, 
                )
                 
            contact_list = Contact.objects.all()
            return render(request, 'mycontacts/show.html',{'contacts': contact_list})    
        
        else:
            """ redirect to the same page if django_form goes wrong """
            return render(request, 'mycontacts/add.html')
    else:
        return render(request, 'mycontacts/add.html')


def edit_contact(request, pk):
    """ Edita um contato existente """
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact.name = form.cleaned_data['name']
            contact.relation = form.cleaned_data['relation']
            contact.phone = form.cleaned_data['phone']
            contact.email = form.cleaned_data['email']
            contact.save()
            return redirect('/')
    else:
        # Preenche os valores iniciais
        form = ContactForm(initial={
            'name': contact.name,
            'relation': contact.relation,
            'phone': contact.phone,
            'email': contact.email,
        })

    return render(request, 'mycontacts/edit.html', {'form': form, 'contact': contact})


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    
    if request.method == 'POST':
        contact.delete()
        return redirect('show')  # nome da URL que lista os contatos
    
    return redirect('show')