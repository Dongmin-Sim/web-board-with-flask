from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, SelectField
from wtforms.fields import choices
from wtforms.validators import DataRequired, Email, EqualTo, Length


class JoinForm(FlaskForm):
    email = EmailField('이메일 주소', validators=[DataRequired(), Email()])
    user_id = StringField('아이디', validators=[
        DataRequired(), Length(min=8, max=15)])
    user_pw = PasswordField('비밀번호', validators=[
        DataRequired(), Length(min=8, max=20), EqualTo('re_password')])
    re_password = PasswordField('비밀번호 확인', validators=[DataRequired(),
                                Length(min=8, max=20)])
    interesting = SelectField('관심분야', choices=[(
        'Front-end', 'front-end'), ('Back-end', 'back-end'), ('Data-engineer', 'data-engineer'), ('Product-Manager', 'Product-Manager')])
    submit = SubmitField('회원가입')


class LoginForm(FlaskForm):
    user_id = StringField('아이디', validators=[
        DataRequired(), Length(min=8)])
    user_pw = PasswordField('비밀번호', validators=[
        DataRequired(), Length(min=8), EqualTo('re_password')])
    submit = SubmitField('submit')
