from django.contrib.auth.models import BaseUserManager

class AUserManager(BaseUserManager):
	def create_user(self, username, password=None):
		if not username:
			raise ValueError('Escoge un nombre de usuario')

		user = self.model(username=username)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username,password):
		user = self.create_user(username, password)
		user.admin = True
		user.is_superuser = True
		user.save(using = self._db)
		return user