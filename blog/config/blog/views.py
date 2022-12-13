from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

# def home(request):
#     return HttpResponse('Hi Django')

def info(request):
    return HttpResponse('<b>Information</b>')

def api(requests):

    data = {
            '1': {
                "title": "مقاله اول",
                "slug": "first-article",
                "description": "this is good article",

        },
             '2': {
                "title": "مقاله اول",
                "slug": "second-article",
                "description": "this is good article",

        },
            '3': {
                "title": "مقاله اول",
                "slug": "third-article",
                "description": "this is good article",

        },
    }



    return JsonResponse(data)

def blog(request):
    context = {
        "articles": [
            {
                "title":"ایلان ماسک در توییتر از مدیران اسپیس ایکس، تسلا و بورینگ کمپانی کمک می‌گیرد",
                "description":"سال ۲۰۲۲ آنقدرها که تصور می‌کردیم پر بار نبود. تاخیر بسیاری از بازی‌های بزرگ و موکول شدن انتشارشان به سال ۲۰۲۳ و از طرفی غیبت برخی از فرنچایزهای بزرگ باعث شد تا امسال خیلی هم خاطره‌انگیز تلقی نشود.",
                "image": "https://digiato.com/wp-content/uploads/2022/12/Musk-910x600.jpg",
            },
            {
                "title":"۱۰ سریال ترسناک برتر سال ۲۰۲۲ که باید دید",
                "description":"طبق اسناد فاش شده، ماسک از حدود 50 مهندس تسلا، چند مدیر اسپیس ایکس و سه کارمند بلندپایه بورینگ کمپانی دعوت کرده است.",
                "image": "https://rooziato.com/wp-content/uploads/2022/12/Guillermo-Del-Toros-Cabinet-of-Curiosities-Episodes-Ranked-Feature-1024x512.jpg",
            },
            {
                "title":"۱۰ سریال ترسناک برتر سال ۲۰۲۲ که باید دید",
                "description":"طبق اسناد فاش شده، ماسک از حدود 50 مهندس تسلا، چند مدیر اسپیس ایکس و سه کارمند بلندپایه بورینگ کمپانی دعوت کرده است.",
                "image": "https://rooziato.com/wp-content/uploads/2022/12/Guillermo-Del-Toros-Cabinet-of-Curiosities-Episodes-Ranked-Feature-1024x512.jpg",
            },
        ]
    }
    return render(request, 'blog/home.html', context)