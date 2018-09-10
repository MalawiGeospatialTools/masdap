from nocaptcha_recaptcha.fields import NoReCaptchaField

from allauth.account.forms import SignupForm

class ReCaptchaSignupForm(SignupForm):
    captcha = NoReCaptchaField()
