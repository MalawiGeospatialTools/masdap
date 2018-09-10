from django.http import HttpResponse

from allauth.account.views import SignupView
from allauth.account import signals

from account_captcha.forms import ReCaptchaSignupForm

class SignupViewCaptcha(SignupView):
    form_class = ReCaptchaSignupForm    

    def form_invalid(self, form):

        signals.user_sign_up_attempt.send(
            sender=ReCaptchaSignupForm,
            username=form.data.get("username"),
            email=form.data.get("email"),
            result=form.is_valid()
        )
        return super(SignupView, self).form_invalid(form)

    def after_signup(self, form):
        signals.user_signed_up.send(sender=ReCaptchaSignupForm, user=self.created_user, form=form)

