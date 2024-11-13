from django.shortcuts import render, redirect
from django.http import JsonResponse


def home(request):
    # check if accessibility preference is set
    if 'accessibility_mode' not in request.session:
        return render(request, 'coffee_shop/accessibility_choice.html')
    return render(request, 'coffee_shop/home.html')

def set_accessibility(request):
    if request.method == 'POST':
        mode = request.POST.get('mode', 'false')
        request.session['accessibility_mode'] = mode == 'true'
        return redirect('home')
    return redirect('home')

def menu(request):
    coffee_menu = [
        {
            'name': 'Ethiopian Yirgacheffe',
            'description': 'Floral and bright with notes of bergamot and lime.',
            'price': '$4.50'
        },
        {
            'name': 'Colombian Supremo',
            'description': 'Sweet caramel notes with a nutty finish.',
            'price': '$4.00'
        },
        {
            'name': 'Sumatra Mandheling',
            'description': 'Full-bodied with earthy, spicy notes.',
            'price': '$4.75'
        },
    ]
    return render(request, 'coffee_shop/menu.html', {'coffees': coffee_menu})

def about(request):
    context = {
        'history': """
            Bean & Brew (Orion NerdX) was founded in 2024 by a group of passionate young and upcoming devs who took an interest in coffee and wanted to bring the best bean from around the world to their local community.
            Our mission is to source and roast the highest quality arabica coffee, and to share our love of coffee with everyone who walks through our doors. We believe that great coffee has the power to bring people together and create meaningful connections.
            Over the years, we've built a strong relationship with coffee growers and cooperatives, ensuring that we're paying fair prices and supporting sustainable farming practices. We're proud to offer a diverse selection of single-origin and blended coffees that showcase the unique flavors and terroirs of the world's premier coffee regions.
            At the heart of our business is a commitment to exceptional customer service. Our baristas are highly trained and passionate about coffee, and they're always happy to answer questions, make recommendations, and ensure that every cup is perfect.
            Whether you're stopping in for your morning brew, meeting a friend for an afternoon pick-me-up, or exploring our menu of specialty drinks and treats, we're excited to share our love of coffee with you.
        """,
        'values': [
            'Sourcing the finest quality beans',
            'Roasting with care and precision',
            'Providing exceptional customer service',
            'Supporting sustainable coffee farming',
            'Creating a welcoming, community-focused space'
        ]
    }
    return render(request, 'coffee_shop/about.html', context)

def contact(request):
    context = {
        'address': '123 Orion Street, Orion City, OR 97201',
        'phone': '(+233) 00-000-0000',
        'email': 'info@beanandbrew.com',
        'hours': {
            'Monday-Fridat': '7am - 8pm',
            'Saturdat-Sunday': '8am - 6pm'
        }
    }
    return render(request, 'coffee_shop/contact.html', context)