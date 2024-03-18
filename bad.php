<?php
// connect to the database
$con = mysqli_connect("localhost", "username", "password", "database");
// prepare a statement for inserting data into the table
if (!mysqli_query($con, "INSERT INTO users (name, password) VALUES ('$_POST[name]', 'sha256($_POST[password])'))) {
 echo "Error: ". mysqli_error($con);
} else {
 // successfully added user to database
 echo "User Added";
}
?>
