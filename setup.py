from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='pyTMCL',
      version='1.0.7',
      description='Talk to Trinamic Stepper Motors using TMCL over serial',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/LukeSkywalker92/pyTMCL',
      author='Lukas Scheffler',
      author_email='luke@lukecodewalker.de',
      license='MIT',
      classifiers=[
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 3",
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      packages=['pyTMCL'],
      install_requires=[
          'pyserial'
      ],
      keywords=[
          'tmcl',
          'trinamic',
          'rs485',
          'stepper',
          'motor',
          'tmcm'
      ],
      zip_safe=False)
