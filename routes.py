from controllers.index import Index

def routes(app):
    app.add_url_rule('/', 'index', Index.index)