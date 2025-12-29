def routes():
    def route(req=None, route=None):
        
        if route == None:
            return f"{req} / HTTP/1.1"
        else:
            return f"{req} {route} HTTP/1.1"

    return {
        route("GET"):"Escolha uma página",
        route("GET","/home"): {"Bem vindo a tela principal!"},
        route("GET","/users"): users(),
        route("GET","/carrinho"): carrinho(),
        route("GET","/saudacao"): "Olá Brasil!",
    }

def users():
    return {
    "Bruno":{
        "Sobrenome": "Barcelos",
        "Idade": 25
    },
    "Matheus":{
        "Sobrenome": "Lopes",
        "Idade": 23
    }
}

def carrinho():
    return {
    "carrinho": {
        "Banana": {
            "categoria": "Fruta",
            "valor": 10
        },
        "Açucar": {
            "categoria": "Cereal",
            "valor": 10
        },
        "Batata": {
            "categoria": "Verdura",
            "valor": "5"
        }
    }
}

def name_routes():
    return list(routes().keys())


