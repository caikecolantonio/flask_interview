## Sobre o projeto

Projeto está usando uma venv com todos os Modulos usados adicionados no Pipfile.
Para fazer migrações no banco de dados eu utilizei o flask_migrate.
Para a serialização usei o Marshmallow.

```
flask run
```

Todos os testes de API foram feitos usando o Postman. 

Para adicionar dados aos Usuarios use a url:

```
localhost/cadastrar
```

Um método GET que precisa ser enviado 3 paramêtros em um dicionario exemplo:

```
{
    "nome_completo": "frank castle",
    "cpf": "229.883.058-83",
    "email": "frankcastle@gmail.com"
}
```
ps: eu enviei os dados usando o Postman, como um GET e mandei o body como um raw com o dicionario acima e o tipo de arquivo JSON.

Para mostrar os dados dos usuarios:

```
localhost/mostrar
```

Para deletar os dados dos usuarios, onde o identificador é o id do usuario:

```
localhost/deletar/id_usuario
```

Para alterar dados do usuario também tem que ser enviado como o dicionario para adicionar a diferença é que não é um método GET e sim PATCH. URL: 

```
localhost/modificar/id_usuario
```

