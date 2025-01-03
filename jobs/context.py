def menu_context(request):
    return {
    "menu": [
    {
        "title":"Companies",
        "url_name":"companies"
    },
    {
        "title":"Add publication",
        "url_name":"add_publication"
    },
    {
        "title":"Contacts",
        "url_name":"contacts"
    },
    {
        "title":"Login",
        "url_name":"login"
    },
    ]
}