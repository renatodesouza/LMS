import uuid
from django.contrib.auth.models import BaseUserManager


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename
                  
class UserManager(BaseUserManager):

    use_in_migration = True

    def _create_user_manager(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O E-mail é necessario')

        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user_manager(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('O super usuario precisa ter o atributo is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('O super usuario precisa ter o atributo is_staff=True')

        return self._create_user_manager(email, password, **extra_fields)