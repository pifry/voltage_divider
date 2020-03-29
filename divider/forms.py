from django import forms


class MyContextForm(forms.Form):
    input_voltage = forms.FloatField(label='Input voltage', required=True, max_value=10, min_value=0)
    output_voltage = forms.FloatField(label='Output voltage', required=True, max_value=10, min_value=0)
    r1_value = forms.FloatField(label='R1', required=False)
