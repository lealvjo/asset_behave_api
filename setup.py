from setuptools import setup, find_packages
from os.path import dirname, abspath, join

ROOT = dirname(abspath(__file__))

def get_extra_requires(path):
    extra_des = []
    with open(path) as fp:
        for p in fp.readlines():
            extra_des.append(p.replace("\n", ""))
    return extra_des

setup(
    name='asset_behave_api',
    version='1.1.1',
    packages=find_packages(),
    url='https://github.com/lealvjo/asset_behave_api',
    license='',
    author='lealvjo',
    author_email='leonardo.jose.barros@hotmail.com',
    description='Example of how to automate API, using python and behavior-oriented development (BDD)',
    platforms='any',
    install_requires=get_extra_requires(join(ROOT, "requirements.txt")),
    entry_points={
        "console_scripts": [
            "asset_behave_api_run=app_b.main:main"
        ]},
    package_data={'' : [join(ROOT, 'app_b/features/*.feature'),
        join(ROOT, 'app_b/features/schema/data_order.json')
        , join(ROOT, 'app_b/features/stage/environment.yml')
        , join(ROOT, 'app_b/features/behave.ini')
        ]}
)