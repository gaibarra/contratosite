from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
#from .reportes import imprimir_solicitud, imprimir_archivos


urlpatterns = [

    path('contratos/contrata/<int:id>',
         coverletter_export, name="coverletter_export"),

    path('contratos/avanza/<int:id>', contratosAvanza, name="contratos_avanza"),
    path('contratos/devuelve/<int:id>',
         contratosDevuelve, name="contratos_devuelve"),


    path('coverletter/export', coverletter_export, name='coverletter_export'),

    path('departamentos/', DepartamentoView.as_view(), name="departamento_list"),
    path('departamentos/new', DepartamentoNew.as_view(), name="departamento_new"),
    path('departamentos/<int:pk>', DepartamentoEdit.as_view(),
         name="departamento_edit"),
    path('departamentos/estado/<int:id>',
         departamentoInactivar, name="departamento_inactivar"),


    path('puestos/', PuestosView.as_view(), name="puestos_list"),
    path('puestos/new', PuestosNew.as_view(), name="puestos_new"),
    path('puestos/<int:pk>', PuestosEdit.as_view(), name="puestos_edit"),
    # path('partes/estado/<int:id>',partesInactivar, name="partes_inactivar"),
    path('puestos/buscar-parte', PuestosView.as_view(), name="buscar_puesto"),




    path('partes/', PartesView.as_view(), name="partes_list"),
    path('partes/new', PartesNew.as_view(), name="partes_new"),
    path('partes/<int:pk>', PartesEdit.as_view(), name="partes_edit"),
     path('partes/<int:id>/faltantes', partes_faltantes, name="partes_faltantes"),
    path('partes/estado/<int:id>', partesInactivar, name="partes_inactivar"),
    path('partes/buscar-parte', PartesView.as_view(), name="buscar_parte"),
    path('partes/<int:pk>/beneficiarios/', generar_documento_beneficiarios, name='generar_beneficiarios'),



    path('contratos/', ContratosView.as_view(), name="contrato_list"),
    path('contratos/new', contratos2, name="contrato_new"),
    
    path('contratos/edit/<int:contrato_id>', contratos2, name="contrato_edit"),
    
    path('contratos/edit2/<int:pk>',
         ContratosEdit.as_view(), name="contrato_edit2"),
    
    


    #path('partes/new2',partes2, name="sujeto_new"),
    path('contratos/gracont/<int:id>', contratoGracont, name="contrato_gracont"),

    path('doctos/<int:contrato_id>/delete/<int:pk>',
         DoctosDetDelete.as_view(), name="doctos_del"),
    path('doctos/edit/<int:contrato_id>', contratos2, name="doctos_edit"),
    
    
    
#     path('change_password/', change_password, name='change_password'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
