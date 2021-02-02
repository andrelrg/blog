from flask import render_template

class Index:

    def index():
        posts = [
            {
                "title": "Teste post do role",
                "description":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem...",
                "git":"andrelrg",
                "tags":["dev", "life"],
                "url":"teste-blog"
            },
            {
                "title": "Isso não é um teste",
                "description":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem...",
                "git":"andrelrg",
                "tags":["dev", "teste"],
                "url":"teste-blog"
            }
        ]

        threads = [
            {
                "title": "Teste thread do role",
                "description":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has...",
                "url":"teste-blog"
            },
            {
                "title": "Isso não é uma thread teste",
                "description":"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has...",
                "url":"teste-blog"
            },
        ]

        return  render_template(
            'index.html',
            posts=posts,
            threads = threads,
            active="home",
            
        )