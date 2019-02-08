def page_not_found(e):
    # note that we set the 404 status explicitly
    return "Page not found", 404

def page_500(e):
    
    return "Something went wrong", 500

def create_404_response(name):
    message = {"message" :f"{name} not found" } 
    status = 404
    return message, status