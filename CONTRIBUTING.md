# Guía para Contribuidores

¡Gracias por tu interés en contribuir a este proyecto! Esta guía te ayudará a empezar.

## 1. Configuración Inicial

### 1.1. Configura tu clave SSH para GitHub

Si aún no te has autenticado con GitHub usando una clave SSH, sigue estos pasos. SSH es más seguro que usar una contraseña.

**a. Genera una nueva clave SSH:**

Abre tu terminal y ejecuta (reemplaza con tu email de GitHub):
```bash
ssh-keygen -t ed25519 -C "tu_email@example.com"
```
Presiona Enter para aceptar la ubicación por defecto y opcionalmente, crea una contraseña para tu clave.

**b. Agrega la clave al ssh-agent:**
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

**c. Agrega la clave a tu cuenta de GitHub:**

Copia tu clave pública.
```bash
cat ~/.ssh/id_ed25519.pub
```
Copia toda la salida, que empieza con `ssh-ed25519...`.

Ve a [https://github.com/settings/keys](https://github.com/settings/keys), haz clic en "New SSH key", dale un título, pega tu clave y guarda.

### 1.2. Haz un "Fork" del Repositorio

Un "fork" es una copia del repositorio en tu propia cuenta de GitHub.

1.  Ve a [https://github.com/OmarAcatlan/proyecto-sistemas-inteligentes](https://github.com/OmarAcatlan/proyecto-sistemas-inteligentes).
2.  Haz clic en el botón "Fork" en la esquina superior derecha.

### 1.3. Clona tu "Fork" a tu PC

Ahora, descarga tu "fork" a tu computadora. Reemplaza `<TU_USUARIO>` con tu nombre de usuario de GitHub.

```bash
git clone git@github.com:<TU_USUARIO>/proyecto-sistemas-inteligentes.git
cd proyecto-sistemas-inteligentes
```

## 2. Proceso de Desarrollo

### 2.1. Crea una Rama de Desarrollo

Crea una nueva rama llamada `dev` para trabajar en tus cambios.

```bash
git checkout -b dev
```

### 2.2. Realiza tus Cambios

Ahora puedes modificar el código. Una vez que hayas terminado, agrega tus cambios y haz un "commit".

```bash
git add .
git commit -m "Agregué una nueva característica increíble"
```

### 2.3. Sube tus Cambios a tu "Fork"

Sube tu rama `dev` a tu repositorio en GitHub.

```bash
git push origin dev
```

## 3. Propón tus Cambios

### 3.1. Crea un "Pull Request"

Un "Pull Request" (PR) es una solicitud para que tus cambios se integren al proyecto principal.

1.  Ve a tu "fork" en GitHub (`https://github.com/<TU_USUARIO>/proyecto-sistemas-inteligentes`).
2.  Verás un botón para "Compare & pull request". Haz clic en él.
3.  Asegúrate de que la rama base sea `master` en el repositorio de `OmarAcatlan/proyecto-sistemas-inteligentes` y la rama de comparación sea `dev` de tu "fork".
4.  Agrega un título y una descripción a tu Pull Request y haz clic en "Create pull request".

¡Y eso es todo! Ahora yo podré revisar tus cambios y, si todo está correcto, los integraré al proyecto.
