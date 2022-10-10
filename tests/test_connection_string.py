import unittest

from tap_mongodb import get_connection_string


class TestConnectionString(unittest.TestCase):
    def setUp(self):
        self.config = {
            "host": "dummy-host",
            "user": "dummy-user",
            "password": "dummy-password",
            "auth_database": "dummy-auth-database",
            "database": "dummy-databse",
            "port": "2017"
        }

    def test_minimal_config(self):
        expected_default_string = "mongodb://dummy-user:dummy-password@dummy-host:2017/dummy-databse?readPreference=secondaryPreferred&authSource=dummy-auth-database&authMechanism=SCRAM-SHA-256"
        expected_srv_string = "mongodb+srv://dummy-user:dummy-password@dummy-host/dummy-databse?readPreference=secondaryPreferred&authSource=dummy-auth-database&authMechanism=SCRAM-SHA-256"

        connection_string = get_connection_string(self.config)
        self.assertEqual(expected_default_string, connection_string)

        self.config["srv"] = "true"
        connection_string = get_connection_string(self.config)
        self.assertEqual(expected_srv_string, connection_string)


    def test_replica_set_config(self):
        self.config["replica_set"] = "dummy-replica-set"

        expected_default_string = "mongodb://dummy-user:dummy-password@dummy-host:2017/dummy-databse?readPreference=secondaryPreferred&authSource=dummy-auth-database&replicaSet=dummy-replica-set&authMechanism=SCRAM-SHA-256"
        expected_srv_string = "mongodb+srv://dummy-user:dummy-password@dummy-host/dummy-databse?readPreference=secondaryPreferred&authSource=dummy-auth-database&replicaSet=dummy-replica-set&authMechanism=SCRAM-SHA-256"

        connection_string = get_connection_string(self.config)
        self.assertEqual(expected_default_string, connection_string)

        self.config["srv"] = "true"
        connection_string = get_connection_string(self.config)
        self.assertEqual(expected_srv_string, connection_string)


    def test_strict_ssl_config(self):
        self.config["ssl"] = "true"

        expected_default_string = "mongodb://dummy-user:dummy-password@dummy-host:2017/dummy-databse?readPreference=secondaryPreferred&authSource=dummy-auth-database&tls=true&authMechanism=SCRAM-SHA-256"
        expected_srv_string = "mongodb+srv://dummy-user:dummy-password@dummy-host/dummy-databse?readPreference=secondaryPreferred&authSource=dummy-auth-database&tls=true&authMechanism=SCRAM-SHA-256"

        connection_string = get_connection_string(self.config)
        self.assertEqual(expected_default_string, connection_string)

        self.config["srv"] = "true"
        connection_string = get_connection_string(self.config)
        self.assertEqual(expected_srv_string, connection_string)

    def test_strict_ssl_config_bools(self):
        self.config["ssl"] = True

        expected_default_string = "mongodb://dummy-user:dummy-password@dummy-host:2017/dummy-databse?readPreference=secondaryPreferred&authSource=dummy-auth-database&tls=true&authMechanism=SCRAM-SHA-256"
        expected_srv_string = "mongodb+srv://dummy-user:dummy-password@dummy-host/dummy-databse?readPreference=secondaryPreferred&authSource=dummy-auth-database&tls=true&authMechanism=SCRAM-SHA-256"

        connection_string = get_connection_string(self.config)
        self.assertEqual(expected_default_string, connection_string)

        self.config["srv"] = True
        connection_string = get_connection_string(self.config)
        self.assertEqual(expected_srv_string, connection_string)


    def test_weak_ssl_config(self):
        self.config["ssl"] = "true"
        self.config["verify_mode"] = "false"

        expected_default_string = "mongodb://dummy-user:dummy-password@dummy-host:2017/dummy-databse?readPreference=secondaryPreferred&authSource=dummy-auth-database&tls=true&tlsAllowInvalidCertificates=true&authMechanism=SCRAM-SHA-256"
        expected_srv_string = "mongodb+srv://dummy-user:dummy-password@dummy-host/dummy-databse?readPreference=secondaryPreferred&authSource=dummy-auth-database&tls=true&tlsAllowInvalidCertificates=true&authMechanism=SCRAM-SHA-256"

        connection_string = get_connection_string(self.config)
        self.assertEqual(expected_default_string, connection_string)

        self.config["srv"] = "true"
        connection_string = get_connection_string(self.config)
        self.assertEqual(expected_srv_string, connection_string)

    def test_weak_ssl_config_bools(self):
        self.config["ssl"] = True
        self.config["verify_mode"] = False

        expected_default_string = "mongodb://dummy-user:dummy-password@dummy-host:2017/dummy-databse?readPreference=secondaryPreferred&authSource=dummy-auth-database&tls=true&tlsAllowInvalidCertificates=true&authMechanism=SCRAM-SHA-256"
        expected_srv_string = "mongodb+srv://dummy-user:dummy-password@dummy-host/dummy-databse?readPreference=secondaryPreferred&authSource=dummy-auth-database&tls=true&tlsAllowInvalidCertificates=true&authMechanism=SCRAM-SHA-256"

        connection_string = get_connection_string(self.config)
        self.assertEqual(expected_default_string, connection_string)

        self.config["srv"] = True
        connection_string = get_connection_string(self.config)
        self.assertEqual(expected_srv_string, connection_string)

    def test_uri_config(self):
        self.config["uri"] = "mongodb://dummy-user:dummy-password@dummy-host:2017/dummy-databse?authSource=dummy-auth-database&tls=true&tlsAllowInvalidCertificates=true"

        expected_default_string = "mongodb://dummy-user:dummy-password@dummy-host:2017/dummy-databse?authSource=dummy-auth-database&tls=true&tlsAllowInvalidCertificates=true"

        connection_string = get_connection_string(self.config)
        self.assertEqual(expected_default_string, connection_string)
