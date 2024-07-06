
# 2° Definição de args:

options = {
    # O dono da DAG. É útil para identificar quem é responsável pela DAG. (Obrigatorio)
    'owner': 'seu_nome',
    # Se True, a tarefa só será executada se a tarefa anterior no DAG tiver sido concluída com sucesso.
    'depends_on_past': False,
    # Data de início da DAG. Pode ser uma data fixa ou dinâmica.           (Obrigatorio)
    'start_date': datetime(2023, 7, 1),
    # Lista de e-mails para notificação em caso de falha.
    'email': ['seu_email@dominio.com'],
    # Se True, envia um e-mail quando a tarefa falha.
    'email_on_failure': True,
    # email_on_retry: Se True, envia um e-mail quando a tarefa é reexecutada.
    'email_on_retry': False,
    # Número de tentativas de reexecução em caso de falha.   (Obrigatorio)
    'retries': 1,
    # Tempo de espera entre tentativas de reexecução.        (Obrigatorio)
    'retry_delay': timedelta(minutes=5),
    # Se essa opção estiver ligada (True), Para dar um tempo ao problema da internet se resolver.
    'retry_exponential_backoff': True,
    #  Tempo máximo de espera entre tentativas de reexecução.
    'max_retry_delay': timedelta(minutes=30),
    #  Tempo máximo de execução da tarefa antes de ser marcada como falha.
    'execution_timeout': timedelta(hours=1),
    #  Tempo máximo de execução do DAG antes de ser marcado como falha.
    'dagrun_timeout': timedelta(hours=2),
    # Se True, a DAG será executada para intervalos perdidos desde a última execução.
    'catchup': False,
    # max_active_runs: Número máximo de execuções ativas do DAG simultaneamente.
    'max_active_runs': 1,
    # Tempo máximo permitido para a tarefa ser concluída.
    'sla': timedelta(hours=1),
    # Peso de prioridade da tarefa para a fila de execução.
    'priority_weight': 10,
    # Nome da fila em que a tarefa deve ser executada.
    'queue': 'default',
    #  Nome do pool de recursos onde a tarefa deve ser executada.
    'pool': 'default_pool',
    # Define em que condições a tarefa será executada.
    'trigger_rule': 'all_success',
}


# 3° Dag:
dag = DAG(
    # O identificador único da DAG. (Obrigatorio)
    dag_id='nome_da_sua_dag',
    # Dicionário com os argumentos padrão da DAG, como discutimos antes. (Obrigatorio)
    default_args=options,
    # Descrição opcional da DAG.
    description='Descrição da sua DAG',
    # Intervalo de agendamento para executar a DAG. Pode ser uma string cron-like ou um objeto timedelta para intervalos simples. (Obrigatorio)
    schedule_interval=timedelta(days=1),
    # Lista de tags associadas à DAG para categorização.
    tags=['etl', 'dados'],
    # Número máximo de tarefas que podem ser executadas simultaneamente por esta DAG.
    concurrency=1,
    # Número máximo de execuções ativas desta DAG simultaneamente.
    max_active_runs=1,
    # Define se a DAG deve retroceder e executar tarefas para os intervalos que perdeu enquanto estava desativada.
    catchup=False,
    # Define a visualização padrão para o painel Airflow.
    default_view='tree',
    # A orientação da DAG no painel Airflow (LR para esquerda para direita, TB para cima para baixo).
    orientation='LR',
    # Data de início da DAG. Pode ser uma data fixa ou uma função como days_ago() para iniciar a DAG a partir de um certo número de dias atrás.
    start_date=datetime(2023, 7, 1),
    # Fuso horário utilizado para agendamento e timestamps na DAG.
    timezone='America/Sao_Paulo',
    # Função de callback chamada quando uma tarefa da DAG falha em atender ao SLA.
    sla_miss_callback=sla_miss_callback_function

)
