from db.mongoConection import chats_collection

def getChatContext(user:str) -> dict:
    context = chats_collection.find_one({"user_id":user}, {"messages": {"$slice": -6}})
    if context and 'messages' in context:
        return [{"sender": msg["sender"], "message": msg["messages"]} for msg in context["messages"]]
    else:
        return None
