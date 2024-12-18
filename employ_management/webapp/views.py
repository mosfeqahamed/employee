from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateRecordForm
from .models import Record
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
'''def home(request):
    return render(request, 'dashboard.html')
'''

def dashboard(request):
    # Get search fields
    name = request.GET.get('Name', '')
    dob = request.GET.get('DateOfBirth', '')
    email = request.GET.get('Email', '')
    mobile = request.GET.get('Mobile', '')

    # Get sorting parameters
    sort_by = request.GET.get('sort_by', 'full_name')  # Default sorting by full name
    order = request.GET.get('order', 'asc')  # Default to ascending order

    # Filtering query
    query = Q()
    if name:
        query &= Q(full_name__icontains=name)
    if dob:
        query &= Q(date_of_birth=dob)
    if email:
        query &= Q(email__icontains=email)
    if mobile:
        query &= Q(mobile__icontains=mobile)

    # Sorting logic
    if order == 'asc':
        records_list = Record.objects.filter(query).order_by(sort_by)
    else:
        records_list = Record.objects.filter(query).order_by(f'-{sort_by}')

    # Pagination
    paginator = Paginator(records_list, 5)  # Show 5 records per page
    page_number = request.GET.get('page')
    records = paginator.get_page(page_number)

    return render(request, 'dashboard.html', {
        'records': records,
        'sort_by': sort_by,
        'order': order
    })



def create_record(request):
    
    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'create-record.html', context=context)


def delete_record(request, pk):
    record = get_object_or_404(Record, pk=pk)

    if request.method == 'POST':
        record.delete()
        messages.success(request, f'Record for {record.full_name} has been deleted.')
        return redirect('dashboard')  # Redirect to the dashboard after deletion



def update_record(request, pk):
    record = get_object_or_404(Record, pk=pk)

    if request.method == 'POST':
        form = CreateRecordForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard or any other page after saving
    else:
        form = CreateRecordForm(instance=record)

    return render(request, 'update_record.html', {'form': form, 'record': record})