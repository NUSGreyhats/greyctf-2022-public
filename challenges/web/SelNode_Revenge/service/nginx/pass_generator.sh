for i in {0..9}; do
    password=`cat /dev/urandom | tr -dc '[:alpha:]' | head -c 32`
    printf "team${i}:${password}\n" >> pass.txt
    hashed_password=`openssl passwd -apr1 $password`
    printf "team${i}:${hashed_password}" >> htpasswd/team${i}
    done
