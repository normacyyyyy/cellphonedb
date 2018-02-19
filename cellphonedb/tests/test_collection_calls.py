import pandas as pd

from cellphonedb.flask_app import create_app
from cellphonedb.extensions import cellphonedb_flask
from cellphonedb.flask_terminal_collector_launcher import FlaskTerminalCollectorLauncher
from cellphonedb.tests.cellphone_flask_test_case import CellphoneFlaskTestCase


class TestCollectionCalls(CellphoneFlaskTestCase):

    def test_collect_data(self):
        cellphonedb_flask.cellphonedb.database_manager.database.drop_everything()
        cellphonedb_flask.cellphonedb.database_manager.database.create_all()

        self.check_proteins()
        self.check_genes()
        self.check_complex()
        self.check_interaction()

    def check_proteins(self):
        self.collect_data('protein')
        self.assert_number_data('protein')

        proteins_expected = pd.read_csv('{}/{}'.format(self.fixtures_dir(), 'collect_protein.csv'))
        multidatas_db = cellphonedb_flask.cellphonedb.database_manager.get_repository('multidata').get_all()

        self.assertEqual(len(proteins_expected), len(multidatas_db),
                         'Database collected multidata (from proteins) didnt match')

    def check_genes(self):
        self.collect_data('gene')
        self.assert_number_data('gene')

    def check_complex(self):
        self.collect_data('complex')
        self.assert_number_data('complex')

    def check_interaction(self):
        self.collect_data('interaction')
        self.assert_number_data('interaction')

    def assert_number_data(self, name):
        namefile = 'collect_{}.csv'.format(name)

        db_data = cellphonedb_flask.cellphonedb.database_manager.get_repository(name).get_all()

        expected_data = pd.read_csv('{}/{}'.format(self.fixtures_dir(), namefile))
        self.assertEqual(len(db_data), len(expected_data), 'Database collected {} didnt match'.format(name))

    def collect_data(self, name):
        namefile = 'collect_{}.csv'.format(name)
        getattr(FlaskTerminalCollectorLauncher(), name)(namefile, self.fixtures_dir())

    def create_app(self):
        return create_app(environment='test')
