from py2exe import freeze

freeze(

  console = [{'script':'test2.py'}],

  options = {'py2exe': {'bundle_files': 1, 'compressed' : True}},

  zipfile = None

)