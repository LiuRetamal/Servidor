cabeceraHTML ="""
<!DOCTYPE html>
<html>
    <head>      
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">        
		
        <!-- Latest compiled and minified CSS -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet">

        <!-- Latest compiled JavaScript -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"></script>

        <link href="css/principal.css" rel="stylesheet">
        <title>{}</title>
        
    </head>    

    <body>
     <div class="container">
            <div class="row">
                <div class="col-3"></div>
                <div class="col-6 text-center">
                    <h3 class="display-3">{}</h3>
        
            
"""
##poner {} para modificar titulo
finalHTML = """

                </div>
                <div class="col-3"></div>
            </div>
        </div>
    </body>
</html>
"""

redireccionHtml = """
<!DOCTYPE html>
<html lang="es">
<head>  
  <meta http-equiv="Refresh" content="{}; URL={}"/>  
</head>
<body>  
    <h3 class='Display-3'>Gracias por usar el servicio secreto del CNI</h3>
</body>
</html>
"""
