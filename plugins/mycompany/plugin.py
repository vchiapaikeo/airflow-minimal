# This is the class you derive to create a plugin
from airflow.plugins_manager import AirflowPlugin


# Defining the plugin class
class AirflowTestPlugin(AirflowPlugin):
    name = "mycompany"
    hooks = []
    macros = []
