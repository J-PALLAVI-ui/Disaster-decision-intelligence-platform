import psycopg2


def get_connection():

    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="disaster_decision_intelligence",
        user="postgres",
        password="aks@123" 
    )

    return connection