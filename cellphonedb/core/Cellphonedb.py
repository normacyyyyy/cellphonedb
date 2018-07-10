import os

from cellphonedb.core.collectors.collector import Collector
from cellphonedb.core.exporters.exporterlauncher import ExporterLauncher
from cellphonedb.core.methods.querylauncher import QueryLauncher
from cellphonedb.core.database import DatabaseManager

cellphone_core_dir = os.path.dirname(os.path.realpath(__file__))
data_dir = '{}/data'.format(cellphone_core_dir)

data_test_dir = '{}/tests/fixtures'.format(cellphone_core_dir)


class Cellphonedb(object):
    def __init__(self, database_manager: DatabaseManager):
        self.database_manager = database_manager
        self.export = ExporterLauncher(self.database_manager)
        self.collect = Collector(self.database_manager)
        self.query = QueryLauncher(self.database_manager)
