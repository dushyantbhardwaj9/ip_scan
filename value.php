<?php
$link = new mysqli("localhost","hemish","pass","dbName");
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
$sql = "SELECT * FROM testtable";
if($result = mysqli_query($link,$sql)){
    if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)){
                $data_arr = array("id" =>  $row['ID'],"backend" =>  $row['VALUE'                                                                                                                                                             ]);
                http_response_code(200);
                 echo json_encode($data_arr);
        }
        mysqli_free_result($result);
    } else{
        echo "No records matching your query were found.";
    }
}else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($link);
}
mysqli_close($link);
?>
