from flask import render_template

class Index:

    def index():
        return  render_template(
            'index.html',
            title="Teste Blog",
            description="Um blog para compartilhar algumas informações de um dev.",
            active="home"
        )