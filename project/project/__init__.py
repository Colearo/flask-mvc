# -*- coding: utf-8 -*-

__version__ = '0.1'

from flask import Flask, g, redirect
app = Flask('project')
app.config['SECRET_KEY'] ='random'

import project.models
import project.controller


