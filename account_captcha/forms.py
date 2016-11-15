from nocaptcha_recaptcha.fields import NoReCaptchaField

from account.forms import SignupForm

class ReCaptchaSignupForm(SignupForm):
    captcha = NoReCaptchaField()
