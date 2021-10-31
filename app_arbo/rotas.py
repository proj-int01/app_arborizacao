from flask import render_template, session, request, redirect, url_for

from app_arbo import app, db

@app.route('/')
def home():
    return "<h1>Teste inicial da nossa página</h1><p>Projeto Integrador Tumra 2020 - Polo Monte Alto</p>"