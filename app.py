from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import ConfigDict
from fastapi.responses import HTMLResponse

from model.form import Form
from model.submission import Submission
import store.forms
import store.submissions

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/static/js", StaticFiles(directory="static/js"), name="script")
templates = Jinja2Templates(directory="templates")

model_config = ConfigDict(arbitrary_types_allowed=True)
forms: store.forms = {}
submissions = store.submissions = {}


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "static": {}})

@app.post("/form")
def create_form(form: Form):
    formId = form.id
    forms[formId] = form
    return {"message": "form created successfully"}

@app.put("/form/{formId}")
def update_form(request: Request, formId: int, form: Form):
    if formId in forms:
        forms[formId] = form
        forms[formId].id = formId
        
        return {"message": "form updated successfully"}
    else:
        return {"message": "Invalid form"}

@app.get("/forms")
async def get_forms(request: Request, type: str = None):
    formsByType = {}
    if type == None:
        type = "all"
    if type != "all":
        for index,form in forms.items():
            if form.status == type:
                formsByType[index] = form
    else:
        formsByType = forms.copy()
        
    return list(formsByType.values())
    
    #return templates.TemplateResponse("list_forms.html", {"request": request, "forms": list(formsByType.values())})

@app.get("/form/{formId}")
def get_form(request: Request, formId: int):
    if formId in forms:
        form = forms[formId]
        if form.status != "published":
                form.actions = ['Edit', 'Publish', 'Delete']
        else:
            form.actions = ['Edit', 'Unpublish', 'Delete']

        return templates.TemplateResponse("form_detail.html", {"request": request, "form": form})
    else:
        return {"message": "Invalid form"}

@app.delete("/form/{formId}")
def delete_form(formId: int):
    if formId in forms:
        del forms[formId]
        return {"message": "form deleted successfully"}
    else:
        return {"message": "Invalid form"}
    
@app.put("/form/{formId}?action=publish")
def publish_form(formId: int):
    if formId in forms:
        forms[formId].status = 'published'
        return {"message": "form published successfully"}
    else:
        return {"message": "Invalid form"}
    
@app.put("/form/{formId}?action=unpublish")
def unpublish_form(formId: int):
    if formId in forms:
        forms[formId].status = 'draft'
        return {"message": "form unpublished successfully"}
    else:
        return {"message": "Invalid form"}
    
@app.put("/form/{formId}/submission")
def submit_form(formId: int, submission: Submission):
    if formId in forms:
        form = forms[formId]
        if form.status == 'published':
            if(submissions.get(formId) == None):
                submissions[formId] = []
            submissions[formId].append(submission)
            return {"message": "form published successfully"}
        else:
            return {"message": "form not yet published"}
    else:
        return {"message": "Invalid form"}
    