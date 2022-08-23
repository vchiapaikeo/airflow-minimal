from airflow.models.baseoperator import BaseOperator


# Should import python-nomad library and perform commands necessary to interact with nomad
class NomadOperator(BaseOperator):
    def __init__(self, name: str, **kwargs) -> None:
        super().__init__(**kwargs)
        self.name = name

    def execute(self, context):
        message = f"Hello {self.name}"
        print(message)
        return message
