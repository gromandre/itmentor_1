def main():
    d = {'website': 'google', 'url': 'google.com'}

    try:
        data = d['url']
    except:
        data = 'https://'
        print('Inside except', data)
        return data
    else:
        data = data.upper()
    print(data)

main()