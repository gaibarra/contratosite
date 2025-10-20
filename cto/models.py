from ckeditor.fields import RichTextField
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from django.utils import timezone


from django.db import models
from django.contrib.auth.models import User

#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from bases.models import ClaseModelo, ClaseModelo2

class Campus(ClaseModelo2):
    claveCampus =  models.CharField('Clave Campus', max_length=3, blank=False, null=False, unique=True) 
    nombreCampus =  models.CharField('Nombre Campus', max_length=150, blank=False, null=False) 
    direccionCampus = models.CharField('Dirección Fiscal Campus', max_length=200, blank=False, null=False)
    directorCampus =  models.CharField('Director Campus', max_length=150, blank=False, null=False)
    telefonoCampus  = models.CharField('Telefono Campus', max_length=13, blank=True, null=True)
    rdMin = models.IntegerField()
    rdMax = models.IntegerField()
    
    def __str__(self):
        
        return self.claveCampus

    def save(self):
        self.nombreCampus = self.nombreCampus.upper()
        super(Campus, self).save()

    class Meta:
        verbose_name_plural = "Campus"
        verbose_name="Campus"

class Area(ClaseModelo2):
    idArea =  models.CharField('Clave Área', max_length=3, blank=False, null=False, unique=True) 
    nombreArea =  models.CharField('Nombre Área', max_length=150, blank=False, null=False) 
    claveCampus = models.ForeignKey(Campus, on_delete=models.CASCADE)
    responsableArea =  models.CharField('Responsable Área', max_length=150, blank=False, null=False)
    
    
    def __str__(self):
        
        return self.idArea

    def save(self):
        self.nombreArea = self.nombreArea.upper()
        super(Area, self).save()

    class Meta:
        verbose_name_plural = "Áreas"
        verbose_name="Área"


class Departamento(ClaseModelo2):
    claveDepartamento = models.CharField('Clave Departamento', max_length=4, blank=False, null=False, unique=True, default="")
    claveCampus = models.ForeignKey(Campus, on_delete=models.CASCADE, default="")
    claveArea = models.ForeignKey(Area, on_delete=models.CASCADE, default="")
    nombreDepartamento = models.CharField(max_length=200)
    f001 = models.CharField('Asimilados', max_length=60, blank=True, null=True)
    f002 = models.CharField('Sueldos', max_length=60, blank=True, null=True)
    f003 = models.CharField('Honorarios', max_length=60, blank=True, null=True)
    f004 = models.CharField('Comodato', max_length=60, blank=True, null=True)
    f005 = models.CharField('Formato5', max_length=60, blank=True, null=True)
    f006 = models.CharField('Formato6', max_length=60, blank=True, null=True)
    f007 = models.CharField('Formato7', max_length=60, blank=True, null=True)
    f008 = models.CharField('Formato8', max_length=60, blank=True, null=True)
    f009 = models.CharField('Formato9', max_length=60, blank=True, null=True)
    f010 = models.CharField('Formato10', max_length=60, blank=True, null=True)
    f011 = models.CharField('Formato11', max_length=60, blank=True, null=True)
    f012 = models.CharField('Formato12', max_length=60, blank=True, null=True)
    f013 = models.CharField('Formato13', max_length=60, blank=True, null=True)
    f014 = models.CharField('Formato14', max_length=60, blank=True, null=True)
    f015 = models.CharField('Formato15', max_length=60, blank=True, null=True)
    f016 = models.CharField('Formato16', max_length=60, blank=True, null=True)
    f017 = models.CharField('Formato17', max_length=60, blank=True, null=True)
    f018 = models.CharField('Formato18', max_length=60, blank=True, null=True)
    f019 = models.CharField('Formato19', max_length=60, blank=True, null=True)
    f020 = models.CharField('Formato20', max_length=60, blank=True, null=True)
    f021 = models.CharField('Formato21', max_length=60, blank=True, null=True)
    f022 = models.CharField('Formato22', max_length=60, blank=True, null=True)
    f023 = models.CharField('Formato23', max_length=60, blank=True, null=True)
    f024 = models.CharField('Formato24', max_length=60, blank=True, null=True)
    f025 = models.CharField('Formato25', max_length=60, blank=True, null=True)
    f026 = models.CharField('Formato26', max_length=60, blank=True, null=True)
    f027 = models.CharField('Formato27', max_length=60, blank=True, null=True)
    f028 = models.CharField('Formato28', max_length=60, blank=True, null=True)
    f029 = models.CharField('Formato29', max_length=60, blank=True, null=True)
    f030 = models.CharField('Formato30', max_length=60, blank=True, null=True)
    f031 = models.CharField('Formato31', max_length=60, blank=True, null=True)
    f032 = models.CharField('Formato32', max_length=60, blank=True, null=True)
    f033 = models.CharField('Formato33', max_length=60, blank=True, null=True)
    f034 = models.CharField('Formato34', max_length=60, blank=True, null=True)
    f035 = models.CharField('Formato35', max_length=60, blank=True, null=True)
    f036 = models.CharField('Formato36', max_length=60, blank=True, null=True)
    f037 = models.CharField('Formato37', max_length=60, blank=True, null=True)
    f038 = models.CharField('Formato38', max_length=60, blank=True, null=True)
    f039 = models.CharField('Formato39', max_length=60, blank=True, null=True)
    f040 = models.CharField('Formato40', max_length=60, blank=True, null=True)
    f041 = models.CharField('Formato41', max_length=60, blank=True, null=True)
    f042 = models.CharField('Formato42', max_length=60, blank=True, null=True)
    f043 = models.CharField('Formato43', max_length=60, blank=True, null=True)
    f044 = models.CharField('Formato44', max_length=60, blank=True, null=True)
    f045 = models.CharField('Formato45', max_length=60, blank=True, null=True)
    f046 = models.CharField('Formato46', max_length=60, blank=True, null=True)
    f047 = models.CharField('Formato47', max_length=60, blank=True, null=True)
    f048 = models.CharField('Formato48', max_length=60, blank=True, null=True)
    f049 = models.CharField('Formato49', max_length=60, blank=True, null=True)
    f050 = models.CharField('Formato50', max_length=60, blank=True, null=True)
    rango1 = models.IntegerField('Rango inicial', blank=True, null=True)  
    rango2 = models.IntegerField('Rango final', blank=True, null=True)
    direccion = models.IntegerField('Dirección', blank=True, null=True)
    testigoUsual1 = models.CharField('Testigo usual 1', max_length=100, blank=True, null=True)
    testigoUsual2 = models.CharField('Testigo usual 2', max_length=100, blank=True, null=True)


    def __str__(self):
        return '{}'.format(self.claveDepartamento + "  " + self.nombreDepartamento )

    def save(self):
        self.nombreDepartamento = self.nombreDepartamento.upper()
        super(Departamento, self).save()

    class Meta:
        verbose_name_plural = "Departamentos"
        verbose_name="Departamento"

class Puestos(ClaseModelo2):
    nombrePuesto = models.CharField('Nombre del puesto', max_length=100, blank=False, null=False)
    claveCampus = models.CharField('Clave del Campus', max_length=3, blank=False, null=False)
    caracteristicasPuesto = RichTextField('Características', blank=True, null=True)
    funcionesPuesto = RichTextField('Funciones', blank=True, null=True)
    herramientasPuesto = RichTextField('Herramientas', blank=True, null=True)
    habilidadesPuesto = RichTextField('Habilidades', blank=True, null=True)
    experienciaPuesto = RichTextField('Experiencia', blank=True, null=True)
    conocimientosPuesto = RichTextField('Conocimientos', blank=True, null=True)

    
    def __str__(self):
        return '{}'.format(self.nombrePuesto)

    def save(self):
        super(Puestos,self).save()

    class Meta:
        verbose_name_plural = "Puestos"
        verbose_name="Puesto"   



class Regimen(ClaseModelo2):
    claveRegimen = models.IntegerField('Clave del Régimen Fiscal', blank=True, null=True)
    nombreRegimen = models.CharField('Nombre del Régimen Fiscal', max_length=150, blank=False, null=False)
    aplicaFisica = models.BooleanField('Aplica Persona Física', default=False)
    aplicaMoral = models.BooleanField('Aplica Persona Moral', default=False)
    fechaInicio = models.DateField('Fecha de inicio',  blank=True, null=True)


    def __str__(self):
        return '{}'.format(self.nombreRegimen)

    def save(self):
        super(Regimen,self).save()

    class Meta:
        verbose_name_plural = "Regímenes Fiscales"
        verbose_name="Régimen Fiscal"         

class Partes(ClaseModelo2):
    class Estatus(models.IntegerChoices):
        PRO = 1, "PROSPECTO"
        CON = 2, "EN PROCESO DE CONTRATACION"
        CTO = 3, "CONTRATADO"
        VOL = 4, "EN PROCESO BAJA VOLUNTARIA"
        NEC = 5, "EN PROCESO BAJA NECESARIA"
        BJA = 6, "DADO DE BAJA"

    estatusParte = models.PositiveSmallIntegerField(
        choices=Estatus.choices,
        default=Estatus.CON,
        verbose_name="Estatus"
    )
    
    class Tipopersona(models.IntegerChoices):
        PFI = 1, "PERSONA FÍSICA"
        PMO = 2, "PERSONA MORAL"
      

    personaParte = models.PositiveSmallIntegerField(
        choices=Tipopersona.choices,
        default=Tipopersona.PFI,
        verbose_name="Tipo de persona"
    )
    claveDepartamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, to_field='claveDepartamento', default="")
    codigo = models.CharField('Código', max_length=13, blank=True, null=True)
    clavePuesto = models.ForeignKey(Puestos, on_delete=models.CASCADE, blank=True, null=True, default="", verbose_name='Puesto' )
    fecha_ingreso = models.DateField('  *Fecha de ingreso*  ', blank=True, null=True)
    email = models.EmailField('Correo electrónico', blank=True, null=True)
    tituloParte = models.CharField('Título abreviado ', max_length=100, blank=True, null=True)
    nombreParte = models.CharField('Nombre o razón social ', max_length=200, blank=False, null=False)
    nombresParte = models.CharField('Nombres', max_length=100, blank=True, null=True)
    apellidoPaternoParte = models.CharField('Apellido 1', max_length=100, blank=True, null=True)
    apellidoMaternoParte = models.CharField('Apellido 2', max_length=100, blank=True, null=True)
    tituloParte = models.CharField('Título abreviado ', max_length=100, blank=True, null=True)
    lugarnacimientoParte = models.CharField('Lugar de nacimiento ', max_length=100, blank=True, null=True)
    rfc = models.CharField('RFC', max_length=14, blank=True, null=True)
    imss = models.CharField('IMSS', max_length=11, blank=True, null=True)
    curp = models.CharField('CURP', max_length=18, blank=True, null=True)
    ine = models.CharField('INE', max_length=18, blank=True, null=True)
    banco = models.CharField('Banco', max_length=20, blank=True, null=True)
    ctaBanco = models.CharField('Cuenta ', max_length=20, blank=True, null=True)
    regfiscalParte =  models.ForeignKey(Regimen, on_delete=models.CASCADE, null=False)
    idrep_legalParte = models.IntegerField('id Representante legal', blank=True, null=True)
    datos_actaconstParte = RichTextField('Datos acta constitutiva', blank=True, null=True)
    datos_representacion = RichTextField('Datos representacion legal', blank=True, null=True)
    titulo_profParte = models.CharField('Título profesional', max_length=100, blank=True, null=True)
    universidadParte =  models.CharField('Universidad', max_length=100, blank=True, null=True)
    cedula_profParte = models.CharField('Cédula profesional', max_length=100, blank=True, null=True)
    domicilioParte = RichTextField(blank=True, null=True, verbose_name='Domicilio')
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank = True, null = True)
    usuario = models.CharField('Usuario', max_length=50, blank=True, null=True)
    phone = models.CharField('Teléfono', max_length=15, blank=True, null=True)
    mobile = models.CharField('Móvil', max_length=15, blank=True, null=True)
    grupo_sanguineo = models.CharField('Grupo sanguíneo', max_length=40, blank=True, null=True)
    alergias = models.CharField('Alergias', max_length=100, blank=True, null=True)
    salarioDiario = models.FloatField('Salario Diario', blank=True, null=True)
    nacionalidadParte =  models.CharField('Nacionalidad', max_length=30, blank=True, null=True)
    estadocivilParte =  models.CharField('Estado Civil', max_length=30, blank=True, null=True)
    actividadesParte = RichTextField('Actividades', blank=True, null=True)
    beneficiario1 = models.CharField(max_length=100, blank=True, null=True, default="" )
    parentesco1 = models.CharField(max_length=30, blank=True, null=True, default="" )
    porcentaje1 = models.CharField(max_length=10, blank=True, null=True, default="" )
    beneficiario2 = models.CharField(max_length=100, blank=True, null=True, default="" )
    parentesco2 = models.CharField(max_length=30, blank=True, null=True, default="" )
    porcentaje2 = models.CharField(max_length=10, blank=True, null=True, default="" )
    beneficiario3 = models.CharField(max_length=100, blank=True, null=True, default="" )
    parentesco3 = models.CharField(max_length=30, blank=True, null=True, default="" )
    porcentaje3 = models.CharField(max_length=10, blank=True, null=True, default="" )
    

    def __str__(self):
        return '{}'.format(self.nombreParte)

    def save(self):
        super(Partes,self).save()

    def save(self, *args, **kwargs):
        self.nombreParte = self.nombresParte + " " + self.apellidoPaternoParte + " " + self.apellidoMaternoParte
        super(Partes, self).save(*args, **kwargs)  

    class Meta:
        verbose_name_plural = "Partes del contrato"
        verbose_name="Parte del contrato"

class Ciclos(ClaseModelo2):
    descripcionCiclo = models.CharField('Descripción del ciclo', max_length=150, blank=False, null=False)
    date_ini = models.DateTimeField('Fecha inicial del ciclo', blank=True, null=True)
    date_fin = models.DateTimeField('Fecha final del ciclo', blank=True, null=True)
    ciclo_actual = models.BooleanField('Ciclo escolar vigente', default=False)

    def __str__(self):
        return '{}'.format(self.descripcionCiclo)

    def save(self):
        super(Ciclos,self).save()

    class Meta:
        verbose_name_plural = "Ciclos escolares"
        verbose_name="Ciclo escolar"

class Tipocontrato(ClaseModelo2):
    tipoContrato = models.CharField('Tipo de contrato', max_length=150, blank=False, null=False)
    tituloContrato = RichTextField('Título del Contrato', blank=False, null=False)
    textoinicialContrato = RichTextField('Texto inicial del Contrato', blank=False, null=False)
    descripcionContrato = RichTextField('Descripción del Contrato', blank=True, null=True)
    marcatipoContrato = models.BooleanField(default=False)
    enCalidadDe1 = models.CharField('En calidad de 1', max_length=150, blank=False, null=False, default="" )
    enCalidadDe2 = models.CharField('En calidad de 2', max_length=150, blank=False, null=False, default="")
    enCalidadDe2f = models.CharField('En calidad de 2', max_length=150, blank=False, null=False, default="")
    enCalidadDe2e = models.CharField('En calidad de 2', max_length=150, blank=False, null=False, default="")
    
    def __str__(self):
        return '{}'.format(self.tipoContrato)

    def save(self, *args, **kwargs):
        super(Tipocontrato, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Tipos de contrato"
        verbose_name="Tipo de contrato"
        constraints = [
            # Garantiza que solo exista un Tipocontrato activo (estado=True)
            # con marcatipoContrato=True al mismo tiempo.
            models.UniqueConstraint(
                fields=["marcatipoContrato"],
                condition=models.Q(marcatipoContrato=True, estado=True),
                name="uniq_tipocontrato_true_only_one_active",
            )
        ]

class Requisitos(ClaseModelo2):
    tipocontrato = models.ForeignKey(Tipocontrato, on_delete=models.CASCADE)
    requisito = models.CharField('Documento', max_length=150, blank=False, null=False)
    coment_req = RichTextField('Descripción', blank=True, null=True)
    indiya =  models.BooleanField('Entregado', default=False)
    
    def __str__(self):
        return '{}'.format(self.requisito)

    def save(self):
        super(Requisitos,self).save()

    class Meta:
        verbose_name_plural = "Requisitos"
        verbose_name="Requisito"

class Contratos(ClaseModelo2):
    tipocontrato = models.ForeignKey(Tipocontrato, on_delete=models.CASCADE, verbose_name='Tipo de Contrato')
    datecontrato = models.DateTimeField('Fecha del contrato', blank=True, null=True)
    datecontrato_ini = models.DateTimeField('Fecha inicial de la vigencia', blank=True, null=True)
    datecontrato_fin = models.DateTimeField('Fecha final de la vigencia', blank=True, null=True)
    parte1 = models.IntegerField('Parte 1', blank=True, null=True, default=3 )
    enCalidadDe1 = models.CharField('En calidad de 1', max_length=150, blank=False, null=False)
    parte2 = models.ForeignKey(Partes, on_delete=models.CASCADE, verbose_name='Sujeto del Contrato')
    enCalidadDe2 = models.CharField('En calidad de 2', max_length=150, blank=False, null=False)
    #parte3 = models.ForeignKey(Partes, on_delete=models.CASCADE)
    #enCalidadDe3 = models.CharField('En calidad de 3', max_length=150, blank=True, null=True)
    lugarContrato = RichTextField('Lugar del Contrato', blank=True, null=True)
    ciudadContrato = models.CharField('Usuario', max_length=50, blank=True, null=True)
    estadoContrato = models.CharField('Usuario', max_length=50, blank=True, null=True)
    paisContrato = models.CharField('Usuario', max_length=50, blank=True, null=True)
    importeContrato = MoneyField('Importe del Contrato', max_digits=13, decimal_places=2, blank=True, null=True, default_currency="MXN")
    npContrato = models.IntegerField('Número de pagos', blank=True, null=True, default = 1)
    imppContrato = MoneyField('Importe de cada pago', max_digits=14, decimal_places=2, blank=False, null=True, default_currency="MXN", default = 0)
    vhppContrato = MoneyField('Valor Hora del Período', max_digits=14, decimal_places=2, blank=False, null=False, default_currency="MXN")
    totalhorasContrato = models.IntegerField('Total de horas', blank=True, default = 40)
    testigoContrato1 = models.CharField('Testigo 1', max_length=100, blank=True, null=True)
    testigoContrato2 = models.CharField('Testigo 2', max_length=100, blank=True, null=True)
    versionContrato = models.CharField('Versión del contrato', max_length=100, blank=True, null=True)
    current_user = models.IntegerField('Usuario actual', blank=True, null=True)
    status = models.CharField('Status de la solicitud', max_length=3, default ="CAP")
    rcap = models.IntegerField('Resposable de Captura', blank=True, null=True)
    fcap = models.DateTimeField('Fecha de Captura', blank=True, null=True)
    rstep1 = models.IntegerField('Resposable step1', blank=True, null=True)
    fstep1 = models.DateTimeField('Fecha step1', blank=True, null=True)
    astep1 = models.CharField('Actividad step1', max_length=3, blank=True, null=True )
    rstep2 = models.IntegerField('Resposable step2', blank=True, null=True)
    fstep2 = models.DateTimeField('Fecha step2', blank=True, null=True)
    astep2 = models.CharField('Actividad step2', max_length=3, blank=True, null=True )
    rstep3 = models.IntegerField('Resposable step3', blank=True, null=True)
    fstep3 = models.DateTimeField('Fecha step3', blank=True, null=True)       
    astep3 = models.CharField('Actividad step3', max_length=3, blank=True, null=True )
    rstep4 = models.IntegerField('Resposable step4', blank=True, null=True)
    fstep4 = models.DateTimeField('Fecha step4', blank=True, null=True)
    astep4 = models.CharField('Actividad step4', max_length=3, blank=True, null=True )
    rstep5 = models.IntegerField('Resposable step5', blank=True, null=True)
    fstep5 = models.DateTimeField('Fecha step5', blank=True, null=True)
    astep5 = models.CharField('Actividad step5', max_length=3, blank=True, null=True )
    rstep6 = models.IntegerField('Resposable step6', blank=True, null=True)
    fstep6 = models.DateTimeField('Fecha step6', blank=True, null=True)
    astep6 = models.CharField('Actividad step6', max_length=3, blank=True, null=True )
    cstep1 = RichTextField('Comentarios 1', blank=True, null=True, default="")
    cstep2 = RichTextField('Comentarios 2', blank=True, null=True, default="")
    cstep3 = RichTextField('Comentarios 3', blank=True, null=True, default="")
    cstep4 = RichTextField('Comentarios 4', blank=True, null=True, default="")
    cstep5 = RichTextField('Comentarios 5', blank=True, null=True, default="")
    cstep6 = RichTextField('Comentarios 6', blank=True, null=True, default="")
    devuelto_por = models.IntegerField('Devuelto por', blank=True, null=True)
    actividadesContrato = RichTextField('Actividades', blank=True, null=True)
    ivaContrato = models.FloatField('IVA del contrato', blank=True, null=True, default = .16)
    importeContratoconiva = models.FloatField('Importe con IVA', blank=True, null=True)
    retivaContrato = models.FloatField('Retención de IVA', blank=True, null=True, default = .1)
    retisrContrato = models.FloatField('Retención de ISR', blank=True, null=True)
    netoContrato = models.FloatField('Importe Neto', blank=True, null=True)
    marcaVehiculo = models.CharField('Marca vehículo', max_length=50, blank=True, null=True)
    modeloVehiculo = models.CharField('Modelo vehículo', max_length=50, blank=True, null=True)
    tipoVehiculo = models.CharField('Tipo vehículo', max_length=50, blank=True, null=True)
    motorVehiculo = models.CharField('Motor vehículo', max_length=50, blank=True, null=True)
    serieVehiculo = models.CharField('Serie vehículo', max_length=50, blank=True, null=True)
    placasVehiculo = models.CharField('Placas vehículo', max_length=50, blank=True, null=True)
    facturaVehiculo = models.CharField('Factura vehículo', max_length=50, blank=True, null=True)
    expedidaFactura = models.CharField('Factura expedida por', max_length=100, blank=True, null=True)
    fechaFactura = models.DateField('Fecha factura', blank=True, null=True)
    tarjetaVehiculo = models.CharField('Tarjeta vehículo', max_length=50, blank=True, null=True)
    expedidaTarjeta = models.CharField('Tarjeta expedida por', max_length=100, blank=True, null=True)
    fechaTarjeta = models.DateField('Fecha tarjeta', blank=True, null=True)
    polizaVehiculo = models.CharField('Póliza vehículo', max_length=50, blank=True, null=True)
    expedidaPoliza = models.CharField('Póliza expedida por', max_length=100, blank=True, null=True)
    fechaPoliza= models.DateField('Fecha vigencia póliza', blank=True, null=True)
    empresa = models.CharField(max_length=150, blank=True, null=True, default="" )
    fecha_constitucion = models.DateField(blank=True, null=True )
    objeto_social = models.TextField(default="", blank=True, null=True )
    domicilio_sociedad = models.TextField(default="", blank=True, null=True )
    registro_mercantil = models.CharField(max_length=50, blank=True, null=True, default="" )
    rfc_sociedad = models.CharField(max_length=25, blank=True, null=True, default="" )
    tipo_sociedad = models.CharField(max_length=150, blank=True, null=True , default="" )
    testimonio = models.TextField(default="", blank=True, null=True )
    clausula = models.TextField(default="", blank=True, null=True )
    

    
    def __str__(self):
        return '{}'.format(self.id)

    def save(self):                                                                                                                                                                              
        super(Contratos,self).save()


    class Meta:
        verbose_name_plural = "Contratos"
        verbose_name="Contrato"


class Secuencia(ClaseModelo2):
    tipocontrato = models.ForeignKey(Tipocontrato, on_delete=models.CASCADE)
    nivel1 = models.IntegerField('Nivel 1', blank=True, null=True)
    nivel2 = models.IntegerField('Nivel 2', blank=True, null=True)
    nivel3 = models.IntegerField('Nivel 3', blank=True, null=True)
    nivel4 = models.IntegerField('Nivel 4', blank=True, null=True)
    identificador = models.CharField('Identificador', max_length=20, blank=True, null=True)
    textoSecuencia = RichTextField('Texto secuencia', blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.tipocontrato)

    def save(self):
        super(Secuencia,self).save()

    class Meta:
        verbose_name_plural = "Secuencia del contrato"
        verbose_name="Secuencia del contrato"
        
class Estados(ClaseModelo2):
    claveEstado = models.CharField('Clave del Estado', max_length=2, blank=False, null=False)
    nombreEstado = models.CharField('Numbre del Estado', max_length=50, blank=False, null=False)
   

    def __str__(self):
        return '{}'.format(self.nombreEstado)

    def save(self):
        super(Estados,self).save()

    class Meta:
        verbose_name_plural = "Estados"
        verbose_name="Estado"

class Niveles(ClaseModelo2):
    nivel = models.CharField('Nivel Escolar', max_length=50, blank=False, null=False)
    
    def __str__(self):
        return '{}'.format(self.nivel)

    def save(self):
        super(Niveles,self).save()

    class Meta:
        verbose_name_plural = "Niveles"
        verbose_name="Nivel"

class Profesiones(ClaseModelo2):
    abrevProfesion = models.CharField('Abreviatura', max_length=20, blank=False, null=False)
    descProfesion = models.CharField('Profesión', max_length=100, blank=False, null=False)
    
    def __str__(self):
        return '{}'.format(self.descProfesion)

    def save(self):
        super(Profesiones,self).save()

    class Meta:
        verbose_name_plural = "Profesiones"
        verbose_name="Profesión"





                                                             

class Valida  (ClaseModelo2):
    tipocontrato = models.ForeignKey(Tipocontrato, on_delete=models.CASCADE)
    nombreCampo = models.CharField('Campo', max_length=50, blank=False, null=False)
    nombreVariable = models.CharField('Variable', max_length=100, blank=False, null=False)
    descVariable = RichTextField('Descripción de la variable', blank=True, null=True)
    captura = models.BooleanField('Captura si/no', default=False)
    indinum = models.BooleanField('Numérico', default=False)

    def __str__(self):
        return '{}'.format(self.tipocontrato)

    def save(self):
        super(Valida,self).save()

    class Meta:
        verbose_name_plural = "Validaciones"
        verbose_name="Validación"    


class Doctos(ClaseModelo2):
    contrato = models.ForeignKey(Contratos, on_delete=models.CASCADE)
    documento = models.ForeignKey(Requisitos, on_delete=models.CASCADE)
    pdf = models.FileField('Archivo del Documento', upload_to='media/', default = 'None/no-img.jpg')
    pdf2 = models.FileField('Archivo del Documento', upload_to='media/', default = 'None/no-img.jpg')
    vigenciaFinDocto = models.DateTimeField('Vigencia del documento', blank=True, null=True)
    comentarioDocto = RichTextField('Comentario del Documento', blank=True, null=True)
    
    def __str__(self):
        return '{}'.format(self.contrato)

    def save(self):
        super(Doctos,self).save()
    
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Documentos"
        verbose_name="Documento"
    
