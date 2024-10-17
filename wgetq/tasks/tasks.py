from celery.task import task

from subprocess import check_call

#Default base directory 
#basedir="/data/static/"


#Example task
@task()
def add(x, y):
    """ Example task that adds two numbers or strings
        args: x and y
        return addition or concatination of strings
    """
    result = x + y
    return result

@task()
def wget(domain):
    result = check_call(['wget', '--mirror', domain])
    return result




