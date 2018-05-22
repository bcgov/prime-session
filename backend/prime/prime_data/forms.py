from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
    
from django import forms

class ViewSessions(forms.Form):
    """
    Form to view all current sessions
    """
    start_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_start_date(self):
        data = self.cleaned_data['start_date']
        
        #Check date is not in past. 
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - date in the past'))
        
        #Check date is in range librarian allowed to change (+4 weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - date more than 4 weeks ahead'))
        
        # Remember to always return the cleaned data.
        return data