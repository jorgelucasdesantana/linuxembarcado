#!/bin/sh
  


  cp $BASE_DIR/../custom-scripts/S41network-config $BASE_DIR/target/etc/init.d
  chmod +x $BASE_DIR/target/etc/init.d/S41network-config

cp $BASE_DIR/../custom-scripts/teste1.py $BASE_DIR/target/usr/bin
  chmod +x $BASE_DIR/target/usr/bin/teste1.py

#

# inicializa o servidor phyton
str="#!/bin/sh 
\n
python /usr/bin/teste1.py &
\
"

echo $str >  $BASE_DIR/target/etc/init.d/S60ServerInit.sh
chmod +x $BASE_DIR/target/etc/init.d/S60ServerInit.sh







