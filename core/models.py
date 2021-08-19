from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.mail import send_mail


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    role = models.CharField(max_length=40, blank=False)
    company = models.CharField(max_length=40, blank=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role', 'company']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def send_mail(subject, message, from_email, recipient_list,
              fail_silently=False, auth_user=None, auth_password=None,
              connection=None, html_message=None):
        """
        Easy wrapper for sending a single message to a recipient list. All members
        of the recipient list will see the other recipients in the 'To' field.

        If auth_user is None, use the EMAIL_HOST_USER setting.
        If auth_password is None, use the EMAIL_HOST_PASSWORD setting.

        Note: The API for this method is frozen. New code wanting to extend the
        functionality should use the EmailMessage class directly.
        """
        connection = connection or get_connection(
           username=auth_user,
           password=auth_password,
           fail_silently=fail_silently,
        )
        mail = EmailMultiAlternatives(subject, message, from_email, recipient_list, connection=connection)
        if html_message:
            mail.attach_alternative(html_message, 'text/html')

        return mail.send()

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

@receiver(post_save, sender=CustomUser)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()