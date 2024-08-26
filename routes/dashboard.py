from flask import Blueprint, render_template

dashboard_route = Blueprint('dashboard', __name__)

@dashboard_route.route('/')
def home():
    return render_template('dashboard.html')