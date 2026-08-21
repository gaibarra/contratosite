from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class CambioContrasenaTests(TestCase):
    def test_authenticated_user_can_change_own_password_without_contract_permissions(self):
        user = User.objects.create_user("usuario_regular", password="anterior-segura")
        self.client.force_login(user)

        response = self.client.post(reverse("bases:cambiar_contrasena"), {
            "old_password": "anterior-segura",
            "new_password1": "nueva-clave-segura-2026",
            "new_password2": "nueva-clave-segura-2026",
        })

        self.assertRedirects(response, reverse("bases:home"))
        user.refresh_from_db()
        self.assertTrue(user.check_password("nueva-clave-segura-2026"))

    def test_anonymous_user_is_redirected_to_login(self):
        response = self.client.get(reverse("bases:cambiar_contrasena"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("bases:login"), response.url)
