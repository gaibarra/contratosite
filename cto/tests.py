from datetime import timedelta

from django.contrib.auth.models import Permission, User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Area, Campus, Contratos, Departamento, Partes, Regimen, Tipocontrato


class MisContratosViewTests(TestCase):
    def setUp(self):
        self.owner = User.objects.create_user("propietario", password="secreto")
        self.other_user = User.objects.create_user("otro", password="secreto")
        self.admin_user = User.objects.create_superuser("admin", "admin@example.com", "secreto")
        permission = Permission.objects.get(content_type__app_label="cto", codename="view_contratos")
        self.owner.user_permissions.add(permission)
        self.other_user.user_permissions.add(permission)

        campus = Campus(
            claveCampus="CAM", nombreCampus="Campus", direccionCampus="Dirección",
            directorCampus="Director", rdMin=1, rdMax=2, uc=self.owner,
        )
        campus.save()
        area = Area(
            idArea="ARE", nombreArea="Área", claveCampus=campus,
            responsableArea="Responsable", uc=self.owner,
        )
        area.save()
        departamento = Departamento(
            claveDepartamento="001", claveCampus=campus, claveArea=area,
            nombreDepartamento="Departamento", uc=self.owner,
        )
        departamento.save()
        regimen = Regimen(nombreRegimen="General", uc=self.owner)
        regimen.save()
        self.parte = Partes(
            claveDepartamento=departamento, regfiscalParte=regimen,
            nombresParte="Ana", apellidoPaternoParte="Propietaria", apellidoMaternoParte="Prueba",
            uc=self.owner,
        )
        self.parte.save()
        self.tipo = Tipocontrato(
            tipoContrato="Laboral", tituloContrato="Título", textoinicialContrato="Texto", uc=self.owner,
        )
        self.tipo.save()
        self.own_contract = self.create_contract(self.owner, "CAP")
        self.other_contract = self.create_contract(self.other_user, "AUT")

    def create_contract(self, creator, status):
        contrato = Contratos(
            tipocontrato=self.tipo, parte2=self.parte, enCalidadDe1="Patrón",
            enCalidadDe2="Trabajador", vhppContrato=100, status=status,
            datecontrato=timezone.now(), uc=creator,
        )
        contrato.save()
        return contrato

    def test_regular_user_only_sees_own_contracts(self):
        self.client.force_login(self.owner)

        response = self.client.get(reverse("cto:mis_contratos_list"))

        self.assertContains(response, f">{self.own_contract.id}<", html=False)
        self.assertNotContains(response, f">{self.other_contract.id}<", html=False)

    def test_filters_contracts_by_subject_date_type_and_status(self):
        self.client.force_login(self.owner)
        response = self.client.get(reverse("cto:mis_contratos_list"), {
            "sujeto": "Ana Propietaria", "fecha_desde": (timezone.now() - timedelta(days=1)).date(),
            "fecha_hasta": timezone.now().date(), "tipo": self.tipo.id, "estado": "CAP",
        })

        self.assertContains(response, f">{self.own_contract.id}<", html=False)

    def test_regular_user_cannot_open_another_users_contract(self):
        self.client.force_login(self.owner)

        response = self.client.get(reverse("cto:mis_contratos_detalle", args=[self.other_contract.id]))

        self.assertEqual(response.status_code, 404)

    def test_superuser_sees_all_contracts_and_can_open_detail(self):
        self.client.force_login(self.admin_user)

        response = self.client.get(reverse("cto:mis_contratos_list"))
        detail_response = self.client.get(reverse("cto:mis_contratos_detalle", args=[self.other_contract.id]))

        self.assertContains(response, f">{self.own_contract.id}<", html=False)
        self.assertContains(response, f">{self.other_contract.id}<", html=False)
        self.assertEqual(detail_response.status_code, 200)

    def test_superuser_without_own_subject_can_open_global_contract_form(self):
        self.tipo.marcatipoContrato = True
        self.tipo.save()
        self.client.force_login(self.admin_user)

        response = self.client.get(reverse("cto:contrato_new"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.parte.nombreParte)
