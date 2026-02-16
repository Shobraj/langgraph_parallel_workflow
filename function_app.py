import azure.functions as func
from src.main import app as fastapi
import logging

app = func.AsgiFunctionApp(app = fastapi, function_name="langgraph_parallel_workflow", http_auth_level=func.AuthLevel.FUNCTION)