from django import forms
from .models import Comuna
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = '__all__'
        widgets = {
            'fecha_fundacion': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control',
                    'max': '2100-12-31'  # Fecha máxima permitida
                },
                format='%Y-%m-%d'
            ),
            'descripcion': forms.Textarea(attrs={
                'rows': 3,
                'class': 'form-control',
                'placeholder': _('Ingrese una descripción opcional...')
            }),
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': _('Ej: Valparaíso')
            }),
            'poblacion': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'placeholder': _('Ej: 250000')
            }),
            'tasa_vulnerabilidad': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0',
                'max': '100',
                'step': '0.01',
                'placeholder': _('Ej: 25.50')
            }),
        }
        labels = {
            'nombre': _('Nombre de la comuna'),
            'poblacion': _('Población total'),
            'tasa_vulnerabilidad': _('Tasa de vulnerabilidad (%)'),
            'fecha_fundacion': _('Fecha de fundación'),
            'descripcion': _('Descripción adicional'),
        }
        help_texts = {
            'tasa_vulnerabilidad': _('Porcentaje entre 0 y 100 con hasta 2 decimales'),
            'fecha_fundacion': _('Seleccione una fecha en el calendario'),
        }
        error_messages = {
            'nombre': {
                'max_length': _('El nombre es demasiado largo'),
                'required': _('Este campo es obligatorio'),
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Añadir clases CSS a todos los campos automáticamente
        for field_name, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
            if field.required:
                field.widget.attrs['required'] = 'required'

    def clean_poblacion(self):
        data = self.cleaned_data['poblacion']
        if data < 0:
            raise forms.ValidationError(
                _("La población no puede ser negativa"),
                code='poblacion_negativa'
            )
        if data > 10000000:  # 10 millones como límite razonable
            raise forms.ValidationError(
                _("La población no puede exceder 10.000.000"),
                code='poblacion_excedida'
            )
        return data

    def clean_tasa_vulnerabilidad(self):
        data = self.cleaned_data['tasa_vulnerabilidad']
        if data < 0:
            raise forms.ValidationError(
                _("La tasa no puede ser negativa"),
                code='tasa_negativa'
            )
        if data > 100:
            raise forms.ValidationError(
                _("La tasa no puede superar el 100%"),
                code='tasa_excedida'
            )
        return round(data, 2)  # Asegurar 2 decimales

    def clean_fecha_fundacion(self):
        data = self.cleaned_data['fecha_fundacion']
        # Validación adicional de fecha si es necesaria
        # Por ejemplo, no permitir fechas futuras
        from django.utils import timezone
        if data > timezone.now().date():
            raise forms.ValidationError(
                _("La fecha de fundación no puede ser futura"),
                code='fecha_futura'
            )
        return data

    def clean(self):
        cleaned_data = super().clean()
        # Validaciones cruzadas entre campos si son necesarias
        return cleaned_data