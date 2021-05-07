from setuptools import setup, find_packages
discord_name = 'skelly386#1410'
discord_server_inv = 'https://discord.com/invite/WhnmkwgtGb'


classifiers = [
    'Development Status :: 3',
    'Intended Audience :: Anime',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8'
]

setup(
    name='anime_images_api',
    version='0.0.1',
    description='a wrapper for the anime images api',
    long_description=open('README.md').read() + '\n\n' +
    open('CHANGELOG.md').read(),
    url=discord_server_inv,
    author=discord_name,
    author_email='skellymclane@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['python', 'image', 'anime', 'api', 'wrapper', 'py'],
    packages=find_packages(),
    install_requires=['download', 'rich']
)
