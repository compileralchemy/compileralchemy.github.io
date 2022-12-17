from livereload import Server, shell

server = Server()
server.watch('.')
server.serve(open_url_delay=1)