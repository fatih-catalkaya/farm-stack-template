mongosh -- "$MONGO_INITDB_DATABASE" <<EOF
    var database = db.getSiblingDB('$MONGO_INITDB_DATABASE');
    var user = '$MONGO_INITDB_USERNAME';
    var passwd = '$MONGO_INITDB_PASSWORD';
    var dbname = '$MONGO_INITDB_DATABASE';
    database.createUser({user: user, pwd: passwd, roles: [{role: "readWrite", db: dbname}]});
EOF