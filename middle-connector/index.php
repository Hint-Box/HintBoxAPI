<?php 
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    
    $dbh = pg_connect("host=localhost dbname=data user=postgres");
    
    if (!$dbh) {
        
        die("Error in connection: " . pg_last_error());
        
    }
    
    $sql = "SELECT * FROM miembros;";
    
    $result = pg_query($dbh, $sql);
    
    if (!$result) {
        
        die("Error in SQL query: " . pg_last_error());
        
    }
    
    pg_free_result($result);
    
    foreach ($_POST as $value) {
        $post = $value;
    }
    
    $sql = "INSERT INTO miembros(membername) VALUES (" . $post . ");";
    
    $result = pg_query($dbh, $sql);
    
    if (!$result) {
        
        die("Error in SQL query: " . pg_last_error());
        
    }
    
    pg_close($dbh);
}

?>
