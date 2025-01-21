def apply_theme(theme_name):
    theme = Theme.objects.get(name=theme_name)
    return theme.color_scheme