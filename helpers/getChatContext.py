from db.mongoConection import chats_collection

def getChatContext(user:str) -> dict:
    context = chats_collection.find_one({"user_id":user}, {"messages": {"$slice": -6}})
    if context:
        return str(context)
    else:
        return None
