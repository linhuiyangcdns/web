from flask import render_template


from . import main


@main.errorhandler(403)
def execute_access_forbidden(e):
    return render_template('403.html'),403


@main.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500


@main.errorhandler(404)
def page_not_found(e):
    return render_template('400.html'),404