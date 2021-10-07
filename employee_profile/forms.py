from django.forms import Form, CharField, DateField


class UserProfileForm(Form):
    username = CharField(max_length=100)
    dob = DateField()
    full_name = CharField(max_length=100)
    email = CharField(max_length=100)
