from app_conf import app
from flask import render_template


@app.route('/')
def index():
    return render_template(
        'app_index/index.html'
    )
    
