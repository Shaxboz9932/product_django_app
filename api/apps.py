from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        import api.signals


# pre_save
# post_save
# pre_delete
# post_delete
# m2m_changed