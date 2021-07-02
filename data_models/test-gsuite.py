import panther_event_type_helpers as event_type
from panther_base_helpers import deep_get
from panther_base_helpers import gsuite_details_lookup as details_lookup

def get_event_type(event):
    if (event.get("name") == "change_calendar_acls"):
        if (event.get("parameters", "access_level") == "read"):
            if (event.get("parameters", "grantee_email") == "__public_principal__@public.calendar.google.com"):
                return event_type.GSUITETEST
    return None