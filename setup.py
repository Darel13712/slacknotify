from setuptools import setup

setup(name='slacknotify',
      version='0.1',
      description='Send notifications to slack from python',
      url='',
      author='Darel',
      author_email='darel142857@gmail.com',
      license='MIT',
      packages=['slacknotify'],
      install_requires=[
        'slackclient',
        'keyring'
    ],
      zip_safe=False)