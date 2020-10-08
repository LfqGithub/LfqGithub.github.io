def response(method):
    if method=="post":
        return "/post"
    elif method=="get":
        return "/get"
    elif method=="head":
        return "/head"
    return "/"

def response_by_dict(method_dict,method):
    return method_dict.get(method,"/") # dict.get(key, default=None): if key do not exist, return default

def main():
    method_dict={
            "post":"/post",
            "get":"/get",
            "head":"head"
            }
    print(response(""))
    print(response_by_dict(method_dict,""))
if __name__=="__main__":
    main()
