from sqlalchemy import create_engine, text


db_connection_string = "mysql+pymysql://niumqrh75jjh6ctnveb4:pscale_pw_mvXaozo5wtPvR7P9oRB6L5wbXajOanTQ8TLoTZiS6tw@aws.connect.psdb.cloud/kolkars_careers?charset=utf8mb4"
engine = create_engine(db_connection_string,
                       connect_args = {
                           "ssl" : {
                               "ssl_ca": "/etc/ssl/cert.pem"
                           }
                       }
                       )

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        
        result_all = result.all()
        jobs = []
        for row in result_all:
            jobs.append(row._asdict())
        return jobs






# database: kolkars_careers
# username: niumqrh75jjh6ctnveb4
# host: aws.connect.psdb.cloud
# password: pscale_pw_mvXaozo5wtPvR7P9oRB6L5wbXajOanTQ8TLoTZiS6tw