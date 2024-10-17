from subprocess import check_call
from celery import Celery
import celeryconfig

app = Celery()
app.config_from_object(celeryconfig)

#Example task
@app.task()
def add(x, y):
    """ Example task that adds two numbers or strings
        args: x and y
        return addition or concatination of strings
    """
    result = x + y
    return result


@app.task()
def wget(domain):
    """ Mirror a sites content
        args: domain
    """
    result = check_call(['wget', '--mirror', domain])
    return result




