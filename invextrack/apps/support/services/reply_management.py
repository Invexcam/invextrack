from ..models.reply import Reply

def create_reply(ticket, text):
    reply = Reply.objects.create(ticket=ticket, text=text)
    return reply

def delete_reply(reply_id):
    reply = Reply.objects.get(id=reply_id)
    reply.delete()