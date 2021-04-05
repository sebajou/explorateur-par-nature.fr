from django.test import Client
import pytest

c = Client()


class TestAPIAccess:
    """Test access to API on Users, Badge, Tribut, Child, Trophies, TutorLink,
    Article, Bibliography, Equipment, Image, ListImage, ListEquipment, ListVideo, Video"""

    @pytest.mark.django_db
    def test_api_access_users(self):
        response = c.get('http://127.0.0.1:8000/api/Userss/')
        assert response.status_code == 401

    def test_api_access_badge(self):
        response = c.get('http://127.0.0.1:8000/api/Badges/')
        assert response.status_code == 401

    def test_api_access_tribut(self):
        response = c.get('http://127.0.0.1:8000/api/Tributs/')
        assert response.status_code == 401

    def test_api_access_child(self):
        response = c.get('http://127.0.0.1:8000/api/Childs/')
        assert response.status_code == 401

    def test_api_access_trophies(self):
        response = c.get('http://127.0.0.1:8000/api/Trophiess/')
        assert response.status_code == 401

    def test_api_access_tutor_link(self):
        response = c.get('http://127.0.0.1:8000/api/TutorLinks/')
        assert response.status_code == 401

    def test_api_access_articles(self):
        response = c.get('http://127.0.0.1:8000/api/Articles/')
        assert response.status_code == 401

    def test_api_access_bibliography(self):
        response = c.get('http://127.0.0.1:8000/api/Bibliographys/')
        assert response.status_code == 401

    def test_api_access_equipment(self):
        response = c.get('http://127.0.0.1:8000/api/Equipments/')
        assert response.status_code == 401

    def test_api_access_image(self):
        response = c.get('http://127.0.0.1:8000/api/Images/')
        assert response.status_code == 401

    def test_api_access_list_image(self):
        response = c.get('http://127.0.0.1:8000/api/ListImages/')
        assert response.status_code == 401

    def test_api_access_list_equipment(self):
        response = c.get('http://127.0.0.1:8000/api/ListEquipments/')
        assert response.status_code == 401

    def test_api_access_listvideo(self):
        response = c.get('http://127.0.0.1:8000/api/ListVideos/')
        assert response.status_code == 401

    def test_api_access_video(self):
        response = c.get('http://127.0.0.1:8000/api/Videos/')
        assert response.status_code == 401
