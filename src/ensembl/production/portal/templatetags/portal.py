# See the NOTICE file distributed with this work for additional information
#   regarding copyright ownership.
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#       http://www.apache.org/licenses/LICENSE-2.0
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
import logging
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.template import Library
from jazzmin.settings import get_settings
from jazzmin.utils import make_menu
from jazzmin.templatetags import jazzmin
from jazzmin.templatetags.jazzmin import register
from typing import List, Dict

from ensembl.production.portal.models import AppView

User = get_user_model()
logger = logging.getLogger(__name__)

old_top_menu = jazzmin.get_top_menu


@register.simple_tag
def get_top_menu(user: AbstractUser, admin_site: str = "admin") -> List[Dict]:
    """
    Produce the menu for the top nav bar
    """
    options = get_settings()
    menu = make_menu(user, options.get("topmenu_links", []), options, admin_site=admin_site)
    children = [
        {"name": child.app_name, "url": child.get_admin_url(), "children": None}
        for child in AppView.objects.user_apps(user)
    ]
    menu.append(
        {
            "name": "Self Services",
            "url": "#",
            "children": children,
            "icon": options["default_icon_children"],
        }
    )
    return menu

# jazzmin.get_top_menu = get_ens_top_menu
