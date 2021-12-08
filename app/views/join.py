import os
import sys
from ..forms import JoinForm
from flask_restful import Resource
from flask import render_template, make_response, flash, redirect
from flask_bcrypt import Bcrypt

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
            email = form.data.get('email')
            user_id = form.data.get('user_id')
            user_pw = form.data.get('user_pw')
            interesting = form.data.get('interesting')

            from ..model.user import User
            user = User(
                email=email,
                user_id=user_id,
                user_pw=user_pw,
                interesting=interesting)

            from .. import db
            db.session.add(user)
            db.session.commit()

            return redirect('/')
        else:
            # TODO: 동일 키 있을 경우 예외처리, 에러메세지
            flash('올바르지 않은 데이터 입니다.')
            return make_response(render_template('join.html', form=form))
