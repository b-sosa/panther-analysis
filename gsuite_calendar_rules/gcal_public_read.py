def rule(event):
    return (event.udm("key") == "read" and event.udm("grantee") == "__public_principal__@public.calendar.google.com")

def title(event):
    return (f"{event.udm('share')} exposed their GSuite Calendar to the world")