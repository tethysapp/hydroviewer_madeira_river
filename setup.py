from setuptools import setup, find_namespace_packages
from setup_helper import find_resource_files

# -- Apps Definition -- #
app_package = 'hydroviewer_madeira_river'
release_package = 'tethysapp-' + app_package
resource_files = find_resource_files('tethysapp/' + app_package + '/scripts', 'tethysapp/' + app_package)

# -- Python Dependencies -- #
dependencies = []

# -- Get Resource File -- #
resource_files = find_resource_files('tethysapp/' + app_package + '/templates', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/public', 'tethysapp/' + app_package)

setup(
    name=release_package,
    version='1',
    description='This app evaluates the accuracy for the historical streamflow values obtained from Streamflow Prediction Tool in Madeira River Basin.',
    long_description='',
    keywords='Historical Validation Tool',
    author='Jorge Luis Sanchez-Lozano, Chris Edwards, Anna Cecil, Tessa Muir',
    author_email='jorgessanchez7@gmail.com, chris3edwards3@gmail.com, anna.cecil1999@gmail.com, tessmuir16@gmail.com',
    url='',
    license='',
    packages=find_namespace_packages(),
    package_data={'': resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
)
