from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class CustomUserCreationForm(UserChangeForm):

	class Meta(UserCreationForm):
		model = get_user_model()
		fields = ('email', 'username',)		#string for creation new form


class CustomUserChangeForm(UserChangeForm):

	class Meta(UserChangeForm):
		model = get_user_model()
		fields = ('email', 'username',)		#string for change new form