from setuptools import setup, find_packages
from os.path import dirname, abspath, join

ROOT = dirname(abspath(__file__)) + '\\'

def get_extra_requires(path):
    extra_deps = []
    with open(path) as fp:
        for p in fp.readlines():
            extra_deps.append(p.replace("\n",""))
    return extra_deps

setup(
    name='asset_behave_api',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/lealvjo/asset_behave_api',
    license='',
    author='lealvjo',
    author_email='leonardo.jose.barros@hotmail.com',
    description='Example of how to automate API, using python and behavior-oriented development (BDD)',
    platforms='any',
    install_requires=get_extra_requires(join(ROOT,"requirements.txt")),
    entry_points={
        "console_scripts": [
            "asset_behave_api=app_b.main:main"
        ]},
    package_data={'' : [join(ROOT, 'app_b/features/excluir_jogo.feature')]}
)