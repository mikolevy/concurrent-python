import threading


def do_some_work():
    print(f'I am thread number: {threading.get_ident()} '
          f'and it is so hard work!')


thread = threading.Thread(target=do_some_work)
thread.start()
thread.join()

print(f'I am the main thread. My number is: {threading.get_ident()})'
      f'All work is done - bye bye!')
