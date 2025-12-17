from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not name or not email or not message:
            messages.error(request, 'All fields are required.')
            return redirect('contact')

        send_mail(
            f'Contact Form Submission from {name}',
            message,
            email,
            ['admin@example.com'],
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def account(request):
    return render(request, 'account.html')

def asset_management(request):
    return render(request, 'asset_management.html')

def buying(request):
    return render(request, 'buying.html')

def crm(request):
    return render(request, 'crm.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def hrms(request):
    return render(request, 'hrms.html')

def manufacturing(request):
    return render(request, 'manufacturing.html')

def projects(request):
    return render(request, 'projects.html')

def reports(request):
    return render(request, 'reports.html')

def selling(request):
    return render(request, 'selling.html')

def stock(request):
    return render(request, 'stock.html')

def support(request):
    return render(request, 'support.html')

def schedule_demo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company = request.POST.get('company')
        industry = request.POST.get('industry')
        requirements = request.POST.get('requirements')

        if not all([name, email, phone, company, industry, requirements]):
            return JsonResponse({'status': 'error', 'message': 'All fields are required.'}, status=400)

        try:
            send_mail(
                f'New Demo Request from {name}',
                f'Name: {name}\nEmail: {email}\nPhone: {phone}\nCompany: {company}\nIndustry: {industry}\n\nRequirements:\n{requirements}',
                email,
                ['hello@nivasync.com'],
            )
            return JsonResponse({'status': 'success', 'message': 'Your demo request has been submitted successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'An error occurred while sending the email.'}, status=500)

    return render(request, 'schedule_demo.html')
