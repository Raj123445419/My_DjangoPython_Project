from .models import sidata

class UserSessionSyncMiddleware:
    """
    Middleware to ensure session data (country, fullname, phone, email) 
    is ALWAYS in sync with the database (sidata model) in real-time.
    If an admin updates the user's country in Django admin or backend,
    all views and templates will instantly see the updated country.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        email = request.session.get('email')
        fullname = request.session.get('fullname')
        phone = request.session.get('phone')

        user = None
        if email:
            user = sidata.objects.filter(email__iexact=email).first()
        if not user and fullname:
            user = sidata.objects.filter(Fullname=fullname).first()
        if not user and phone:
            user = sidata.objects.filter(phonnumber=phone).first()

        if user:
            # Sync fresh values from database into session
            if user.country:
                request.session['country'] = user.country.strip()
            request.session['fullname'] = user.Fullname
            request.session['email'] = user.email
            request.session['phone'] = user.phonnumber
            request.session['profile_pic_url'] = user.profile_pic.url if user.profile_pic else ''
            request.user_obj = user
        else:
            request.user_obj = None

        response = self.get_response(request)
        return response
