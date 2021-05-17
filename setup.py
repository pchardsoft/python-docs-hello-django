from setuptools import setup

setup(
  name = 'DAS_finance',         # How you named your package folder (TSIClient)
  packages = ['DAS_finance'],   # Chose the same as "name"
  version = '1.0.0',      # Start with a small number and increase it with every change you make
  #license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  #long_description=long_description,
  #long_description_content_type='text/markdown',  # This is important!
  author = 'Javier González',                   # Type in your name
  author_email = 'javier@informaticos.com',      # Type in your E-Mail
  url = 'https://github.com/pchardsoft/python-docs-hello-django',   # Provide either the link to your github or to your website
  #download_url = 'https://github.com/RaaLabs/TSIClient/archive/v_0.7.tar.gz',    # If you create releases through Github, then this is important
  #keywords = ['Time Series Insight', 'TSI', 'TSI SDK'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
  #        'requests',
   #       'pandas'
      ],
  classifiers=[
   # 'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
   # 'Intended Audience :: Developers',      # Define that your audience are developers
   # 'Topic :: Software Development :: Build Tools',
   # 'License :: OSI Approved :: MIT License',   # Again, pick a license
   # 'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
   # 'Programming Language :: Python :: 3.4',
   # 'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.8',
  ],
)