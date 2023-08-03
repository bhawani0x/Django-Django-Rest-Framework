**AbstractUser vs AbstractBaseUser**
The default user model in Django uses a username to identify a user during authentication uniquely. If you'd instead use an email address, you must create a custom user model by subclassing AbstractUser or AbstractBaseUser.

**Options:**
1. AbstractUser: Use this option if you are happy with the existing fields on the user model and want to remove the username field.
2. AbstractBaseUser: Use this option if you want to start from scratch by creating your own, completely new user model.

**The steps are the same for each:**
1. Create a custom user model and Manager
2. Update settings.py
3. Customize the UserCreationForm and UserChangeForm forms
4. Update the admin


**Follow the below steps for creating custom user**
1. create a new users app
2. Add the new app to the INSTALLED_APPS list in settings.py
3. add below code to users/test.py
4. create a new file managers.py
5. Update users/models.py:
6. add ```AUTH_USER_MODEL = "users.CustomUser"``` to settings.py
7. run migrations and migrate commands
