from django.forms import ModelForm
from .models import Firstyearform

class FirstyearAdmission(ModelForm):
    class Meta:
        model = Firstyearform
        fields = '__all__'
        labels = {
            'guardian_cnumber': 'Father CNIC Number',
            'Guardian_mlyincome': 'Guardian Monthly Income',
            'cnic_no': 'CNIC Number',
            'cnic_img': 'CNIC Image',
            'vaccination_img': 'Vaccination Image',
            'slip_img': 'Slip Image',
            
        }

    def __init__(self, *args, **kwargs):
        super(FirstyearAdmission, self).__init__(*args, **kwargs)
        self.fields['religion'].empty_label = "Select"