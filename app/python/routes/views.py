from flask import Blueprint, render_template

main_views = Blueprint('main_routes', __name__)

@main_views.route('/')
def main(**kwargs):
    return render_template("index.html")
