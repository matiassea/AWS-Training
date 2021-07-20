EC2
Instances => Servidor
Launch Instances
Selecciona sistema operativo => Ubuntu Server "Free tier Eligible"
Step 2: Choose an Instance Type
Se elige el plan a seleccionar => "Free Tier Eligible"
Next

Step 3: Configure Instance Details => Next
Next

Step 4: Add Storage
Next

Step 5: Add Tags
Next

Step 6: Configure Security Group
Security group name: => Grupo e usuarios que entraran a esta instancia
Description:

En la tabla se puede definir el protocolo
Definir lo IP autorizados a ingresar
Se define el tipo de protocolo

SSH TCP 22 Custom
HTTP  TCP 80  Anywhere
HTTPS TCP 442 Anywhere
Custom TCP  3000  Anywhere

Review and Launch

Step 7: Review Instance Launch

Launch


Select an existing key pair or create a new key pair


Choose an existing key pair => Create a new key pair  
key pair name => "Se coloca el nombre"
Download Key

Launch Instance.


Por medio del protocolo SSH conectaremos a esta IP "Public IPv4 address"

