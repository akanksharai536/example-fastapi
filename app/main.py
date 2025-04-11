from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user,auth, vote
from .config import settings

print(settings.database_username)

#models.Base.metadata.create_all(bind = engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")          
def root():
    return {"message": "Welcome/Hello to my API code"}





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
"""class Post(BaseModel):
    title: str
    content: str
    published : bool = True"""
    #rating : Optional[int] = None

    
"""@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    return {"data": posts}"""


"""@app.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    return {"status": "Success"}"""

    
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


"""@app.post("/posts")        
def create_posts(post: Post):
    post_dict = post.dict() 
    post_dict['id'] = randrange(0,1000000)
    my_posts.append(post_dict)
    return {"Data": post_dict}"""

'''@app.get("/post/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return post'''

"""@app.get("/posts/{id}")
def get_post(id: int,response: Response):    # str
    post = find_post(id)
    if not post:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'message': f"post with id: {id} was not found"}
    return {"post_details": post}"""


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

