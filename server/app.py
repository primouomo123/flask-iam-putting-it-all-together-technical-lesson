#!/usr/bin/env python3

from flask import request, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from models import User, Post, UserSchema, PostSchema

from config import app, db, api

if __name__ == '__main__':
    app.run(port=5555, debug=True)