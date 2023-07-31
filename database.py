from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

def configure():
    load_dotenv()


configure()

db_connection_string = os.getenv('connection_string')
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

def load_job_from_db(id):
    with engine.connect() as conn:
        t = text('SELECT * FROM jobs WHERE id=:val')
        result = conn.execute(statement = t,  parameters=dict(val=id))
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()



def add_applications(job_id, data):
    with engine.connect() as conn:
        query = text("insert into applications (job_id, full_name, email, linked_in, Education, w_exp, resume_url) values (:job_id, :full_name, :email, :linked_in, :Education, :w_exp, :resume_url)")

        conn.execute(statement = query, parameters=dict(job_id=job_id, full_name=data['full_name'], email=data['email'], linked_in=data['linked_in'], Education=data['Education'], w_exp=data['w_exp'], resume_url=data['resume_url']))