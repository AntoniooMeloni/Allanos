<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Allanos - Sistema de Automação</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
            color: #333;
        }

        header {
            background-color: #004d99;
            color: #fff;
            padding: 20px 0;
            text-align: center;
        }

        header img {
            height: 60px;
            vertical-align: middle;
            margin: 0 10px;
        }

        header h1 {
            display: inline-block;
            vertical-align: middle;
            margin: 0;
            font-size: 2em;
        }

        main {
            max-width: 900px;
            margin: 30px auto;
            padding: 0 20px;
        }

        section {
            background-color: #fff;
            padding: 20px 30px;
            margin-bottom: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        h2 {
            color: #004d99;
        }

        code {
            background-color: #eee;
            padding: 2px 6px;
            border-radius: 4px;
            font-family: monospace;
        }

        pre {
            background-color: #eee;
            padding: 10px;
            border-radius: 6px;
            overflow-x: auto;
        }

        footer {
            text-align: center;
            padding: 20px;
            font-size: 0.9em;
            color: #666;
        }

        a {
            color: #004d99;
            text-decoration: none;
        }

        a:hover {
            text-decoration: underline;
        }

        .badges img {
            height: 30px;
            margin: 0 5px;
            vertical-align: middle;
        }
    </style>
</head>
<body>

<header>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0c/SENAI_logo.svg/256px-SENAI_logo.svg.png" alt="Logo SENAI">
    <h1>Allanos</h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d7/Android_robot.svg/120px-Android_robot.svg.png" alt="Logo Android">
</header>

<main>

    <section>
        <h2>Descrição</h2>
        <p>
            <strong>Allanos</strong> é um sistema de automação desenvolvido em <strong>Kotlin/Java</strong>, projetado para rodar em <strong>Raspberry Pi</strong> e outros dispositivos.
            Permite controlar dispositivos de forma inteligente, sendo ideal para projetos de automação residencial, escolar ou experimental.
        </p>
        <ul>
            <li>Controle automatizado de dispositivos</li>
            <li>Interface simples e intuitiva</li>
            <li>Código modular para fácil extensão</li>
            <li>Compatível com Raspberry Pi e sistemas Linux/Windows</li>
        </ul>
    </section>

    <section>
        <h2>Requisitos</h2>
        <ul>
            <li>Java 17 ou superior</li>
            <li>Gradle</li>
            <li>Sistema operacional Linux ou Windows</li>
            <li>Raspberry Pi (opcional)</li>
        </ul>
    </section>

    <section>
        <h2>Instalação</h2>
        <pre>
git clone https://github.com/AntoniooMeloni/Allanos.git
cd Allanos
./gradlew build
        </pre>
    </section>

    <section>
        <h2>Execução</h2>
        <h3>Usando Gradle</h3>
        <pre>
./gradlew run
        </pre>

        <h3>Usando JAR compilado</h3>
        <pre>
java -jar build/libs/allanos.jar
        </pre>
    </section>

    <section>
        <h2>Estrutura do Projeto</h2>
        <ul>
            <li>/src/main/kotlin - Código-fonte em Kotlin/Java</li>
            <li>/src/main/resources - Recursos (imagens, configurações)</li>
            <li>/build - Arquivos compilados pelo Gradle</li>
            <li>gradlew / gradlew.bat - Scripts para executar o Gradle</li>
        </ul>
    </section>

    <section>
        <h2>Contribuição</h2>
        <ol>
            <li>Fork o repositório</li>
            <li>Crie uma branch para sua feature: <code>git checkout -b minha-feature</code></li>
            <li>Faça commit das alterações: <code>git commit -m "Adicionando nova feature"</code></li>
            <li>Envie para o repositório remoto: <code>git push origin minha-feature</code></li>
            <li>Abra um Pull Request</li>
        </ol>
    </section>

</main>

<footer>
    🔧 Desenvolvido com ❤️ por <strong>Antônio A. Meloni</strong> | Licença MIT
</footer>

</body>
</html>
