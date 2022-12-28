from .atri import Atri
from fastapi import Request, Response

def init_state(at: Atri):
    at.Bar1.custom.data = [{"x":2010, "category1":40, "category2":50}, 
                           {"x":2011, "category1":30, "category2":60}]

def handle_page_request(at: Atri, req: Request, res: Response):
    pass

def handle_event(at: Atri, req: Request, res: Response):
    pass