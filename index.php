<?php
try
{
    $bdd = new PDO('mysql:host=localhost;dbname=bdd_temperaturevilles', 'root', '');
}
catch(Exception $e)
{
    die('Erreur : '.$e->getMessage());
}

$liste_villes = $bdd->query('SELECT ville FROM temperaturevilles');
?>
<form method="post" action="affichage_temperature.php">
<select name="ville">
<?php foreach($liste_villes as $ville) {?>
      <option value=<?=$ville[0]?>><?php echo ucfirst($ville[0]);?></option>
<?php } ?>
</select>
<input type="submit" value="Avoir la temperature"/>
</form>
