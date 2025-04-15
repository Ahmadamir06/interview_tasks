from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class ChatForm(FlaskForm):
    body = TextAreaField('Message', validators=[DataRequired(), Length(1, 500)])
    submit = SubmitField()