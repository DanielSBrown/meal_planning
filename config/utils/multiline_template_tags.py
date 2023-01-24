# This is a hack to allow multiline template tags, which Django won't do:
# https://code.djangoproject.com/ticket/8652
#
# It is pulled from Zach Snow's answer to this SO post:
# https://stackoverflow.com/questions/49110044/django-template-tag-on-multiple-line

import re

from django.template import base


def allow_multiline_template_tags():
    base.tag_re = re.compile(base.tag_re.pattern, re.DOTALL)
