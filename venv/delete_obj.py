import boto3
import mysql
from mysql import connector

def deleteObject():
    mydb = mysql.connector.connect(
        host="95.9.218.53",
        user="root",
        password="kmt-6895",
        database="sharefile",
        port="30106"
    )
    mycursor = mydb.cursor()
    s3 = boto3.client('s3', region_name="us-east-2",
                      aws_access_key_id="AKIAUPMUVJIUAWXDFQ7B",
                      aws_secret_access_key="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")

    query = "select file_name from sharefile.deleting_obj"
    mycursor.execute(query)
    res = mycursor.fetchall()
    for x in res:
        print(x[0])
        s3.delete_object(Bucket="denizzzp12", Key=x[0])
        
if __name__ == '__main__':
    deleteObject()


