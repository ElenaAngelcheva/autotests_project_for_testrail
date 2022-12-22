from voluptuous import Schema, Required, PREVENT_EXTRA, Optional,Any

CreatePprojectSchema = Schema({
    "id": int,
    Required('name'): str,
    "announcement": Any(str,None),
    "show_announcement": bool,
    "is_completed": bool,
    "completed_on": Any(str, None),
    "suite_mode": int,
    "default_role_id": Any(1, None),
    "url": str,
    "users": list,
    "groups": list

},
    required=False,
    extra=PREVENT_EXTRA
)
