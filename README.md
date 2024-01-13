# LEGACY TECHNOLOGY - UNFV JAIRO API

## Credenciales

<!-- aca explico como levantar el proyecto -->


<!-- con este comando se actualiza los requirements
pip freeze > requirements.txt -->
### Credenciales de desarrollo

```bash
# Todo el contenido de este archivo será reconocido como variables de entorno
# Este archivo NO debe subirse a git y es donde deberían guardarse las 
# credenciales y las contraseñas.

# ESTE ARCHIVO DEBE AGREGARSE AL GITIGNORE O TODO EL MUNDO VERÁ TUS CLAVES

FLASK_ENV="development"

DATABASE_URI="postgresql://postgres:legacy23@localhost:5432/legacy_technology"
```


### Credenciales de producción

```bash
# Todo el contenido de este archivo será reconocido como variables de entorno
# Este archivo NO debe subirse a git y es donde deberían guardarse las 
# credenciales y las contraseñas.

# ESTE ARCHIVO DEBE AGREGARSE AL GITIGNORE O TODO EL MUNDO VERÁ TUS CLAVES

FLASK_ENV="development"

DATABASE_URI="postgresql://postgres:legacy23@localhost:5432/legacy_technology"
```