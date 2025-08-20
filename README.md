<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Allanos - Sistema de Automação</title>
<style>
    body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        background-color: #f0f2f5;
        margin: 0;
        padding: 0;
        color: #333;
    }

    header {
        background-color: #004d99;
        color: white;
        text-align: center;
        padding: 20px;
    }

    header img {
        height: 50px;
        vertical-align: middle;
        margin: 0 10px;
    }

    header h1 {
        display: inline-block;
        vertical-align: middle;
        font-size: 2em;
        margin: 0;
    }

    main {
        max-width: 800px;
        margin: 30px auto;
        padding: 0 20px;
    }

    section {
        background-color: white;
        padding: 20px 25px;
        margin-bottom: 20px;
        border-radius: 10px;
        box-shadow: 0 3px 8px rgba(0,0,0,0.1);
    }

    h2 {
        color: #004d99;
        margin-top: 0;
    }

    pre {
        background-color: #eee;
        padding: 10px;
        border-radius: 6px;
        overflow-x: auto;
        font-size: 0.95em;
    }

    ul, ol {
        margin: 10px 0 10px 20px;
    }

    footer {
        text-align: center;
        padding: 15px;
        font-size: 0.9em;
        color: #666;
        background-color: #f0f2f5;
    }

    a {
        color: #004d99;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
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
    <p><strong>Allanos</strong> é um sistema de automação desenvolvido em <strong>Kotlin/Java</strong>, projetado para rodar em <strong>Raspberry Pi</strong> e outros dispositivos. Permite controlar dispositivos de forma inteligente, sendo ideal para projetos de automação residencial, escolar ou experimental.</p>
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
    <h2>Como Contribuir</h2>
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
