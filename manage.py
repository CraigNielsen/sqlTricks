# manage.py
from flask import current_app
from flask.ext.script import Command, Manager, Shell, Server

from myapp import theapp, db, models

manager = Manager(theapp)

# @manager.command
# def hello():
#     print "hello"

# @manager.command
# def yoyo():
# 	print "this is a command line exectution yolo :)

class RunServer(Server):
    def handle(self, *args, **kwargs):
        Server.handle(self, *args, **kwargs)
manager.add_command('run-server', RunServer(use_debugger=True, use_reloader=True))

def _make_context():
    context = dict(
        db=db,
        current_app=current_app,
    )
    context.update(vars(models))
    return context
manager.add_command('shell', Shell(make_context=_make_context))


class Hello(Command):
    def run(self):
        print "hello there world"
manager.add_command('Hello', Hello())

if __name__ == "__main__":
    manager.run()
    