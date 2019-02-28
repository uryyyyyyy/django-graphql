from django.contrib.auth.models import BaseUserManager

from utils.choices import USER_ROLES


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_superuser(self, email, password, **kwargs):
        """
        for createsuperuser command.
        https://docs.djangoproject.com/ja/2.1/ref/contrib/auth/#django.contrib.auth.models.UserManager.create_superuser
        """
        print('create_superuser')
        kwargs["email"] = self.normalize_email(email)
        kwargs["role"] = USER_ROLES.ADMINISTRATOR
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True
        user = self.model(**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
