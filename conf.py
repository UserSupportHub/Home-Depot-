# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Manage Your Home Depot Credit Card'
copyright = '2025, The Home Depot'
author = 'The Home Depot'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "HomeDepot.com/MyCard – Manage Your Home Depot Credit Card Online"

# Optional short title (e.g., for nav bar)
html_short_title = "Home Depot MyCard"

# Favicon (optional)
html_favicon = 'favicon.ico'

# Choose a theme (uncomment if you have one installed)
# html_theme = 'sphinx_rtd_theme'

# Hide "View page source" link
html_show_sourcelink = False

# Allow raw HTML in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Paths to static files like CSS or images
# html_static_path = ['_static']  # Uncomment if using static assets like logo/favicon

# -- Custom HTML meta (inserted via layout.html) -----------------------------
# If you want meta tags for SEO, edit the layout.html in _templates and use:
# {% block extrahead %}<meta name="description" content="...">{% endblock %}
