from django import forms

SEX=[
('1','Male'),
('0','Female')
]

CHOICES=[
('1','Typical angina'),
('2','Atypical angina'),
('3','Non-anginal pain'),
('4','Asymptomatic')
]

FASTING_BP=[
('1','Yes'),
('0','No')
]

resting_electrocardiographic_results=[
('0','Normal'),
('1','Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)'),
('2','Showing probable or definite left ventricular hypertrophy by Estes criteria')
]

exercise_induced_angina=[
('1','Yes'),
('0','No')
]

slope_of_the_peak_exercise_ST_segment=[
('1','Upsloping'),
('2','Flat'),
('3','Downsloping')
]

THAL=[
('3','Normal'),
('6','Fixed Defect'),
('7','Reversable Defect')
]
class ContactForm(forms.Form):
	age= forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
	sex=forms.FloatField(widget=forms.RadioSelect(choices=SEX, attrs={'class': 'form-group'}))
	cp=forms.ChoiceField(
		label='Type of chest pain',choices=CHOICES
		)

	trestbps= forms.FloatField(label='Resting BP in mm Hg',
		widget=forms.NumberInput(
			attrs={'class': 'form-control'})
		)
	chol= forms.FloatField(label='Serum cholestoral in mg/dl',
		widget=forms.NumberInput(
			attrs={'class': 'form-control'})
		)
	fbs= forms.FloatField(label='fasting blood sugar > 120 mg/dl',widget=forms.RadioSelect(choices=FASTING_BP))
	restecg=forms.ChoiceField(label='Resting electrocardiographic results',choices=resting_electrocardiographic_results)

	thalach= forms.FloatField(label='Maximum heart rate achieved',
		widget=forms.NumberInput(
			attrs={'class': 'form-control'})
		)
	exang= forms.FloatField(label='Exercise induced angina',widget=forms.RadioSelect(choices=exercise_induced_angina))
	oldpeak= forms.FloatField(label='ST depression induced by exercise relative to rest',
			widget=forms.NumberInput(
			attrs={'class': 'form-control'})
			)

	slope= forms.ChoiceField(label='Slope of the peak exercise ST segment',choices=slope_of_the_peak_exercise_ST_segment)
	
	ca= forms.FloatField(label='Number of major vessels (0-3) colored by flourosopy',
			widget=forms.NumberInput(
			attrs={'class': 'form-control'})
			)
	
	thal= forms.ChoiceField(choices=THAL)
	

	