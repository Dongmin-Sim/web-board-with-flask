import os
import sys

from wtforms.validators import Email
from ..forms import JoinForm
from flask_restful import Resource
from flask import render_template, make_response, flash, redirect
from sqlalchemy.exc import IntegrityError

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__name__))))


# Join api
class Join(Resource):
    def get(self):
        form = JoinForm()
        return make_response(render_template('join.html', form=form))

    def post(self):
        form = JoinForm()

        print(form.validate_on_submit(), form.data)

        if form.validate_on_submit():
            from ..model.user import User
            user = User(
                email=form.email.data,
                user_id=form.user_id.data,
                user_pw=form.user_pw.data,
                interesting=form.interesting.data)

            # TODO: 동일 키 있을 경우 예외처리, 에러메세지
            from .. import db

            try:
                db.session.add(user)
                db.session.commit()
                return redirect('/')
            except IntegrityError as e:
                flash('이미 존재하는 아이디 혹은 이메일입니다.', 'integrityerror')
                # code, msg = e.args
                return redirect('/join')

        else:
            flash('올바르지 않은 데이터 입니다.', 'notsubmit')
            return redirect('/join')
