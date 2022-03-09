from crypt import methods
from unicodedata import category
from flask import render_template, request, redirect, url_for, abort
from . import main
from flask_login import current_user, login_required
from .. import db,photos
from .forms import UpdateProfile, PitchForm
from ..models import Pitch, User, PhotoProfile
from datetime import datetime

import markdown2


@main.route('/', methods = ['GET', 'POST'])
@login_required
def index():
  '''
  view for root page that returns the index page and its data
  '''

  title = 'Home - Welcome to PitchPal'
  user = current_user
