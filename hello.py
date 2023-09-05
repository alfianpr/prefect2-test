from prefect import flow, task

@task
def create_message():
    msg = "hello, prefect!"
    return msg

@flow
def hello_world():
    return print(create_message())


if __name__ == "__main__":
    hello_world()