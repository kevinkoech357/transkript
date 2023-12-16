from celery import Celery


def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config["CELERY_BROKER_URL"],
        backend=app.config["CELERY_RESULT_BACKEND"],
    )

    celery.config_from_object(app.config, namespace="CELERY")

    return celery
