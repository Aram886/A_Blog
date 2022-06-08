from urllib import request
from django.shortcuts import render

def index(request):
    d = [
        {
            "name": "Aram Hovhannisyan",
            "image": "guestt.jpg",
            "description":"Lorem ipsum, dolor sit amet consectetur adipisicing elit. Assumenda sint explicabo corporis"
                            "totam cupiditate nam harum distinctio    repudiandae possimus vitae, numquam tempore!"
                            "Eveniet ipsa nostrum dolores iste tempora, deserunt recusandae sequi dignissimos porro quaerat,"
                            "repellat amet, perspiciatis ut laudantium! ebitis iste molestiae excepturi aut quia minima.",
            "desc": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet exercitationem distinctio soluta nisi doloribus,"
                        "odio quia molestias quam praesentium fuga aliquid laudantium sequi saepe repellat. Labore ducimus laudantium totam ratione?"
                        "Distinctio facilis vel ipsa consequuntur enim asperiores repellendus voluptas nulla tempora mollitia perspiciatis"
                        "eos quasi consectetur quos tempore magni repudiandae maxime, magnam exercitationem culpa corporis eum"
                        "Unde recusandae voluptates soluta dolor. Recusandae enim nisi, voluptate omnis autem ipsum consequatur eaque!"
                        "Minus ut at doloribus inventore? Autem temporibus, ullam illum perferendis exercitationem ducimus optio debitis"
                        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet exercitationem distinctio soluta nisi doloribus,"
                        "odio quia molestias quam praesentium fuga aliquid laudantium sequi saepe repellat. Labore ducimus laudantium totam ratione?"
                        "Distinctio facilis vel ipsa consequuntur enim asperiores repellendus voluptas nulla tempora mollitia perspiciatis"
                        "eos quasi consectetur quos tempore magni repudiandae maxime, magnam exercitationem culpa corporis eum"
                        "Unde recusandae voluptates soluta dolor. Recusandae enim nisi, voluptate omnis autem ipsum consequatur eaque!"
                        "Minus ut at doloribus inventore? Autem temporibus, ullam illum perferendis exercitationem ducimus optio debitis" 
                        "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eveniet exercitationem distinctio soluta nisi doloribus,"
                        "odio quia molestias quam praesentium fuga aliquid laudantium sequi saepe repellat. Labore ducimus laudantium totam ratione?"
                        "Distinctio facilis vel ipsa consequuntur enim asperiores repellendus voluptas nulla tempora mollitia perspiciatis"
                        "eos quasi consectetur quos tempore magni repudiandae maxime, magnam exercitationem culpa corporis eum"
                        "Unde recusandae voluptates soluta dolor. Recusandae enim nisi, voluptate omnis autem ipsum consequatur eaque!"
                    "Minus ut at doloribus inventore? Autem temporibus, ullam illum perferendis exercitationem ducimus",
            'images': "head.png"
        }
    ]

    return render(request, 'blog/index.html', {
        "index": d
    })

def blog(request):
    b = [
        {
            "book_name": 'Game of Thrones',
            "genres": ["Action", "Fantasy", "Serials"],
            "image": "throne.jpg",
        },
        {
            "book_name": 'Dragon',
            "genres": ["Fantasy", "Serials", "Drama"],
            "image": "drag.jpg",
        },
        {
            "book_name": 'Magic',
            "genres": ["Action", "Drama", "Serials"],
            "image": "magic.jpg",
        },
        {
            "book_name": 'Game of Thrones',
            "genres": ["Action", "Fantasy", "Serials"],
            "image": "throne.jpg",
        },
        {
            "book_name": 'Magic',
            "genres": ["Action", "Drama", "Serials"],
            "image": "magic.jpg",
        },
        {
            "book_name": 'Dragon',
            "genres": ["Fantasy", "Serials", "Drama"],
            "image": "drag.jpg",
        },
    ]

    return render(request, "blog/blogg.html",{
        "blogs": b
        } 
    )

def contacts(request):
    return render(request, "blog/contacts.html")

def about(request):
    a = [
        {
        "name": "My name is Aram Hovhannisyan",
        "education": "School number 18",
        "skills": ["Python", "Git", "Trello", "Html/Css", "Django-slightly"],
        "courses":" Gitc  Technology  Center  Python",
    }
    ]

    return render(request, "blog/about.html", {
        "abouts": a
    })