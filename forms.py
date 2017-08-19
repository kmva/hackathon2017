from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, PhoneNumberField
from wtforms.validators import DataRequired, Email, Length

class SignUpForm(FlaskForm):
    first_name = StringField('Имя'.decode('utf-8'), validators=[DataRequired("Введите имя".decode('utf-8'))])
    email = StringField('Почта'.decode('utf-8'), validators=[DataRequired("Введите свой e-mail".decode('utf-8'))]) # Email("Введите свой e-mail".decode('utf-8')))
    password = PasswordField('Пароль'.decode('utf-8'), validators=[DataRequired("Введите пароль".decode('utf-8'))]) # Length(min=6, message="Количество символов не меньше 6".decode('utf-8')))
    phone_number = PhoneNumberField('Номер телефона'.decode('utf-8'), validators=[DataRequired("Введите номер телефона".decode('utf-8'))])
    submit = SubmitField('Зарегистрироваться'.decode('utf-8'), validators=[DataRequired("Введите свой e-mail".decode('utf-8'))]) # Email("Введите свой e-mail".decode('utf-8')))

class LoginForm(FlaskForm):
    email = StringField('Почта', validators=[DataRequired("Введите почту".decode('utf-8'))])
    password = PasswordField('Пароль'.decode('utf-8'), validators=[DataRequired("Введите пароль".decode('utf-8'))]) # Length(min=6, message="Количество символов не меньше 6".decode('utf-8')))
    submit = SubmitField('Войти'.decode('utf-8'), validators=[DataRequired("Введите свой e-mail".decode('utf-8'))]) # Email("Введите свой e-mail".decode('utf-8')))

class SearchingForm(FlaskForm):
    dish = StringField("Поиск".decode('utf-8'), validators=[DataRequired("Введите название")])
