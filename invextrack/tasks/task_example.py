from celery import shared_task

@shared_task
def exemple_task(param):
    """
    Tâche d'exemple asynchrone.
    :param param: Paramètre de la tâche
    :return: Message de réussite
    """
    print(f"Exécution de la tâche avec le paramètre : {param}")
    return f"Tâche terminée avec le paramètre : {param}"