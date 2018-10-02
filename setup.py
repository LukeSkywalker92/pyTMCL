from setuptools import setup

setup(name='pyTMCL',
      version='1.0.0',
      description='Talk to Trinamic Stepper Motors using TMCL over serial',
      url='https://github.com/LukeSkywalker92/pyTMCL',
      author='Alan Pich',
      author_email='luke@lukecodewalker.de',
      license='MIT',
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
