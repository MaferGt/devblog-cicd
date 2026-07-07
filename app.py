from app import create_app
from config import Config

#Crear la aplicación usando la factory function
app = create_app()

if __name__ == '__main__':
    # Punto de entrada de la aplicación
    print("Iniciando DevBlog...")
    print(f"Servidor corriendo en: http://{Config.HOST}:{Config.PORT}")
    print("Presiona Ctrl+C para detener el servidor")
    
    # Iniciar el servidor Flask
    app.run(
        host=Config.HOST, # 0.0.0.0 permite conexiones externas
        port=Config.PORT, # Puerto configurado (5000 por defecto)
        debug=Config.DEBUG # Modo debug para desarrollo
    )