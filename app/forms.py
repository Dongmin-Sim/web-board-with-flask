from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class JoinForm(FlaskForm):
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    user_id = StringField('User Id', validators=[
        DataRequired(), Length(min=8, max=15)])
    user_pw = PasswordField('User Password', validators=[
        DataRequired(), Length(min=8, max=20), EqualTo('re_password')])
    re_password = PasswordField('Re Password', validators=[
                                Length(min=8, max=20)])
    interesting = SelectField('interesting', choices=[(
        'Front-end', 'front-end'), ('Back-end', 'back-end'), ('Data-engineer', 'data-engineer'), ('Product-Manager', 'Product-Manager')])
    submit = SubmitField('submit')
