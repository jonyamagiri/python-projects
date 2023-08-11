#!/usr/bin/env python3

def email_slicer(email):
    username, domain_part = email.split('@')
    domain_parts = domain_part.split('.')
    domain = '.'.join(domain_parts[:-1])  # Join all parts except the last one
    extension = domain_parts[-1]  # Last part is the extension
    return username, domain, extension

def main():
    print('Welcome to the email slicer')
    
    while True:
        user_email = input('\nEnter your email address (or type "exit" to quit): ')
        
        if user_email.lower() == 'exit':
            print('Exiting the program. Goodbye!')
            break
        
        username, domain, extension = email_slicer(user_email)
        
        print('\nUsername:', username)
        print('Domain:', domain)
        print('Extension:', extension)

if __name__ == '__main__':
    main()



# #!/usr/bin/env python3

# def main():
#     print('Welcome to the email slicer')
#     print('')

#     user_email = input('Enter your email address: ')

#     (username, domain) = user_email.split('@')
#     (domain, extension) = domain.split('.')

#     print('Username: ', username)
#     print('Domain: ', domain)
#     print('Extension: ', extension)

# while True:
#     main()

# collect email from user
# split the email using @, the first saved as the username, the second part is the domain
# split the domain at . to get the domain name and extension
