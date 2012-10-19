import md5

def gravatar(email, width=220):
    hash = md5.new(email).hexdigest()
    url = "http://www.gravatar.com/avatar"
    return unicode("%s/%s?d=mm&s=%s" % (url, hash, width))