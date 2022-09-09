def slice_email(email):
    (username, domain) = email.split('@')
    (domain, extension) = domain.split('.')
    print('Username : '+username)
    print('Domain : '+domain)
    print('Extension : .'+extension)

email = input('Enter your email : ')

slice_email(email)