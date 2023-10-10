# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sphinx_rtd_theme
import sys,os

project = 'Generalised LR parsing algorithms'
copyright = '2023, xrtero'
author = 'xrtero'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
sys.path.append(os.path.abspath('myst_parser'))

extensions = ['myst_parser']


myst_enable_extensions = [
    "dollarmath",
    "html_image",
]


templates_path = ['_templates']
exclude_patterns = []




# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


html_static_path = ['_static']

source_suffix = {
  '.rst': 'restructuredtext',
  '.txt': 'markdown',
  '.md': 'markdown',
}