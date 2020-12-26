from typing import List
from sqlalchemy import Column,Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()
engine = create_engine('mysql://root:kmt-6895@95.9.218.53:30106/sharefile')
Base.metadata.create_all(engine)


class UploadInfo(Base):
    __tablename__="share_file"

    secret_key=Column(String(50),primary_key=True)
    secret_file = Column(String(50))
    original_file = Column(String(50))
    insert_date = Column(DateTime)
    delete_date = Column(DateTime)
    size = Column(Integer)
    IP= Column(String(25))

class download(Base):
    __tablename__="download_info"
    ip = Column(String(25),primary_key=True)
    size = Column(Integer,primary_key=True)

class expiretimeFiles(Base):
    __tablename__= "deleting_obj"

    file_name=Column(String(50),primary_key=True)


def insert(secret_key,secret_file,original_file,insert_date,delete_date,size,IP):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    info =UploadInfo(secret_key=secret_key, secret_file=secret_file, original_file=original_file, insert_date=insert_date,
                      delete_date=delete_date, size=size, IP=IP)
    session.add(info)
    session.commit()

def select(param):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    for instance in session.query(UploadInfo).filter(UploadInfo.secret_key==param):
        original_file = instance.original_file
        secret_file =instance.secret_file
        size = instance.size

    return original_file,secret_file,size

def downloadInsert(ip,size):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    session.add(download(ip=ip,size=size))
    session.commit()
    return "OK"

def truncateTable() -> List:
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    table = []
    for res in session.query(expiretimeFiles):
        table.append(res.file_name)
    session.query(expiretimeFiles).delete()
    session.commit()
    return table



















