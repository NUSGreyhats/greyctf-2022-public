<?php
    // Beauty lies in simplicity

    if(isset($_COOKIE['infos'])){
        foreach($_COOKIE['infos'] as $key => $value) {
            putenv("{$key}={$value}");
        }

        system('echo Hello, $name');
    }

    if(!isset($_COOKIE['infos'])) {
        setcookie('infos[name]', "GreyCat");
        header("Location: ".$_SERVER["REQUEST_URI"]);
    }
?>

<html>
<head>
    <meta charset="UTF-8">
    <title>Greetings from the GreyCat</title>
</head>
<body>
<!-- <a href="?source=1">Show</a> -->
<?php if (isset($_GET['source'])) highlight_file(__FILE__); ?>
</body>
</html>
