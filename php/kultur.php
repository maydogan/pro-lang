<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<title>Genel kültür</title>
  <head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link rel="stylesheet" type="text/css" href="../css/style.css" />
    <link href="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8/themes/base/jquery-ui.css" rel="stylesheet" type="text/css"/>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5/jquery.min.js"></script>
    <script src="http://ajax.googleapis.com/ajaaax/libs/jqueryui/1.8/jquery-ui.min.js"></script>
	<link href="style.css" rel="stylesheet" type="text/css">
	<html>
		<body >
		<table id = "footer" >
		<tr>
			<td colspan="2" style="background-color:#FFA500;">
				<h3>Bilginizi sınamaya ne dersiniz? </h3>
			</td>
		</tr>
		<tr valign="top">
			<td style="background-color:#FFD700;width:100px;text-align:top;">
				<h3> Genel kültür Testi</h3> <br/>
			</td>
			<td
	style="background-color:#eeeeee;width:500px;text-align:top;">
	</script>
	</script>
    </head>
	<body>
	<br/><br/><br/>
    <div id = "box">
	 <div id = "lb">
	  <div id = "rb">
	   <div id = "bb">
	    <div id = "blc">
	     <div id = "brc">
		  <div id = "tb">
		   <div id = "tlc">
		    <div id = "trc">
			 <div id = "content">
				<dl>
					<dt>
						<h4>
							<?php
									if (!mysql_connect("localhost", "root", "12345"))
										die("Veritabanina baglanamadi...");
									if (!mysql_select_db("bar"))
										die("Veritabani hatali...");

									$soru1 = $_POST['s1'];
									$soru2 = $_POST['s2'];
									$soru3 = $_POST['s3'];
									$soru4 = $_POST['s4'];
									$soru5 = $_POST['s5'];
									if (!$soru1 || !$soru2 || !$soru3 || !$soru4 || !$soru5){
										echo 'Lütfen bütün soruları yanıtlayınız...';
										exit;
									}
									else {
										mysql_query("insert into kul (s1, s2, s3, s4, s5) VALUES('$soru1','$soru2','$soru3','$soru4', '$soru5')");
										$answer = array ('c','b','a','b','b');
										$ques = array("s1" , "s2" , "s3" , "s4" , "s5" );
										$t = 0;
										for($i = 0 ; $i < sizeof($answer) ;$i ++){
											if ($answer[$i] == $_POST[$ques[$i]]){
												$t = $t + 1;
											}	
										}
										echo $t."dogrunuz var...";
									}
							?>
					  </h4>
					</dt>
				  </dl>				
				</div>
			   </div>
			  </div>
			 </div>
			</div>
		   </div>
	     </div>
	    </div>
	   </div>
	  </div>
    </body>
</html>
