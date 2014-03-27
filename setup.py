from vyperlogix.py2exe import setup

__target__ = r'C:\@vm1\pakbuilder'

minion = setup.CopyFilesToTarget(__target__)

setup.do_setup(
    program_name='pakbuilder',
    company_name='VyperLogix Corp.',
    product_name='VyperLogix PAK Builder',
    description='VyperLogix PAK Builder',
    product_version='1.3.0.0',
    icon='VyperLogixCorp.ico',
    callback=minion.callback,
    collector=setup.VyperLogixLibraryZipsCollector,
    dist_dir='./dist',
    packages=['paramiko'],
    packagedir={ 'Crypto':'C:/Python27/Lib/site-packages/Crypto',
                 'paramiko':'C:/Python27/Lib/site-packages/paramiko-1.10.1-py2.7.egg/paramiko'
                 },
    datafiles=[ ('.', ['README.md']), ('.', ['LICENSE']) ],
    data_files=[],
    compiled_excludes=['boto','requests','web','simplejson','json','wsgiref']
)
