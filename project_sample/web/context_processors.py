import logging

from django.conf import settings


logger = logging.getLogger(__name__)


def custom_context_processors(request):
    response = {
        'site_name': settings.SITE_NAME,
        'menu': settings.MENU_ITEMS,
    }
    logger.info(response)
    return response
