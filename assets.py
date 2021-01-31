from flask import current_app as app
from flask_assets import Bundle

def compile_static_assets(assets):
    assets.auto_build = True
    assets.debug = False

    style_bundle = Bundle(
        'src/less/*.less',
        filters='less,cssmin',
        output='dist/css/style.min.css',
        extra={'rel': 'stylesheet/css'}
    )
    js_bundle = Bundle(
        'src/js/main.js',
        filters='jsmin',
        output='dist/js/main.min.js'
    )
    assets.register('main_styles', style_bundle)
    assets.register('main_js', js_bundle)
    style_bundle.build()
    js_bundle.build()