<?php
if(isset($_POST['ville'])):

$ville = htmlspecialchars($_POST['ville'], ENT_QUOTES);

try
{
    $bdd = new PDO('mysql:host=localhost;dbname=bdd_temperaturevilles', 'root', '');
}
catch(Exception $e)
{
        die('Erreur : '.$e->getMessage());
}
$bdd->query('SET lc_time_names = "fr_FR"');
$req = $bdd->prepare('SELECT temperature, DATE_FORMAT(last_update, "Le %d %M %Y à %H:%i") AS last_update FROM temperaturevilles WHERE ville = ?');
$req->execute(array($ville));
$donnees = $req->fetch();

echo ($donnees['last_update']);
?>
 il faisait
<?=$donnees['temperature']?>
 °C à 
<?php
echo ucfirst($ville);
$req->closeCursor();
endif
?>
