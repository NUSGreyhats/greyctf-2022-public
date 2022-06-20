<?php
    include 'secret.php';

    class Greeting {
        private $info = array("name" => "GreyCat");

        public function __wakeup() {
            foreach ($this->info as $key => $value) {
                putenv("{$key}={$value}");
            }
        }

        public function sayHi() {
            system('echo Hello, $name');
        }

    }

    function sign($str) {
        global $secret;
        return hash('sha256', $secret . $str);
    }

    function unserialize_safe($str) {
        return unserialize($str, ['allowed_classes' => ['Greeting']]);
    }

    if(isset($_COOKIE['info']) && isset($_COOKIE['signature'])){
        $serialized_info = $_COOKIE['info'];
        $signature = $_COOKIE['signature'];
        if (hash_equals(sign($serialized_info), $signature) === FALSE) {
            unset($_COOKIE['info']);
            unset($_COOKIE['signature']);
        } else {
            $serialized_info = explode('|', $serialized_info);
            $infos = array_map('unserialize_safe', $serialized_info);
            foreach ($infos as $info) {
                if ($info instanceof Greeting) {
                    $info->sayHi();
                }
            }
        }
    }

    if(!isset($_COOKIE['info']) || !isset($_COOKIE['signature'])) {
        $greeting = [new Greeting];
        $serialized_info = implode(' ', array_map('serialize', $greeting));
        setcookie('info', $serialized_info);
        setcookie('signature', sign($serialized_info));
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
