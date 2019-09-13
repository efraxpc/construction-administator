from flask import Flask, request, make_response, redirect, render_template
from flask_bootstrap import Bootstrap

from app import app

bootstrap = Bootstrap(app)