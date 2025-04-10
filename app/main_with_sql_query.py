from fastapi import FastAPI,Response,status,HTTPException, Depends
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models
from .database import engine, get_db


models.Base.metadata.create_all(bind = engine)

app = FastAPI()

"""def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()"""

"""@app.get("/")
async def root():
    return {"message": "Hello Akanksha"}"""

# request Get method url: "/"
class Post(BaseModel):
    title: str
    content: str
    published : bool = True
    #rating : Optional[int] = None
"""while True:
    try:
        conn = psycopg2.connect(host='akankshas-macbook-air.local', port = 55432, database='fastapi', 
                                user='postgres', password='postgres', cursor_factory=RealDictCursor)
        
        cursor = conn.cursor()
        print("Database connection was succesfull")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error:", error)
        time.sleep(2)"""
    

my_posts = [{"title": "Title of post 1", "content": "content of post 1", "id": 1},
            {"tilte": "favorite foods", "content": "I like pizza", "id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p ['id']==id:
            return i

@app.get("/")          
def root():
    return {"message": "Welcome to my API code."}

@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}


"""@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return {"status": "Success"}"""
    
@app.get("/posts")          
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}


"""@app.get("/posts")          # /this is a represent of path
def get_posts():
    cursor.execute(SELECT * FROM posts)
    posts = cursor.fetchall()
    return {"data": posts}
    return {"data": "This is your posts!!!"}"""


"""@app.get("/")          # agr path nhi denge to hmesa result phle wale ka ayega
def get_post():
    return {"data": "This is your posts!!!"}"""


"""@app.post("/createposts")        
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"message": "Succesfully created posts!"}"""


"""@app.post("/createposts")        
def create_posts(payLoad: dict = Body(...)):
    print(payLoad)
    return {"new_post": f"title: {payLoad['title']}, content : {payLoad['content']}"}
# title str, content str"""


"""@app.post("/createposts")        
def create_posts(new_post: Post):
    print(new_post.rating)    #  agr postman me rating nhi bhi likha hoga to wo bool value ka result None ayega.
    print(new_post.published)    #  agr postman me published nhi bhi likha hoga to wo bool value ka result true ayega.
    return {"Data": "New post!"}"""



"""@app.post("/posts")        
def create_posts(post: Post):
    print(post)
    print(post.model_dump_json()) #supported in new version of Fastapi
    print(post.dict()) # supported in old version of FastApi but deprecated in new version
    return {"Data": post}"""


@app.post("/posts",status_code=status.HTTP_201_CREATED)        
def create_posts(post: Post,db: Session = Depends(get_db)):
    #cursor.execute("""INSERT INTO posts (title,content,published)VALUES (%s, %s,%s) RETURNING * """,
    #              (post.title,post.content,post.published))
    #new_post = cursor.fetchone()
    #conn .commit()
    #new_post = models.Post(title=post.title, content=post.content, published=post.published)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"Data": new_post}

"""@app.post("/posts")        
def create_posts(post: Post):
    post_dict = post.dict() 
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"Data": post_dict}"""

@app.get("/post/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

"""@app.get("/posts/{id}")
def get_post(id: int,response: Response):    # str
    post = find_post(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f"post with id: {id} was not found"}
    return {"post_details": post}"""


@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    #ursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id)))
    #post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} was not found")
    return {"post_details": post}

@app.delete("/posts/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db)):
    #cursor.execute("""DELETE FROM posts WHERE id =%s returning * """, (str(id)))
    #deleted_post = cursor.fetchone()
    #conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id)
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exist")
    post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code= status.HTTP_204_NO_CONTENT)

"""@app.delete("/posts/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # deleting post
    # find the index in the array that has required ID
    # my_posts.pop(index)
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exist")
    my_posts.pop(index)
    # return {'message': 'post was succesfully deleted'}
    return Response(status_code= status.HTTP_204_NO_CONTENT)"""

@app.put("/posts/{id}")
def update_post(id:int, updated_post:Post, db: Session = Depends(get_db)):
    #cursor.execute("""UPDATE posts SET title =%s, content= %s, published=%s WHERE id = %s RETURNING * """, 
    #               (post.title,post.content,post.published,str(id)))
    #updated_post=cursor.fetchone()
    #conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post=post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exist")
    #post_query.update({'title': 'hey this is my updated title','content': 'hey this is my updated content'},synchronize_session=False)
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return {"data" : post_query.first()}
    #return {"data" : 'successfull'}

"""@app.put("/posts/{id}")
def update_post(id:int, post:Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"post with id: {id} does not exist")
    post_dict = post.dict()
    post_dict['id']=id
    my_posts[index]=post_dict
    return {"data" : post_dict}"""
    #return{'message':'update post'}


