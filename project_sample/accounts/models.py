from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)
