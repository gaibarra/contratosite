from django import forms
from django.forms import ModelForm
# from django.core.exceptions import ValidationError
# import re

from django.contrib.auth.models import User
from .models import Departamento, Partes, Contratos, Puestos

# def validate_rfc(value):
#     pattern = r'^[A-Za-z]{4}\d{6}'
#     if not re.match(pattern, value):
#         raise ValidationError(
#             ('El RFC debe contener las cuatro primeras letras y los seis siguientes deben ser números'),
#             params={'value': value},
#         )
        
        
class DateInput(forms.DateInput):
    input_type = 'date'


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['claveDepartamento', 'claveCampus', 'claveArea', 'nombreDepartamento',
                  'f001', 'f002', 'f003', 'testigoUsual1', 'testigoUsual2', 'estado']
        exclude = ['um', 'fm', 'uc', 'fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['nombreDepartamento'].widget.attrs['style'] = "width:400px"
        self.fields['testigoUsual1'].widget.attrs['style'] = "width:400px"
        self.fields['testigoUsual2'].widget.attrs['style'] = "width:400px"
        self.fields['f001'].widget.attrs['style'] = "width:400px"
        self.fields['f002'].widget.attrs['style'] = "width:400px"
        self.fields['f003'].widget.attrs['style'] = "width:400px"


        
class PartesForm(ModelForm):
    
    # rfc = forms.CharField(validators=[validate_rfc])

    claveDepartamento = forms.ModelChoiceField(
        queryset=Departamento.objects.filter(estado=True)
        .order_by('claveDepartamento')
    )

    domicilioParte = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "cols": 80,
                "placeholder": "Domicilio completo",
                "verbose_name": "Domicilio",
            }
        )
    )

    class Meta:
        model = Partes
        fields = ['claveDepartamento', 'estatusParte', 'codigo', 'tituloParte', 'nombresParte', 'apellidoPaternoParte', 'apellidoMaternoParte', 'fecha_ingreso', 'email', 'lugarnacimientoParte', 'rfc', 'imss',  'curp',
                  'nacionalidadParte', 'estadocivilParte', 'regfiscalParte', 'cedula_profParte', 'titulo_profParte', 'universidadParte', 'domicilioParte', 'phone', 'mobile', 'grupo_sanguineo', 'alergias', 'clavePuesto', 'actividadesParte', 'beneficiario1', 'parentesco1', 'porcentaje1' , 'beneficiario2',  'parentesco2', 'porcentaje2','beneficiario3', 'parentesco3',  'porcentaje3']
        exclude = ['um', 'fm', 'uc', 'fc']

        widgets = {
            'fecha_ingreso': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['estatusParte'].widget.attrs['style'] = "width:450px"
        self.fields['codigo'].widget.attrs['style'] = "width:100px"
        self.fields['codigo'].widget.attrs['readonly'] = True
        self.fields['claveDepartamento'].widget.attrs['style'] = "width:540px"
        self.fields['tituloParte'].widget.attrs['style'] = "width:110px"
        self.fields['apellidoPaternoParte'].widget.attrs['style'] = "width:160px"
        self.fields['apellidoMaternoParte'].widget.attrs['style'] = "width:160px"
        self.fields['titulo_profParte'].widget.attrs['style'] = "width:300px"
        self.fields['universidadParte'].widget.attrs['style'] = "width:400px"
        self.fields['cedula_profParte'].widget.attrs['style'] = "width:200px"
        self.fields['beneficiario1'].widget.attrs['style'] = "width:300px"
        self.fields['parentesco1'].widget.attrs['style'] = "width:200px"
        self.fields['porcentaje1'].widget.attrs['style'] = "width:100px"
        self.fields['beneficiario2'].widget.attrs['style'] = "width:300px"
        self.fields['parentesco2'].widget.attrs['style'] = "width:200px"
        self.fields['porcentaje2'].widget.attrs['style'] = "width:100px"
        self.fields['beneficiario3'].widget.attrs['style'] = "width:300px"
        self.fields['parentesco3'].widget.attrs['style'] = "width:200px"
        self.fields['porcentaje3'].widget.attrs['style'] = "width:100px"
        self.fields['clavePuesto'].widget.attrs['style'] = "width:500px"
        self.fields['clavePuesto'].widget.attrs['verbose_name'] = "Puesto"
        self.fields['domicilioParte'].widget.attrs['verbose_name'] = "Domicilio"
        self.fields['actividadesParte'].widget.attrs['style'] = "width:600px"
        self.fields['fecha_ingreso'].widget.attrs['style'] = "width:200px"
        self.fields['clavePuesto'].required = True
        self.fields['rfc'].required = True
        self.fields['curp'].required = True
        self.fields['nombresParte'].required = True
        self.fields['apellidoPaternoParte'].required = True
        # self.fields['beneficiario1'].required = True
        # self.fields['parentesco1'].required = True
        # self.fields['parentesco1'].required = True


class PartesForm2(ModelForm):
    
    
    # rfc = forms.CharField(validators=[validate_rfc])
    
    # claveDepartamento = forms.ModelChoiceField(
    #     queryset=Departamento.objects.filter(estado=True)
    #         .order_by('claveDepartamento')
    #     )

    domicilioParte = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "cols": 80,
                "placeholder": "Domicilio completo",
                "verbose_name": "Domicilio",
            }
        )
    )

    class Meta:
        model = Partes
        fields = ['claveDepartamento', 'estatusParte', 'codigo', 'tituloParte', 'nombresParte', 'apellidoPaternoParte', 'apellidoMaternoParte', 'fecha_ingreso', 'email', 'lugarnacimientoParte', 'rfc', 'imss',  'curp',
                  'nacionalidadParte', 'estadocivilParte', 'regfiscalParte', 'cedula_profParte', 'titulo_profParte', 'universidadParte', 'domicilioParte', 'phone', 'mobile', 'grupo_sanguineo', 'alergias', 'clavePuesto', 'actividadesParte', 'beneficiario1', 'parentesco1', 'porcentaje1' , 'beneficiario2',  'parentesco2', 'porcentaje2','beneficiario3', 'parentesco3',  'porcentaje3']
        exclude = ['um', 'fm', 'uc', 'fc']

        widgets = {
            'fecha_ingreso': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['estatusParte'].widget.attrs['style'] = "width:450px"
        self.fields['codigo'].widget.attrs['style'] = "width:100px"
        self.fields['codigo'].widget.attrs['readonly'] = True
        self.fields['claveDepartamento'].widget.attrs['style'] = "width:540px"
        self.fields['tituloParte'].widget.attrs['style'] = "width:110px"
        self.fields['apellidoPaternoParte'].widget.attrs['style'] = "width:160px"
        self.fields['apellidoMaternoParte'].widget.attrs['style'] = "width:160px"
        self.fields['titulo_profParte'].widget.attrs['style'] = "width:300px"
        self.fields['universidadParte'].widget.attrs['style'] = "width:400px"
        self.fields['cedula_profParte'].widget.attrs['style'] = "width:200px"
        self.fields['beneficiario1'].widget.attrs['style'] = "width:300px"
        self.fields['parentesco1'].widget.attrs['style'] = "width:200px"
        self.fields['porcentaje1'].widget.attrs['style'] = "width:100px"
        self.fields['beneficiario2'].widget.attrs['style'] = "width:300px"
        self.fields['parentesco2'].widget.attrs['style'] = "width:200px"
        self.fields['porcentaje2'].widget.attrs['style'] = "width:100px"
        self.fields['beneficiario3'].widget.attrs['style'] = "width:300px"
        self.fields['parentesco3'].widget.attrs['style'] = "width:200px"
        self.fields['porcentaje3'].widget.attrs['style'] = "width:100px"
        self.fields['clavePuesto'].widget.attrs['style'] = "width:500px"
        self.fields['clavePuesto'].widget.attrs['verbose_name'] = "Puesto"
        self.fields['domicilioParte'].widget.attrs['verbose_name'] = "Domicilio"
        self.fields['actividadesParte'].widget.attrs['style'] = "width:600px"
        self.fields['fecha_ingreso'].widget.attrs['style'] = "width:200px"
        self.fields['clavePuesto'].required = True
        self.fields['rfc'].required = True
        self.fields['curp'].required = True
        self.fields['nombresParte'].required = True
        self.fields['apellidoPaternoParte'].required = True
        # self.fields['beneficiario1'].required = True
        # self.fields['parentesco1'].required = True
        # self.fields['parentesco1'].required = True


class ContratosForm(forms.ModelForm):

    class Meta:
        model = Contratos
        fields = ['id', 'tipocontrato',  'parte2', 'datecontrato', 'datecontrato_ini', 'datecontrato_fin', 'importeContrato',  'npContrato', 'imppContrato', 'totalhorasContrato',
                  'testigoContrato1',  'testigoContrato2', 'empresa', 'rfc_sociedad', 'tipo_sociedad', 'testimonio', 'domicilio_sociedad', 'clausula','objeto_social'  ]
        exclude = ['um', 'fm', 'uc', 'fc']
        
        widgets = {
            'datecontrato_ini': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        
            'datecontrato_fin': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
            
            'datecontrato': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'placeholder': 'Select a date',
                       'type': 'date'
                       }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['tipocontrato'].widget.attrs['style'] = "width:750px"
        
        self.fields['parte2'].widget.attrs['style'] = "width:450px"
        self.fields['datecontrato_ini'].widget.attrs['style'] = "width:200px"
        self.fields['datecontrato_fin'].widget.attrs['style'] = "width:200px"
        
        self.fields['importeContrato'].widget.attrs['style'] = "width:160px"
        
        self.fields['imppContrato'].widget.attrs['style'] = "width:160px"
        self.fields['testigoContrato1'].widget.attrs['style'] = "width:350px"
        self.fields['testigoContrato2'].widget.attrs['style'] = "width:350px"
       
        self.fields['empresa'].widget.attrs['style'] = "width:450px"
        self.fields['empresa'].label = "Nombre de la empresa"
        
        self.fields['rfc_sociedad'].widget.attrs['style'] = "width:350px"
        self.fields['rfc_sociedad'].label = "R.F.C "  
        self.fields['tipo_sociedad'].widget.attrs['style'] = "width:450px"
        self.fields['tipo_sociedad'].label = "Tipo de sociedad"
        
        self.fields['testimonio'].widget.attrs['style'] = "width:450px; height: 100px;"
        self.fields['testimonio'].label = "Descripción de la Escritura Pública"
        
        self.fields['domicilio_sociedad'].widget.attrs['style'] = "width:450px; height: 100px;"
        self.fields['domicilio_sociedad'].label = "Domicilio de la sociedad"
        
        self.fields['clausula'].widget.attrs['style'] = "width:450px; height: 100px;"
        self.fields['clausula'].label = "Claúsula de representación legal"
        
        self.fields['objeto_social'].widget.attrs['style'] = "width:450px; height: 100px;"
        self.fields['objeto_social'].label = "Actividad principal de la sociedad"
        
class PuestosForm(forms.ModelForm):
    class Meta:
        model = Puestos
        fields = ['nombrePuesto', 'claveCampus', 'caracteristicasPuesto', 'conocimientosPuesto',
                  'experienciaPuesto', 'funcionesPuesto', 'habilidadesPuesto', 'herramientasPuesto']
        exclude = ['um', 'fm', 'uc', 'fc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['nombrePuesto'].widget.attrs['style'] = "width:700px"
        self.fields['nombrePuesto'].widget.attrs['readonly'] = True
        self.fields['claveCampus'].widget.attrs['style'] = "width:700px"
        self.fields['claveCampus'].widget.attrs['readonly'] = True
        self.fields['caracteristicasPuesto'].widget.attrs['style'] = "width:700px"
        self.fields['conocimientosPuesto'].widget.attrs['style'] = "width:700px"
        self.fields['experienciaPuesto'].widget.attrs['style'] = "width:700px"
        self.fields['funcionesPuesto'].widget.attrs['style'] = "width:700px"
        self.fields['habilidadesPuesto'].widget.attrs['style'] = "width:700px"
        self.fields['herramientasPuesto'].widget.attrs['style'] = "width:700px"
