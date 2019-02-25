"""
File::__init__.py
Author::Kevin.P.Barnett
Date::Feb.18.2019
"""

import os
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'poll_db.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        print('Failed to Create Path: '+app.instance_path)

    from . import db, ep_app, ep_slack, ep_admin
    db.init_app(app)

    app.register_blueprint(ep_app.bp)
    app.register_blueprint(ep_slack.bp)
    app.register_blueprint(ep_admin.bp)

    return app