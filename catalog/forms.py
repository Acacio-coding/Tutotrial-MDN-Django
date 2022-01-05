from django import forms
import datetime
from django.core.exceptions import ValidationError

class RenewBookForm(forms.Form):
    renew_date = forms.DateField(help_text = 'Enter a date between today and 4 weeks ahead (default: 3).')

    def validate_renew_date(self):
        date = self.cleaned_data['renew_date']

        if date < datetime.date.today():
            raise ValidationError("Invalid date, smaller than today!")

        if date > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError("Invalid date, bigger than 4 weeks ahead")
        
        return date