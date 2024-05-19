from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
import pytz
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
import logging

logger = logging.getLogger(__name__)

class RedirectMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.is_superuser:
            if request.get_full_path() == "/":
                if (
                        hasattr(request.user, "member")
                        and request.get_full_path().startswith(settings.HOME_URL)
                        is False
                ):
                    logger.debug(f'Redirecting to {settings.HOME_URL}')
                    return HttpResponseRedirect(settings.HOME_URL)
        #else:
        elif not request.user.is_superuser:  # Add this condition to redirect to login page if user is not authenticated
            logger.debug(f'User authenticated: {request.user.is_authenticated}')
            logger.debug(f'User is superuser: {request.user.is_superuser}')
            logger.debug(f'Current path: {request.get_full_path()}')
            if not request.get_full_path().startswith(tuple(settings.LOGIN_REQUIRED_IGNORE_PATHS)):
                logger.debug(f'Redirecting to {settings.LOGIN_URL}')
                return HttpResponseRedirect(settings.LOGIN_URL)
        response = self.get_response(request)
        return response


class TimezoneMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        tzname = request.session.get("django_timezone")
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response
